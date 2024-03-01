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

board = ttt.initial_state()

def ai_func(board, button):

    game_over = ttt.terminal(board)[0]
    player = ttt.player(board)

    if game_over:
        winner = ttt.winner(board)
        if winner is None:
            print(f"Game Over: Tie.")
        else:
            print(f"Game Over: {winner} wins.")
    else:
        print(f"Computer thinking...")
        time.sleep(0.5)
        move = ttt.minimax(board)
        board = ttt.result(board, move)

        move_coord = movemap.index(move)

        # discord.ui.Button['custom_id' = 1]
        print(move)
        print(move_coord)
        print("Bbbb", button.custom_id)

        return board, move

# def button_autopress(move, button):
#     button

class Buttons(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)

    @discord.ui.button(label="ㅤ", custom_id="0", row=0, style=discord.ButtonStyle.primary)
    async def button_callback(self, interaction, button: discord.ui.Button):
        label = current_label[next(myIterator)]
        button.label = label
        button.disabled = True
        board[button.row][0] = label
        await interaction.response.edit_message(content=board, view=self)
        ai_func(board, button)


    @discord.ui.button(label="ㅤ", custom_id="1", row=0, style=discord.ButtonStyle.primary)
    async def second_button_callback(self, interaction, button: discord.ui.Button):
        label = current_label[next(myIterator)]
        button.label = label
        button.disabled = True
        board[button.row][1] = label
        await interaction.response.edit_message(content=board, view=self)
        ai_func(board, button)

    @discord.ui.button(label="ㅤ", custom_id="2", row=0, style=discord.ButtonStyle.primary)
    async def third_button_callback(self, interaction, button: discord.ui.Button):
        label = current_label[next(myIterator)]
        button.label = label
        button.disabled = True
        board[button.row][2] = label
        await interaction.response.edit_message(content=board, view=self)
        ai_func(board)

    @discord.ui.button(label="ㅤ", custom_id="3", row=1, style=discord.ButtonStyle.primary)
    async def fourth_button_callback(self, interaction, button: discord.ui.Button):
        label = current_label[next(myIterator)]
        button.label = label
        button.disabled = True
        board[button.row][0] = label
        await interaction.response.edit_message(content=board, view=self)
        ai_func(board)

    @discord.ui.button(label="ㅤ", custom_id="4", row=1, style=discord.ButtonStyle.primary)
    async def fifth_button_callback(self, interaction, button: discord.ui.Button):
        label = current_label[next(myIterator)]
        button.label = label
        button.disabled = True
        board[button.row][1] = label
        await interaction.response.edit_message(content=board, view=self)
        ai_func(board)

    @discord.ui.button(label="ㅤ", custom_id="5", row=1, style=discord.ButtonStyle.primary)
    async def sixth_button_callback(self, interaction, button: discord.ui.Button):
        label = current_label[next(myIterator)]
        button.label = label
        button.disabled = True
        board[button.row][2] = label
        await interaction.response.edit_message(content=board, view=self)
        ai_func(board)

    @discord.ui.button(label="ㅤ", custom_id="6", row=2, style=discord.ButtonStyle.primary)
    async def seventh_button_callback(self, interaction, button: discord.ui.Button):
        label = current_label[next(myIterator)]
        button.label = label
        button.disabled = True
        board[button.row][0] = label
        await interaction.response.edit_message(content=board, view=self)
        ai_func(board)

    @discord.ui.button(label="ㅤ", custom_id="7", row=2, style=discord.ButtonStyle.primary)
    async def eighth_button_callback(self, interaction, button: discord.ui.Button):
        label = current_label[next(myIterator)]
        button.label = label
        button.disabled = True
        board[button.row][1] = label
        await interaction.response.edit_message(content=board, view=self)
        ai_func(board)

    @discord.ui.button(label="ㅤ", custom_id="8", row=2, style=discord.ButtonStyle.primary)
    async def ninth_button_callback(self, interaction, button: discord.ui.Button):
        label = current_label[next(myIterator)]
        button.label = label
        button.disabled = True
        board[button.row][2] = label
        await interaction.response.edit_message(content=board, view=self)
        ai_func(board)
