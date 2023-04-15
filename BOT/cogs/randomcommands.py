import discord
from discord.ext import commands
import random
from lists import music

class randomcommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.slash_command(name = "random-music",description = "Donne une musique aléatoire choisie par mes soins en 2021")
    async def random_music(self,ctx):
        await ctx.respond(ctx.author.mention+", Voici votre musique : "+random.choice(music))

    @commands.Cog.listener()
    async def on_message(self,message):
        if "sex" in message.content.lower():
            a = "mot sussy dans le message"
            print(a)
            await message.add_reaction("🍑")
            await message.add_reaction("🍆")
            await message.add_reaction("😱")


def setup(bot):
    bot.add_cog(randomcommands(bot))

