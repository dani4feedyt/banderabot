import discord
import tictactoe as ttt
import time

X = "X"
O = "O"
EMPTY = None

user_player: int

current_label = [X, O]

movemap = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

wintxt = None

ai_turn = False


class Select(discord.ui.View):
    def __init__(self):
        super().__init__()
        print("proooooc")


    @discord.ui.button(label=X, row=1, style=discord.ButtonStyle.success)
    async def x_callback(self, interaction, button: discord.ui.Button):
        button.disabled = True
        await interaction.response.edit_message(content="Ви обрали грати за хрестика!", view=self)
        global user_player
        user_player = 0
        player_select()
        print("player", player_select())
        Select.stop(self)
        msg = await interaction.original_response()
        await msg.edit(view=TicTacToe())

    @discord.ui.button(label=O, row=1, style=discord.ButtonStyle.danger)
    async def o_callback(self, interaction, button: discord.ui.Button):
        button.disabled = True
        await interaction.response.edit_message(content="Ви обрали грати за нолика!", view=self)
        global user_player
        user_player = 1
        player_select()
        print("player", player_select())
        Select.stop(self)
        msg = await interaction.original_response()
        await msg.edit(view=TicTacToe())


def clearup():
    global wintxt
    global ai_turn
    TicTacToe.board = ttt.initial_state(0)
    ai_turn = False
    wintxt = None


def player_select():
    global user_player
    global current_label
    ai_p = 1
    if ai_p == user_player:
        ai_p = 0

    user_p = current_label[user_player]
    ai_p = current_label[ai_p]

    # if user_p == O:
    #     current_label = [O, X]
    # else:
    #     current_label = [X, O]

    return user_p, ai_p


def ai_func(self, board, view):

    global ai_turn

    move = ()
    game_over = ttt.terminal(view.board)[0]
    player = ttt.player(view.board)
    print("plaaaay", player)

    if not game_over:
        print(f"Computer thinking...")

    if player_select()[0] != player and not game_over:
        if ai_turn:
            time.sleep(0.5)
            move = ttt.minimax(view.board)
            view.board = ttt.result(view.board, move)

            move_coord = movemap.index(move)
            x = movemap[move_coord][0]
            print(x)
            y = movemap[move_coord][1]
            print(y)
            print("view_board", view.board)

            print(move)
            print(move_coord)

            ai_turn = False
        else:
            ai_turn = True

        return view.board, move


class Button(discord.ui.Button['TicTacToe']):
    def __init__(self, x: int, y: int, label, style, disabled):
        super().__init__(style=style, label=label, row=y, disabled=disabled)
        self.x = x
        self.y = y

    async def callback(self, interaction: discord.Interaction):
        view: TicTacToe = self.view
        player = ttt.player(view.board)
        self.label = player
        view.board[self.y][self.x] = self.label
        self.disabled = True
        self.content = view.board
        await interaction.response.edit_message(content=self.content, view=view)
        msg = await interaction.original_response()
        if not ttt.terminal(view.board)[0]:
            if ai_func(self, view.board, view)[0] is not None:
                await msg.edit(content=ai_func(self, view.board, view)[0], view=view)
        else:
            print("NON((")

        view.recreate_board(view.board)
        if wintxt is not None:
             await msg.edit(content=wintxt)

        await msg.edit(view=view)

class TicTacToe(discord.ui.View):
    children: list[Button]

    def __init__(self):
        super().__init__()
        print("proc")
        clearup()

        self.board = ttt.initial_state(0)
        print("ini_board", self.board)##########deeeeeeeeeep copy

        if user_player == 1:
            self.board = ttt.initial_state(1)

        self.recreate_board(self.board) ########

    def recreate_board(self, board):
        self.clear_items()
        global wintxt
        for x in range(3):
            for y in range(3):
                style = discord.ButtonStyle.secondary
                if board[y][x] is None:
                    label = 'ㅤ'
                    disabled = False
                else:
                    if board[y][x] == X:
                        style = discord.ButtonStyle.success
                    elif board[y][x] == O:
                        style = discord.ButtonStyle.danger
                    label = board[y][x]
                    disabled = True

                if ttt.terminal(self.board)[0]:
                    disabled = True
                    winner = ttt.winner(self.board)
                    if winner is None:
                        wintxt = "Гра закінчена: Нічия."
                    else:
                        wintxt = f"Гра закінчена: {winner} переміг."

                print("board", board)
                print("ini", ttt.initial_state(0))
                self.add_item(Button(x, y, label, style, disabled))
