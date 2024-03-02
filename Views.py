import discord
from itertools import cycle
import tictactoe as ttt
import time

X = "X"
O = "O"
EMPTY = None

user_player: int

current_label = ["X", "O"]

movemap = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

myIterator = cycle(range(2))

triggered = False


class Select(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.board = ttt.ini


    @discord.ui.button(label="X", row=1, style=discord.ButtonStyle.success)
    async def x_callback(self, interaction, button: discord.ui.Button):
        button.disabled = True
        await interaction.response.edit_message(content="Ви обрали грати за хрестика!", view=self)
        global user_player
        user_player = 0
        Select.stop(self)
        msg = await interaction.original_response()
        await msg.edit(view=TicTacToe())

    @discord.ui.button(label="O", row=1, style=discord.ButtonStyle.danger)
    async def o_callback(self, interaction, button: discord.ui.Button):
        button.disabled = True
        await interaction.response.edit_message(content="Ви обрали грати за нолика!", view=self)
        global user_player
        user_player = 1
        Select.stop(self)
        msg = await interaction.original_response()
        await msg.edit(view=TicTacToe())


def clearup():
    TicTacToe.board = ttt.initial_state(0)
    global triggered
    triggered = False


def player_select():
    global user_player
    ai_p = 1
    if ai_p == user_player:
        ai_p = 0

    user_p = current_label[user_player]
    ai_p = current_label[user_player]

    return user_p, ai_p


def ai_func(self, board, view):

    game_over = ttt.terminal(view.board)[0]
    player = ttt.player(view.board)

    if game_over:
        winner = ttt.winner(view.board)
        if winner is None:
            print(f"Game Over: Tie.")
        else:
            print(f"Game Over: {winner} wins.")
    else:
        print(f"Computer thinking...")

    if player_select()[0] != player and not game_over:
        time.sleep(0.5)
        move = ttt.minimax(view.board)
        view.board = ttt.result(view.board, move)

        move_coord = movemap.index(move)
        x = movemap[move_coord][0]
        print(x)
        y = movemap[move_coord][1]
        print(y)
        print(view.board)

        print(move)
        print(move_coord)
        next(myIterator)

        return view.board, move


class Button(discord.ui.Button['TicTacToe']):
    def __init__(self, x: int, y: int, label, style, disabled):
        super().__init__(style=style, label=label, row=y, disabled=disabled)
        self.x = x
        self.y = y

    async def callback(self, interaction: discord.Interaction):
        view: TicTacToe = self.view
        turn = current_label[next(myIterator)]
        self.label = turn
        view.board[self.y][self.x] = self.label
        self.disabled = True
        self.content = view.board
        await interaction.response.edit_message(content=self.content, view=view)
        msg = await interaction.original_response()
        await msg.edit(content=ai_func(self, view.board, view)[0], view=view)
        view.recreate_board() ##########
        await msg.edit(view=view)

class TicTacToe(discord.ui.View):
    children: list[Button]

    def __init__(self):
        super().__init__()

        self.board = ttt.ini ##########deeeeeeeeeep copy

        global triggered
        if user_player == 1:
            self.board = ttt.initial_state(1)
            if not triggered:
                next(myIterator)
            triggered = True

        self.recreate_board() ########

    def recreate_board(self):
        self.clear_items()
        for x in range(3):
            for y in range(3):
                style = discord.ButtonStyle.secondary
                if self.board[y][x] is None:
                    label = 'ㅤ'
                    disabled = False
                else:
                    if self.board[y][x] == current_label[0]:
                        style = discord.ButtonStyle.success
                    elif self.board[y][x] == current_label[1]:
                        style = discord.ButtonStyle.danger
                    label = self.board[y][x]
                    disabled = True
                print(self.board)
                print(ttt.ini)
                self.add_item(Button(x, y, label, style, disabled))
