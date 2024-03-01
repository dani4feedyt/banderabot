import discord
from itertools import cycle
import tictactoe

X = "X"
O = "O"
EMPTY = None

current_label = ["X", "O"]

myIterator = cycle(range(2))

matrix = [[EMPTY, EMPTY, EMPTY],
          [EMPTY, EMPTY, EMPTY],
          [EMPTY, EMPTY, EMPTY]]


# user = None
# board = ttt.initial_state()
# ai_turn = False

class Buttons(discord.ui.View):

    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)


    @discord.ui.button(label="ㅤ", row=0, style=discord.ButtonStyle.primary)
    async def button_callback(self, interaction, button: discord.ui.Button):
        label = current_label[next(myIterator)]
        button.label = label
        button.disabled = True
        matrix[button.row][0] = label
        await interaction.response.edit_message(content=matrix, view=self)



    @discord.ui.button(label="ㅤ", row=0, style=discord.ButtonStyle.primary)
    async def second_button_callback(self, interaction, button: discord.ui.Button):
        label = current_label[next(myIterator)]
        button.label = label
        button.disabled = True
        matrix[button.row][1] = label
        await interaction.response.edit_message(content=matrix, view=self)

    @discord.ui.button(label="ㅤ", row=0, style=discord.ButtonStyle.primary)
    async def third_button_callback(self, interaction, button: discord.ui.Button):
        label = current_label[next(myIterator)]
        button.label = label
        button.disabled = True
        matrix[button.row][2] = label
        await interaction.response.edit_message(content=matrix, view=self)

    @discord.ui.button(label="ㅤ", row=1, style=discord.ButtonStyle.primary)
    async def fourth_button_callback(self, interaction, button: discord.ui.Button):
        label = current_label[next(myIterator)]
        button.label = label
        button.disabled = True
        matrix[button.row][0] = label
        await interaction.response.edit_message(content=matrix, view=self)

    @discord.ui.button(label="ㅤ", row=1, style=discord.ButtonStyle.primary)
    async def fifth_button_callback(self, interaction, button: discord.ui.Button):
        label = current_label[next(myIterator)]
        button.label = label
        button.disabled = True
        matrix[button.row][1] = label
        await interaction.response.edit_message(content=matrix, view=self)

    @discord.ui.button(label="ㅤ", row=1, style=discord.ButtonStyle.primary)
    async def sixth_button_callback(self, interaction, button: discord.ui.Button):
        label = current_label[next(myIterator)]
        button.label = label
        button.disabled = True
        matrix[button.row][2] = label
        await interaction.response.edit_message(content=matrix, view=self)

    @discord.ui.button(label="ㅤ", row=2, style=discord.ButtonStyle.primary)
    async def seventh_button_callback(self, interaction, button: discord.ui.Button):
        label = current_label[next(myIterator)]
        button.label = label
        button.disabled = True
        matrix[button.row][0] = label
        await interaction.response.edit_message(content=matrix, view=self)

    @discord.ui.button(label="ㅤ", row=2, style=discord.ButtonStyle.primary)
    async def eighth_button_callback(self, interaction, button: discord.ui.Button):
        label = current_label[next(myIterator)]
        button.label = label
        button.disabled = True
        matrix[button.row][1] = label
        await interaction.response.edit_message(content=matrix, view=self)

    @discord.ui.button(label="ㅤ", row=2, style=discord.ButtonStyle.primary)
    async def ninth_button_callback(self, interaction, button: discord.ui.Button):
        label = current_label[next(myIterator)]
        button.label = label
        button.disabled = True
        matrix[button.row][2] = label
        await interaction.response.edit_message(content=matrix, view=self)
