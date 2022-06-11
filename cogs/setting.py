import variables
import discord


from discord.ext import commands
import json
from os import getcwd
import datetime
import logging
import sys
import inspect

class setting(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.Cog.listener()
  async def on_ready(self):
    print(f'{getcwd()} => cogs/setting.py loaded')



  @commands.command(name="prefix")
  @commands.has_permissions(manage_guild=True)
  async def prefix(self, ctx, inputa=None):
    logging.info(f"{sys._getframe().f_code.co_name} ran in {ctx.guild.name} ({ctx.guild.id})")
    

    if inputa==None:
      e=discord.Embed(color=int(variables.colour.default), title="Prefix", description=f"{variables.emotes.cross} You need to provide a prefix.\n```prefix <args>```")
      e.set_thumbnail(url=variables.info.avatar)
      await ctx.reply(embed=e)
    else:

      inputa=inputa.replace("\"", "")
      if inputa==None:
        e=discord.Embed(color=int(variables.colour.default), title="Prefix", description=f"{variables.emotes.cross} You cannot use the `\"` symbol.\n```prefix <args>```")
        e.set_thumbnail(url=variables.info.avatar)
        await ctx.reply(embed=e)
      

      with open('./json/settings/server.json', 'r') as f:
        prefixes = json.load(f)
      inputa = inputa if inputa!="reset" else "px "
      prefixes[str(ctx.guild.id)]["settings"]["prefix"] = inputa

      with open('./json/settings/server.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
      e=discord.Embed(color=int(variables.colour.default), title="Prefix", description=f"{variables.emotes.tick} Prefix has been changed to `{inputa}`.",timestamp=datetime.datetime.utcnow())
      e.set_thumbnail(url=variables.info.avatar)
      await ctx.reply(embed=e)
      f.close()



def setup(bot):
    bot.add_cog(setting(bot))