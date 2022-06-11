import variables
import discord
from discord.ext import commands
import json

import logging
import sys
import inspect

from os import getcwd
import datetime
class moderation(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.Cog.listener()
  async def on_ready(self):
    print(f'{getcwd()} => cogs/moderation.py loaded')

  @commands.command(name="auto",aliases=["automod", "perspective", "toxicity", "toxic"])
  @commands.has_permissions(manage_guild=True)
  async def auto(self, ctx, _input=None):
    logging.info(f"{sys._getframe().f_code.co_name} ran in {ctx.guild.name} ({ctx.guild.id})")
    with open("./json/settings/server.json", "r") as f:
      settings = json.load(f)
    if "moderation" not in settings[str(ctx.guild.id)]:
      settings[str(ctx.guild.id)]["moderation"] = False
      with open("./json/settings/server.json", "w") as f:
        json.dump(settings, f, indent=4)
    
    if "automod" not in settings[str(ctx.guild.id)]["settings"]:
      settings[str(ctx.guild.id)]["settings"]["automod"] = 25
      with open("./json/settings/server.json", "w") as f:
        json.dump(settings, f, indent=4)


    

    if _input==None:
      with open("./json/settings/server.json", "r") as f:
        settings = json.load(f)

      settings[str(ctx.guild.id)]["moderation"] = True if settings[str(ctx.guild.id)]["moderation"] == False else False

      with open("./json/settings/server.json", "w") as f:
        json.dump(settings, f, indent=4)

      w="disabled" if settings[str(ctx.guild.id)]["moderation"] == False else "enabled"
      q=variables.emotes.cross if settings[str(ctx.guild.id)]["moderation"] == False else variables.emotes.tick

      e=discord.Embed(color=int(variables.colour.default), title="Automod", description=f"{q} Automod has been {w}.")
      e.set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)

    e=discord.Embed(color=int(variables.colour.default), title="Automod", description=f"{variables.emotes.cross} You need to provide an integer between 0-25\n```automod <args:optional>```")
    e.set_thumbnail(url=variables.info.avatar)
      
    try:
      tmp = int(_input)
    except:
      return await ctx.reply(embed=e)
      

    if tmp>25 or tmp<0:
      return await ctx.reply(embed=e)

    with open("./json/settings/server.json", "r") as f:
      settings = json.load(f)
    settings[str(ctx.guild.id)]["settings"]["automod"] = tmp
    with open("./json/settings/server.json", "w") as f:
      json.dump(settings, f, indent=4)

    e=discord.Embed(color=int(variables.colour.default), title="Automod", description=f"{variables.emotes.tick} Set the toxicity tolerance to `{tmp}`.",timestamp=datetime.datetime.utcnow())
    e.set_thumbnail(url=variables.info.avatar)
    await ctx.reply(embed=e)
    
  @commands.command(name="slowmode", aliases=["sm", "delay"])
  @commands.has_permissions(manage_guild=True)
  async def slowmode(self, ctx, secs=None, channel=None):
    
    logging.info(f"{sys._getframe().f_code.co_name} ran in {ctx.guild.name} ({ctx.guild.id})")
    aa=False
    if channel==None:
      channel = await self.bot.fetch_channel(ctx.channel.id)
      aa=True
    else:
      try:
        channel = channel.replace("<#", "").replace(">", "")
      except:
        
        e=discord.Embed(color=int(variables.colour.default), title="Slowmode", description=f"{variables.emotes.cross} Incorrect inputs.\n```slowmode <args:seconds> <args:optional:channel>```")
        e.set_thumbnail(url=variables.info.avatar)
        return await ctx.reply(embed=e)

    
    try:
      channel = int(channel) if not aa else channel
      
      channel = await self.bot.fetch_channel(ctx.channel.id) if aa else await self.bot.fetch_channel(channel)
      
      await channel.edit(slowmode_delay=secs)
      
      e=discord.Embed(color=int(variables.colour.default), title="Slowmode", description=f"{variables.emotes.tick} Slowmode in <#{channel.id}> has been set to `{secs}`s.", timestamp=datetime.datetime.utcnow())
      e.set_thumbnail(url=variables.info.avatar)
      
      return await ctx.reply(embed=e)
    except:
      e=discord.Embed(color=int(variables.colour.default), title="Slowmode", description=f"{variables.emotes.cross} Incorrect inputs.\n```slowmode <args:seconds> <args:optional:channel>```")
      e.set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)
  
  '''@commands.command(name="censor")
  def censor(self, ctx):
    with open("./json/settings/server.json", "r") as f:
      settings = json.load(f)
    if "censor" not in settings[str(ctx.guild.id)]:
      settings[str(ctx.guild.id)]["censor"] = False
    if settings[str(ctx.guild.id)]["censor"] == False:
      settings[str(ctx.guild.id)]["censor"] = True
    elif settings[str(ctx.guild.id)]["censor"] == True:
      settings[str(ctx.guild.id)]["censor"] = False
    with open("./json/settings/server.json", "w") as f:
      json.dump(settings, f, indent=4)'''

  @commands.command(name="ban", aliases=["b"])
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, user=None, *reason):
    logging.info(f"{sys._getframe().f_code.co_name} ran in {ctx.guild.name} ({ctx.guild.id})")
    if user==None:
      e=discord.Embed(color=int(variables.colour.default), title="Ban", description=f"{variables.emotes.cross} Incorrect inputs.\n```ban <user> <reason:optional>```")
      e.set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)
    
    tmp=""
    for x in reason:
      tmp+=x+" "
    reason=tmp
    reason = "The ban hammer has spoken." if reason=="" else reason

    try:
      user=user.replace("<", "").replace("@", "").replace(">", "").replace("!", "")
      user = await self.bot.fetch_user(user)
      await ctx.guild.ban(user=user, reason=reason)
      e=discord.Embed(color=int(variables.colour.default), title="Ban", description=f"{variables.emotes.tick} Banned user {user.mention}.\n```{reason}```")
      e.set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)

    except:
      e=discord.Embed(color=int(variables.colour.default), title="Ban", description=f"{variables.emotes.cross} Incorrect inputs.\n```ban <user> <reason:optional>```")
      e.set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)
  
  @commands.command(name="unban", aliases=["pardon", "unb"])
  @commands.has_permissions(ban_members=True)
  async def unban(self, ctx, userid=None):
    if userid==None:
      e=discord.Embed(color=int(variables.colour.default), title="Unban", description=f"{variables.emotes.cross} Incorrect inputs.\n```unban <userid>```")
      e.set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)
    
    try:
      userid=int(userid)
      await ctx.guild.unban(discord.Object(id=userid))
      e=discord.Embed(color=int(variables.colour.default), title="Ban", description=f"{variables.emotes.tick} Unbanned user <@!{userid}>.")
      e.set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)
    except:
      e=discord.Embed(color=int(variables.colour.default), title="Unban", description=f"{variables.emotes.cross} Incorrect inputs.\n```unban <userid>```")
      e.set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)
  
  @commands.command(name="kick", aliases=["k"])
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, user=None):
    logging.info(f"{sys._getframe().f_code.co_name} ran in {ctx.guild.name} ({ctx.guild.id})")
    if user==None:
      e=discord.Embed(color=int(variables.colour.default), title="Kick", description=f"{variables.emotes.cross} Incorrect inputs.\n```kick <user>```")
      e.set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)
    
    try:
      user=user.replace("<", "").replace("@", "").replace(">", "").replace("!", "")
      user = await self.bot.fetch_user(user)
      await ctx.guild.kick(user=user)
      e=discord.Embed(color=int(variables.colour.default), title="Kick", description=f"{variables.emotes.tick} Kicked user {user.mention}.")
      e.set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)
    except:
      e=discord.Embed(color=int(variables.colour.default), title="Kick", description=f"{variables.emotes.cross} Incorrect inputs.\n```kick <user>```")
      e.set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)

  @commands.command(name="lock", aliases=["l", "unlock"])
  @commands.has_permissions(manage_guild=True)
  async def lock(self, ctx, where=None):
    logging.info(f"{sys._getframe().f_code.co_name} ran in {ctx.guild.name} ({ctx.guild.id})")
    if where == None:
      overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
      if overwrite.send_messages == False:
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        e=discord.Embed(color=int(variables.colour.default), title="Channel unlocked.", description=f"This channel has been unlocked by an administrator.")
        e.set_thumbnail(url=variables.info.avatar)
        return await ctx.reply(embed=e)

      await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
      e=discord.Embed(color=int(variables.colour.default), title="Channel locked.", description=f"This channel has been locked by an administrator.")
      e.set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)
    
    where=where.replace("<", "").replace("#", "").replace(">", "")
    try:
      where = ctx.guild.get_channel(int(where))

      overwrite = where.overwrites_for(ctx.guild.default_role)
      if overwrite.send_messages == False:
        await where.set_permissions(ctx.guild.default_role, send_messages=True)
        e=discord.Embed(color=int(variables.colour.default), title="Channel unlocked.", description=f"This channel has been unlocked by an administrator.")
        e.set_thumbnail(url=variables.info.avatar)
        await where.send(embed=e)

        e=discord.Embed(color=int(variables.colour.default), title="Lock", description=f"{variables.emotes.tick} {where.mention} has been unlocked.")
        e.set_thumbnail(url=variables.info.avatar)
        return await ctx.reply(embed=e)

 



      await where.set_permissions(ctx.guild.default_role, send_messages=False)
      e=discord.Embed(color=int(variables.colour.default), title="Channel locked.", description=f"This channel has been locked by an administrator.")
      e.set_thumbnail(url=variables.info.avatar)
      await where.send(embed=e)
 
      e=discord.Embed(color=int(variables.colour.default), title="Lock", description=f"{variables.emotes.tick} {where.mention} has been locked.")
      e.set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)
    except:
      e=discord.Embed(color=int(variables.colour.default), title="Lock", description=f"{variables.emotes.cross} That channel does not exist\n```lock <channel:optional>```")
      e.set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)


    
        


    

    




      



    



  

def setup(bot):
    bot.add_cog(moderation(bot))