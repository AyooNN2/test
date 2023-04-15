import discord
from discord.ext import commands

class hellomessage(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = self.bot.get_channel(924134472578908172)
        await channel.send("quitte le serv "+member.name+", t pas le bienvenu")
        isOnMobile = member.is_on_mobile()
        if isOnMobile: 
            await channel.send("T SUR MOBILE BOUFONS ! MDR")
        else:
            await channel.send("eus t pas sur mobiles tois")

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(924134472578908172)
        if not member.bot:
            await channel.send(member.name+"#"+member.discriminator+" a quitté le serveur")
        else:
            await channel.send("diz freeking bot")




        

def setup(bot):
    bot.add_cog(hellomessage(bot))
