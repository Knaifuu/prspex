import inspect

import logging
import variables
import discord
from discord.ext import commands
from os import getcwd
from random import randint, choice
import sys


class fun(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.Cog.listener()
  async def on_ready(self):
    print(f'{getcwd()} => cogs/fun.py loaded')

  @commands.command(name="hungry")
  async def hungry(self, ctx):
    e=discord.Embed(color=int(variables.colour.default), title="Food Delivery", description=f"Have chicken nuggets!").set_thumbnail(url="https://images-ext-1.discordapp.net/external/0SpdLndVWZgsWF30cfmBUZ7vD9WsSgjUYxefqT_UqL8/https/www.pngfind.com/pngs/m/149-1499834_chicken-nuggets-png-heart-shaped-chicken-nugget-transparent.png")
    return await ctx.reply(embed=e)








  @commands.command(name="coinflip", aliases=["flip", "coin", "heads", "tails", "cf"])
  async def coinflip(self, ctx):
    logging.info(f"{sys._getframe().f_code.co_name} ran in {ctx.guild.name} ({ctx.guild.id})")
    a = randint(1, 2)
    ht = "tails" if a==1 else "heads"
    w = variables.emotes.tails if a==1 else variables.emotes.heads 

    e=discord.Embed(color=int(variables.colour.default), title="Coinflip", description=f"{w} The coin landed on {ht}.").set_thumbnail(url=variables.info.avatar)
      
    await ctx.reply(embed=e)

  @commands.command(name="8ball", aliases=["eightball", "8b"])
  async def eightball(self, ctx, *z):
    logging.info(f"{sys._getframe().f_code.co_name} ran in {ctx.guild.name} ({ctx.guild.id})")
    e=discord.Embed(color=int(variables.colour.default), title="8ball", description=f"{choice(variables.eightball.responses)}").set_thumbnail(url=variables.info.avatar)

    await ctx.reply(embed=e)

  @commands.command(name="dice", aliases=["die"])
  async def dice(self, ctx, amt=None):
    logging.info(f"{sys._getframe().f_code.co_name} ran in {ctx.guild.name} ({ctx.guild.id})")
    amt = 6 if amt == None else amt

    try:
      amt = int(amt)
      amt=randint(1,amt)
      e=discord.Embed(color=int(variables.colour.default), title="Dice", description=f"{variables.emotes.dice} The dice rolled {amt}.").set_thumbnail(url=variables.info.avatar)

      await ctx.reply(embed=e)
    except:
      e=discord.Embed(color=int(variables.colour.default), title="Dice", description=f"{variables.emotes.cross} Incorrect inputs.\n```dice <args:optional:int>```").set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)
    
  @commands.command(name="reverse", aliases=["backwards", "reversetext", "rt"])
  async def reverse(self, ctx, *args):
    logging.info(f"{sys._getframe().f_code.co_name} ran in {ctx.guild.name} ({ctx.guild.id})")
    a=""
    if not args:
      e=discord.Embed(color=int(variables.colour.default), title="Reverse", description=f"{variables.emotes.cross} Incorrect inputs.\n```reverse <args>```").set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)
    for x in args:
      a+=(x+" ")
    e=discord.Embed(color=int(variables.colour.default), title=" ", description=f"```{a[::-1][1:]}```")
    return await ctx.reply(embed=e)
  





  @commands.command(name="gayrate", aliases=["howgay", "gayr"])
  async def gayrate(self, ctx, user=None):
    logging.info(f"gayrate ran in {ctx.guild.name} ({ctx.guild.id})")
    a = randint(0,100)
    
    user=user.replace("<", "").replace("!", "").replace("@", "").replace(">", "") if user!=None else None
    user = ctx.message.author.id if user==None else user


    try:
      int(user)
      user = await self.bot.fetch_user(user)
      e=discord.Embed(color=int(variables.colour.default), title=f"Gayrate", description=f"<@!{user.id}> is {a}% gay.")
      e.set_thumbnail(url="https://cdn.discordapp.com/attachments/849611723026726915/942506467200737310/NicePng_rainbow-png-transparent_688483.png")

      await ctx.reply(embed=e)
    except:
      e=discord.Embed(color=int(variables.colour.default), title=f"Gayrate", description=f"{variables.emotes.cross} This is not a valid user ID.\n```gayrate <args:optional>```")
      e.set_thumbnail(url=variables.info.avatar)

      await ctx.reply(embed=e)




      


  
    






def setup(bot):
    bot.add_cog(fun(bot))