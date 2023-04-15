import asyncio

import discord
from discord.ext import commands
from discord.utils import get

created_vc = []

time_before_delete = 360

class admin(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    
    @commands.slash_command(description = "Envoie un message privé a l'utilisateur mentionné")
    @commands.has_permissions(administrator=True)
    async def dm(self,ctx,user :discord.Member,*,message=None):
        if discord.Member == None:
            await ctx.respond("Vous devez mentionner quelqu'un pour lui envoyer un message privé")
            
        else:
            try:
                await user.send(message)
                await ctx.respond("Un message a été envoyé à "+user.name+"!")
            
            except Exception as e:
                await ctx.respond("Impossible d'envoyer de message à cet utilisateur.")
            
                if e.code == 50007:
                    await ctx.send("Cet utilisateur a désactivé ses messages privés.")
                else:
                    await ctx.respond(e)


        

    @commands.slash_command(description="Met un rôle spécifié à l'utilisateur mentionné")
    @commands.has_permissions(manage_roles = True)
    async def giverole(self,ctx,user : discord.Member,*,role: discord.Role):
        if role in user.roles:
            await ctx.respond(f"{user.mention} a déjà le role {role}!")
        else:
            await user.add_roles(role)
            await ctx.respond(f"J'ai ajouté le rôle {role} à {user.mention}")


    @commands.slash_command(description="Enlève un rôle spécifié à l'utilisateur mentionné")
    @commands.has_permissions(manage_roles = True)
    async def removerole(self,ctx,user : discord.Member,*,role: discord.Role):
        if role in user.roles:
            await user.remove_roles(role)
            await ctx.respond(f"J'ai enlevé le rôle {role} à {user.mention}")
            
        else:
           await ctx.respond(f"{user.mention} n'a pas le role {role}!")



    #MUTE COMMANDS 
    @commands.slash_command(description="Mute une personne")
    @commands.has_permissions(manage_messages = True)
    async def mute(self,ctx,user : discord.Member):
       role = discord.utils.get(ctx.guild.roles, id=int(1096492574560235532))
       if role in user.roles:
            await ctx.respond(f"{user.mention} est déjà muted !")
            
       else:
           await user.add_roles(role)
           await ctx.respond(f"{user.mention} s'est fais mute ! jetez lui des tomates ce loser")

    @commands.slash_command(description="Démute une personne")
    @commands.has_permissions(manage_messages = True)
    async def unmute(self,ctx,user : discord.Member):
       role = discord.utils.get(ctx.guild.roles, id=int(1096492574560235532))
       if not role in user.roles:
            await ctx.respond(f"{user.mention} n'est pas mute !")
            
       else:
           await user.remove_roles(role)
           await ctx.respond(f"{user.mention} s'est fais démute mais fais attention quand meme")


    #CREATE VC COMMAND
    @commands.slash_command(name="create-vc",description="Crée un vocal pour vous (temporaire)")
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1,30,commands.BucketType.user)
    async def create_vc(self,ctx,name=None):
        if name == None:
            name = f"Salon de {ctx.author.name}"
        category = discord.utils.get(ctx.guild.categories,id = 924134472578908171)
        channel = await ctx.guild.create_voice_channel(name=name,
                                             category=category,
                                             reason = f"Création de salon par {ctx.author.name}#{ctx.author.discriminator}")

        await ctx.respond(f"Un salon vocal du nom de **{name}** à été crée par {ctx.author.mention} !")
        created_vc.append(channel)
        
        await asyncio.sleep(time_before_delete)
        if len(channel.members) != 0: return

        created_vc.remove(channel)
        await channel.delete(reason="Auto-suppression")

    #AUTO DESTROY VC
    @commands.Cog.listener()
    async def on_voice_state_update(self,member,before,after):
        channel = before.channel

        if after.channel is not None: return
        if channel not in created_vc: return
        if len(channel.members) != 0: return

        await asyncio.sleep(time_before_delete)

        if len(channel.members) != 0: return

        created_vc.remove(channel)
        await channel.delete(reason="Auto-suppression")
                    
            



        
        


def setup(bot):
    bot.add_cog(admin(bot))