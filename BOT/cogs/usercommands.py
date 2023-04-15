import discord
import time
from discord.ext import commands

class usercommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.slash_command(name = "userinfo", description = "Affiche des informations sur l'utilisateur mentionné (Nom, Tag, Id et date de création du compte)")
    async def user(self,ctx,user :discord.Member = None):
        if user is None:
            list_of_roles = []
            
            created_at = int(ctx.author.created_at.timestamp())
            joined_at = int(ctx.author.joined_at.timestamp())

            embed = discord.Embed(color=0xa385ff)

            embed.set_author(name=f"{ctx.author.name}#{ctx.author.discriminator}",icon_url=ctx.author.avatar.url)

            embed.set_thumbnail(url=ctx.author.avatar.url)
            embed.add_field(name="",value=ctx.author.mention,inline=False)
            embed.add_field(name="ID",value=ctx.author.id,inline=True)
            embed.add_field(name="Nickname",value=ctx.author.nick,inline=True)
            embed.add_field(name="Crée le",value=f"<t:{created_at}:D> (<t:{created_at}:R>)",inline=False)
            embed.add_field(name="Crée le",value=f"<t:{joined_at}:D> (<t:{joined_at}:R>)",inline=False)
            for role in list(reversed(ctx.author.roles)):
                if role.name != "@everyone":
                    list_of_roles.append(role.mention)
                string_of_roles = ", ".join(list_of_roles)

            if string_of_roles != "":
                embed.add_field(name=f"Rôles [{len(list_of_roles)}]",value=string_of_roles)
            else:
                embed.add_field(name="Rôles",value="Pas de rôle")
        else:
            list_of_roles = []


            created_at = int(user.created_at.timestamp())
            joined_at = int(user.joined_at.timestamp())

            embed = discord.Embed(color=0xa385ff)

            embed.set_author(name=f"{user.name}#{user.discriminator}",icon_url=user.avatar.url)
            embed.set_thumbnail(url=user.avatar.url)
            embed.add_field(name="",value=user.mention,inline=False)
            embed.add_field(name="ID",value=user.id,inline=True)
            embed.add_field(name="Nickname",value=user.nick,inline=True)
            embed.add_field(name="Crée le",value=f"<t:{created_at}:D> (<t:{created_at}:R>)",inline=False)
            embed.add_field(name="Crée le",value=f"<t:{joined_at}:D> (<t:{joined_at}:R>)",inline=False)


            for role in list(reversed(user.roles)):
                if role.name != "@everyone":
                    list_of_roles.append(role.mention)
                string_of_roles = ", ".join(list_of_roles)

            if string_of_roles != "":
                embed.add_field(name=f"Rôles [{len(list_of_roles)}]",value=string_of_roles)
            else:
                embed.add_field(name="Rôles",value="Pas de rôle")


            
        await ctx.respond(embed = embed)
        



def setup(bot):
    bot.add_cog(usercommands(bot))