import random
import os

import discord
from discord.ext import tasks
from discord.ext import commands

from lists import activity_text
from key import key

intents = discord.Intents.all()
intents.members = True

user_errors = []

bot = commands.Bot(command_prefix="!",
                   intents = intents,
                   case_insensitive=True,
                   help_command=None
                   )

@tasks.loop(minutes=5)
async def update_presence():
    randomtext = random.choice(activity_text)
    await bot.change_presence(activity=discord.Game(randomtext))
    print(f"Nouveau statut du bot : {randomtext}")

@bot.event
async def on_ready():
    
    print("Bot démarré")
    print("--------------------------------")
    update_presence.start()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        userid = ctx.author.id
        if not userid in user_errors:
            user_errors[userid] = 1
        else:
            user_errors[userid] += 1

        number_of_error = user_errors[userid]
        if number_of_error < 5:
            await ctx.respond("ta pas les permissions")

        if number_of_error < 10:
            await ctx.respond("poto ça fais plus de 5 fois je te dis t'as pas les perm arrete sale fdp :skull:")

#@bot.event
#async def on_application_command_error(ctx,error):
#    await ctx.respond("Une erreur est survenue")
#    if isinstance(error,commands.MissingPermissions):
#        await ctx.respond("Vous n'avez pas la permission d'éxecuter cette commande")


@bot.slash_command(description= "Envoie une liste des commandes")
async def help(ctx):

    embed = discord.Embed(title="Commandes d'aide",color=0x51bde8)
    for command in bot.walk_application_commands():
        embed.add_field(name=f"__{command.name}__",value=command.description,inline=False)


    await ctx.respond(embed=embed)

for file in os.listdir("cogs"):
    if not file.endswith(".py"): continue
    
    file_name = file[:-3]
    bot.load_extension(f"cogs.{file_name}")

bot.run(key)


