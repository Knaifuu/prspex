from googleapiclient import discovery
import variables
import logging
import discord
from discord.ext import commands
import json
import asyncio
import sys
import inspect


from os import getcwd
apikey = "AIzaSyDXPPCip9z7jxD2cGQR-vPsxFKRjiypq5A"


class listeners(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.Cog.listener()
  async def on_ready(self):
    print(f'{getcwd()} => cogs/listeners.py loaded')

  

  @commands.Cog.listener()
  async def on_message(self, message):

    if message.content.split(" ")[0] == "<@942133195065929748>" or message.content.split(" ")[0] == "<@!942133195065929748>":
      with open("./json/settings/server.json", "r") as f:
        settings=json.load(f)
      prf = settings[str(message.guild.id)]["settings"]["prefix"]
      f.close()

      e=discord.Embed(color=int(variables.colour.default), title="prspex", description=f"My prefix here is `{prf}`.\n```{prf}help```")
      e.set_thumbnail(url=variables.info.avatar)
      await message.reply(embed=e)
      


    if message.author.bot or "the ass" in message.content.lower() or "fucking" in message.content.lower() or message.content == "":
      return
    with open("./json/settings/server.json", "r") as f:
      settings = json.load(f)
    if "moderation" not in settings[str(message.guild.id)]:
      settings[str(message.guild.id)]["moderation"] = False
      with open("./json/settings/server.json", "w") as f:
        json.dump(settings, f, indent=4)
    
    if settings[str(message.guild.id)]["moderation"] == True:
      ww = settings[str(message.guild.id)]["settings"]["automod"]

      client = discovery.build(
              "commentanalyzer",
              "v1alpha1",
              developerKey=apikey,
              discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
              static_discovery=False,
        )
      
      analyze_request = {
              'comment': { 'text': message.content },
              'requestedAttributes': {'TOXICITY': {}} 
        }
      response = client.comments().analyze(body=analyze_request).execute()
      if round(response["attributeScores"]["TOXICITY"]["summaryScore"]["value"]*100,None) >=(ww+60):
        e=discord.Embed(color=int(variables.colour.default), title="Automod", description=f"{variables.emotes.perms} Deleted toxic message from {message.author.mention}.")
        e.set_thumbnail(url=variables.info.avatar)

        b = await message.reply(embed=e)
        await message.delete()
        await asyncio.sleep(2)
        await b.delete()

  @commands.Cog.listener()
  async def on_message_edit(self, ctx, message):
    if message.author.bot or "the ass" in message.content.lower() or "fucking" in message.content.lower() or message.content == "":
      return
    with open("./json/settings/server.json", "r") as f:
      settings = json.load(f)
    if "moderation" not in settings[str(message.guild.id)]:
      settings[str(message.guild.id)]["moderation"] = False
      with open("./json/settings/server.json", "w") as f:
        json.dump(settings, f, indent=4)
    
    if settings[str(message.guild.id)]["moderation"] == True:
      ww = settings[str(message.guild.id)]["settings"]["automod"]

      client = discovery.build(
              "commentanalyzer",
              "v1alpha1",
              developerKey=apikey,
              discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
              static_discovery=False,
        )
      
      analyze_request = {
              'comment': { 'text': message.content },
              'requestedAttributes': {'TOXICITY': {}} 
        }
      response = client.comments().analyze(body=analyze_request).execute()
      
      if round(response["attributeScores"]["TOXICITY"]["summaryScore"]["value"]*100,None) >=(ww+60):
        
        e=discord.Embed(color=int(variables.colour.default), title="Automod", description=f"{variables.emotes.perms} Deleted toxic message from {message.author.mention}.")
        e.set_thumbnail(url=variables.info.avatar)

        b = await message.reply(embed=e)
        await message.delete()
        await asyncio.sleep(2)
        await b.delete()
  
  @commands.Cog.listener()
  async def on_command_error(self, ctx, err):
    if isinstance(err, commands.errors.CommandNotFound):
      return
    if isinstance(err, commands.errors.MissingPermissions):
      e=discord.Embed(color=int(variables.colour.default), title="Missing permissions", description=f"{variables.emotes.cross} You are missing the required permissions to run this command.\nUse `help` for a list of commands you may use.")
      e.set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)
    raise err
    









def setup(bot):
    bot.add_cog(listeners(bot))