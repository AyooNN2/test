import discord
from discord.ext import commands
from discord import Interaction


class Buttons(discord.ui.View):
  def __init__(self):
    super().__init__(timeout=10)

    joinbutton = discord.ui.Button(label='Rejoindre le discord de Dewas', 
                                   style=discord.ButtonStyle.green, 
                                   url='https://discord.gg/dAaTAJwEzX')
    
    self.add_item(joinbutton)

    robloxbutton = discord.ui.Button(label="Profil Roblox", 
                                     style=discord.ButtonStyle.red, 
                                     url='https://www.roblox.com/users/421310257/profile')
    
    self.add_item(robloxbutton)
    
  async def command_callback(self, button, interaction):
    await interaction.response.send_message("eu")


class UI(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.slash_command(name="buttons",description="Test de boutons")
    async def buttons(self,ctx):
        view = Buttons()
        await ctx.respond("Il y a deux boutons :",view=view)
        await view.wait()


def setup(bot):
    bot.add_cog(UI(bot))
