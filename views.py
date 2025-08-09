import discord


class G_R(discord.ui.View):
    def __init__(self, author, grnb_f, redb_f):
        super().__init__()
        self.author = author
        self.grnb_f = grnb_f
        self.redb_f = redb_f

    @discord.ui.button(label="Так", row=1, style=discord.ButtonStyle.success)
    async def g_callback(self, interaction, button: discord.ui.Button):
        await self.grnb_f()
        button.disabled = True

    @discord.ui.button(label="Ні", row=1, style=discord.ButtonStyle.danger)
    async def r_callback(self, interaction, button: discord.ui.Button):
        await self.redb_f()
        button.disabled = True

    async def interaction_check(self, interaction: discord.Interaction):
        return interaction.user.id == self.author.id
