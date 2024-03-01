import discord


class Buttons(discord.ui.View):

    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)

    @discord.ui.button(label="ㅤ", row=0, style=discord.ButtonStyle.primary)
    async def button_callback(self, interaction, button: discord.ui.Button):
        button.label = "X"
        await interaction.response.edit_message(content="0.0", view=self)

    @discord.ui.button(label="ㅤ", row=0, style=discord.ButtonStyle.primary)
    async def second_button_callback(self, interaction, button: discord.ui.Button):
        button.label = "X"
        await interaction.response.edit_message(content="0.1", view=self)

    @discord.ui.button(label="ㅤ", row=0, style=discord.ButtonStyle.primary)
    async def third_button_callback(self, interaction, button: discord.ui.Button):
        button.label = "X"
        await interaction.response.edit_message(content="0.2", view=self)

    @discord.ui.button(label="ㅤ", row=1, style=discord.ButtonStyle.primary)
    async def fourth_button_callback(self, interaction, button: discord.ui.Button):
        button.label = "X"
        await interaction.response.edit_message(content="1.0", view=self)

    @discord.ui.button(label="ㅤ", row=1, style=discord.ButtonStyle.primary)
    async def fifth_button_callback(self, interaction, button: discord.ui.Button):
        button.label = "X"
        await interaction.response.edit_message(content="1.1", view=self)

    @discord.ui.button(label="ㅤ", row=1, style=discord.ButtonStyle.primary)
    async def sixth_button_callback(self, interaction, button: discord.ui.Button):
        button.label = "X"
        await interaction.response.edit_message(content="1.2", view=self)

    @discord.ui.button(label="ㅤ", row=2, style=discord.ButtonStyle.primary)
    async def seventh_button_callback(self, interaction, button: discord.ui.Button):
        button.label = "X"
        await interaction.response.edit_message(content="2.0", view=self)

    @discord.ui.button(label="ㅤ", row=2, style=discord.ButtonStyle.primary)
    async def eighth_button_callback(self, interaction, button: discord.ui.Button):
        button.label = "X"
        await interaction.response.edit_message(content="2.1", view=self)

    @discord.ui.button(label="ㅤ", row=2, style=discord.ButtonStyle.primary)
    async def ninth_button_callback(self, interaction, button: discord.ui.Button):
        button.label = "X"
        await interaction.response.edit_message(content="2.2", view=self)