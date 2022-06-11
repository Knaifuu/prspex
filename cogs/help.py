from pathlib import Path
import sys
import inspect
import logging
import variables

import discord
from discord.ext import commands
from os import getcwd

class help(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.Cog.listener()
  async def on_ready(self):
    print(f'{getcwd()} => cogs/help.py loaded')


  @commands.command(name="help")
  async def help(self, ctx, what=None):
    logging.info(f"{sys._getframe().f_code.co_name} ran in {ctx.guild.name} ({ctx.guild.id})")
    cmds={
      "prefix":f"{variables.emotes.perms}Changes the prefix of the bot.\n```prefix <args>```",
      "automod":f"{variables.emotes.perms}Toggles auto moderation settings, or changes the toxicity tolerance value.\n```automod <args:optional>```\n```automod\nautomod 15```",
      "ping":f"View the current ping of the bot in milliseconds.\n```ping```",
      "avatar":f"Displays your avatar, or a specified user's.\n```avatar <args:optional>```\n```avatar\navatar @steve\navatar 942133195065929748```",
      "help":f"View all commands, or information about a specific one.\n```help <args:optional>```\n```help\nhelp colour```",
      "invite":f"Get a link to invite the bot to your server.\n```invite```",
      "slowmode":f"{variables.emotes.perms}Change the slowmode settings for a channel, 0 to disable.\n```slowmode <args:seconds> <args:optional:channel>```\n```slowmode 60\nslowmode 300 #general```",
      "coinflip":f"Flips a coin that can land on either heads or tails.\n```coinflip```",
      "8ball":f"Ask the magic 8ball a question.\n```8ball <args:optional>```\n```8ball\n8ball should I go out?```",
      "dice":f"Roll a dice, defaults to 6 sides.\n```dice <args:optional:int>```\n```dice\ndice 20```",
      "reverse":f"Reverses anything you say.\n```reverse <args>```\n```reverse this text will be reversed```",
      "gayrate":f"Tells you how gay someone is. This is 100% accurate.\n```gayrate <args:optional>```\n```gayrate @steve```",
      "colour":f"Get information about a colour from a hex value.\n```colour <args>```\n```colour 0FA3FB\ncolour db1abd```",
      "ascii":f"Displays your desired text in an ASCII format.\n```ascii <args>```\n```ascii blocks```",
      "botstats":f"Displays the current statistics of the bot.\n```botstats```",
      "serverinfo":f"Displays information about the server.\n```serverinfo```",
      "userinfo":f"Displays information about a user.\n```userinfo <args:optional>```\n```userinfo\nuserinfo @steve\nuserinfo 942133195065929748```",
      "dog":f"Displays a random dog image, or a specific breed.\n```dog <args:optional>```\n```dog\ndog spaniel```",
      "number":f"Displays a fact about a number.\n```number <args:optional>```\n```number\nnumber 10```",
      "ban":f"{variables.emotes.perms}Bans a user from the server.\n```ban <user> <reason:optional>```\n```ban @steve\nban 942133195065929748\nban @steve being mean\nban 942133195065929748 being mean```",
      "unban":f"{variables.emotes.perms}Unbans a user from the server.\n```unban <userid>```\n```unban 942133195065929748```",
      "kick":f"{variables.emotes.perms}Kicks a user from the server.\n```kick <user>```\n```kick @steve\nkick 942133195065929748```",
      "lock":f"{variables.emotes.perms}Toggles permissions to stop users from messaging in a channel.\n```lock <channel:optional>```\n```lock\nlock #general```",
      "changelog":f"View the changelog for this version of the bot.\n```changelog```",
      "embed":f"{variables.emotes.perms}Created an embed in the current channel, then deleted your embed command message.\n```embed <title> | <content> | <thumbnail:optional> | <colour:hex:optional>```\n```embed Rules | Have fun\n\nembed Beans | Have some beans | https://beanhub.org/assets/img/Homemade-Heinz-Baked-Beans_0-SQ.jpg\n\nembed I like the colour green | It's cool | 00ff00\n\nembed Red is cool too | very cool | https://2.imimg.com/data2/LP/OV/MY-1666467/blood-red-excusive-colour-tiles-500x500.jpg | FF0000```"

    }
    if what==None:
      e=discord.Embed(color=int(variables.colour.default), title="Help", description=f"Use `help <args>` to get info about a specific command.\n{variables.emotes.perms} requires moderative or administrative permissions.")
      e.set_thumbnail(url=variables.info.avatar)
      e.add_field(name="Settings", value=f"{variables.emotes.perms}prefix", inline=True)
      e.add_field(name="Moderation", value=f"{variables.emotes.perms}automod\n{variables.emotes.perms}slowmode\n{variables.emotes.perms}ban\n{variables.emotes.perms}unban\n{variables.emotes.perms}kick\n{variables.emotes.perms}lock", inline=True)
      e.add_field(name="Utility", value=f"{variables.emotes.perms}embed\navatar\nhelp\ninvite\nping\ncolour\nascii\nbotstats\nserverinfo\nuserinfo", inline=True)
      e.add_field(name="Fun", value="coinflip\n8ball\ndice\nreverse\ngayrate", inline=True)
      e.add_field(name="API", value="dog\nnumber", inline=True)
      e.add_field(name="Other", value=f"changelog", inline=True)
      
      return await ctx.reply(embed=e)
    else:
      what=what.lower()
      if what not in cmds:
        e=discord.Embed(color=int(variables.colour.default), title="Help", description=f"{variables.emotes.cross} This command does not exist!")
        e.set_thumbnail(url=variables.info.avatar)
        return await ctx.reply(embed=e)
      e=discord.Embed(color=int(variables.colour.default), title=f"Help - {what}", description=f"{cmds[what]}")
      e.set_thumbnail(url=variables.info.avatar)
      await ctx.reply(embed=e)
  
  
  @commands.command(name="changelog", aliases=["ver", "version", "updates"])
  async def changelog(self, ctx):
    logging.info(f"{sys._getframe().f_code.co_name} ran in {ctx.guild.name} ({ctx.guild.id})")
    txt = Path('./bot/update.txt').read_text()
    e=discord.Embed(color=int(variables.colour.default), title="Changelog", description=f"```{txt}```")
    e.set_thumbnail(url=variables.info.avatar)
    return await ctx.reply(embed=e)
        
    

    








def setup(bot):
    bot.add_cog(help(bot))