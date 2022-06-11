import inspect
import sys
import logging
import variables
import discord
from discord.ext import commands
import json

from os import getcwd
import requests
class api(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.Cog.listener()
  async def on_ready(self):
    print(f'{getcwd()} => cogs/api.py loaded')


  @commands.command(name="dog")
  async def dog(self, ctx, breed=None):
    logging.info(f"{sys._getframe().f_code.co_name} ran in {ctx.guild.name} ({ctx.guild.id})")
    
    if breed==None:
      e=discord.Embed(color=int(variables.colour.default))
      a=json.loads(requests.get("https://dog.ceo/api/breeds/image/random").text)["message"]

      e.set_image(url=a)
      return await ctx.reply(embed=e)
    

    a=json.loads(requests.get(f"https://dog.ceo/api/breed/{breed}/images/random").text)

    if a["status"] == "error":
      e=discord.Embed(color=int(variables.colour.default), title="Dog", description=f"{variables.emotes.cross} That dog breed does not exist.\n```dog <args:optional>```")
      e.set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)
    
    e=discord.Embed(color=int(variables.colour.default))
    e.set_image(url=a["message"])
    return await ctx.reply(embed=e)

  @commands.command(name="number", aliases=["num"])
  async def number(self, ctx, num=None):
    logging.info(f"{sys._getframe().f_code.co_name} ran in {ctx.guild.name} ({ctx.guild.id})")

    if num==None:
      numFact = requests.get("http://numbersapi.com/random").text
      
      e=discord.Embed(color=int(variables.colour.default), title=f"Number", description=f"{numFact}")
      e.set_thumbnail(url=variables.info.avatar)

      return await ctx.reply(embed=e)
    
    if not num.isdigit():
      e=discord.Embed(color=int(variables.colour.default), title="Number", description=f"{variables.emotes.cross} A valid number must be provided.\n```number <args:optional>```")
      e.set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)
    
    numFact = requests.get(f"http://numbersapi.com/{num}").text

    if numFact.endswith("mail!)."):
      numFact = f"{num} is an unremarkable number."

    e=discord.Embed(color=int(variables.colour.default), title=f"Number", description=f"{numFact}")
    e.set_thumbnail(url=variables.info.avatar)

    return await ctx.reply(embed=e)









  
def setup(bot):
    bot.add_cog(api(bot))