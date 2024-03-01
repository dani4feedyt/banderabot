import discord
from itertools import cycle
import tictactoe as ttt
import time

X = "X"
O = "O"
EMPTY = None

current_label = ["X", "O"]

movemap = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

myIterator = cycle(range(2))

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
        time.sleep(0.5)
        move = ttt.minimax(view.board)
        view.board = ttt.result(view.board, move)

        move_coord = movemap.index(move)
        x = movemap[move_coord][0]
        print(x)
        y = movemap[move_coord][1]
        print(y)
        print(view.board)


        # Button.callback().label = 1

        print(move)
        print(move_coord)
        next(myIterator)

        return view.board, move

# def button_autopress(move, button):
#     button

class Button(discord.ui.Button['TicTacToe']):
    def __init__(self, x: int, y: int, label):
        super().__init__(style=discord.ButtonStyle.secondary, label=label, row=y)
        self.x = x
        self.y = y

    async def callback(self, interaction: discord.Interaction):
        view: TicTacToe = self.view
        turn = current_label[next(myIterator)]
        self.style = discord.ButtonStyle.success
        self.label = turn
        view.board[self.y][self.x] = self.label
        self.disabled = True
        self.content = view.board
        await interaction.response.edit_message(content=self.content, view=view)
        msg = await interaction.original_response()
        await msg.edit(content=ai_func(self, view.board, view)[0], view=view)
        view.recreate_board()

class TicTacToe(discord.ui.View):
    children: list[Button]

    def __init__(self):
        super().__init__()

        self.board = ttt.initial_state()
        self.recreate_board()

    def recreate_board(self):
        self.clear_items()
        for x in range(3):
            for y in range(3):
                if self.board[x][y] is None:
                    label = 'ㅤ'
                else:
                    label = self.board[x][y]
                print(label)
                self.add_item(Button(x, y, label))


        # for x in range(3):
        #     for y in range(3):
        #         self.remove_item(Button(x, y))



# class Field(discord.ui.View):
#     def __init__(self, *, timeout=180):
#         super().__init__(timeout=timeout)
#
#     @discord.ui.button(label="ㅤ", custom_id="0", row=0, style=discord.ButtonStyle.primary)
#     async def button_callback(self, interaction, button: discord.ui.Button):
#         label = current_label[next(myIterator)]
#         button.label = label
#         button.disabled = True
#         board[button.row][0] = label
#         await interaction.response.edit_message(content=board, view=self)
#         ai_func(board, button)
#
#
#     @discord.ui.button(label="ㅤ", custom_id="1", row=0, style=discord.ButtonStyle.primary)
#     async def second_button_callback(self, interaction, button: discord.ui.Button):
#         label = current_label[next(myIterator)]
#         button.label = label
#         button.disabled = True
#         board[button.row][1] = label
#         await interaction.response.edit_message(content=board, view=self)
#         ai_func(board, button)
#
#     @discord.ui.button(label="ㅤ", custom_id="2", row=0, style=discord.ButtonStyle.primary)
#     async def third_button_callback(self, interaction, button: discord.ui.Button):
#         label = current_label[next(myIterator)]
#         button.label = label
#         button.disabled = True
#         board[button.row][2] = label
#         await interaction.response.edit_message(content=board, view=self)
#         ai_func(board)
#
#     @discord.ui.button(label="ㅤ", custom_id="3", row=1, style=discord.ButtonStyle.primary)
#     async def fourth_button_callback(self, interaction, button: discord.ui.Button):
#         label = current_label[next(myIterator)]
#         button.label = label
#         button.disabled = True
#         board[button.row][0] = label
#         await interaction.response.edit_message(content=board, view=self)
#         ai_func(board)
#
#     @discord.ui.button(label="ㅤ", custom_id="4", row=1, style=discord.ButtonStyle.primary)
#     async def fifth_button_callback(self, interaction, button: discord.ui.Button):
#         label = current_label[next(myIterator)]
#         button.label = label
#         button.disabled = True
#         board[button.row][1] = label
#         await interaction.response.edit_message(content=board, view=self)
#         ai_func(board)
#
#     @discord.ui.button(label="ㅤ", custom_id="5", row=1, style=discord.ButtonStyle.primary)
#     async def sixth_button_callback(self, interaction, button: discord.ui.Button):
#         label = current_label[next(myIterator)]
#         button.label = label
#         button.disabled = True
#         board[button.row][2] = label
#         await interaction.response.edit_message(content=board, view=self)
#         ai_func(board)
#
#     @discord.ui.button(label="ㅤ", custom_id="6", row=2, style=discord.ButtonStyle.primary)
#     async def seventh_button_callback(self, interaction, button: discord.ui.Button):
#         label = current_label[next(myIterator)]
#         button.label = label
#         button.disabled = True
#         board[button.row][0] = label
#         await interaction.response.edit_message(content=board, view=self)
#         ai_func(board)
#
#     @discord.ui.button(label="ㅤ", custom_id="7", row=2, style=discord.ButtonStyle.primary)
#     async def eighth_button_callback(self, interaction, button: discord.ui.Button):
#         label = current_label[next(myIterator)]
#         button.label = label
#         button.disabled = True
#         board[button.row][1] = label
#         await interaction.response.edit_message(content=board, view=self)
#         ai_func(board)
#
#     @discord.ui.button(label="ㅤ", custom_id="8", row=2, style=discord.ButtonStyle.primary)
#     async def ninth_button_callback(self, interaction, button: discord.ui.Button):
#         label = current_label[next(myIterator)]
#         button.label = label
#         button.disabled = True
#         board[button.row][2] = label
#         await interaction.response.edit_message(content=board, view=self)
#         ai_func(board)
