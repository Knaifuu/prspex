# prspex
# Authors: Knaifuu, Zumoarikunori
# Date: 12 Feb 2022

from os import environ,listdir,getenv


import logging

import datetime
from keep_alive import keep_alive
import variables
import discord
from discord.ext import commands
import json
import asyncio
from random import choice
def get_prefix(client, message):
    with open("./json/settings/server.json", 'r') as f:
        prefix = json.load(f)

    return prefix[str(message.guild.id)]["settings"]["prefix"]
bot = commands.Bot(command_prefix=get_prefix, help_command=None, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{choice(variables.eightball.statuses)}"),status=discord.Status.dnd, case_insensitive=True, intents=discord.Intents().all())

class tm:
  _time = datetime.datetime.now()

@bot.event
async def on_guild_join(guild):
  with open("./json/settings/server.json", "r") as f:
    serverjson = json.load(f)

  serverjson[str(guild.id)] = {
    "settings": {
      "prefix": "px "
    }
  }

  with open("./json/settings/server.json", "w") as f:
    json.dump(serverjson, f, indent=4)
  f.close()

@bot.event
async def on_guild_leave(guild):
  with open("./json/settings/server.json", "r") as f:
    serverjson = json.load(f)
  serverjson.pop(guild.id)
  with open("./json/settings/server.json", "w") as f:
    json.dump(serverjson, f, indent=4)
  f.close()


for x in listdir('./cogs'):
	if x.endswith('.py'):
		bot.load_extension(f'cogs.{x[:-3]}')



@bot.event
async def on_ready():
  print(f"logged in as {bot.user}")
 

  while True:
    await asyncio.sleep(120)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{choice(variables.eightball.statuses)}", status=discord.Status.dnd))
    


level = logging.INFO
fmt = "[%(levelname)s] %(asctime)s - %(message)s"
logging.basicConfig(level=level, format=fmt)

keep_alive()
bot.run(getenv('TOKEN'))