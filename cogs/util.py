
import variables
from variables import emb
import discord
from discord.ext import commands
import json
import logging
import sys
import inspect

from os import getcwd

import requests
import datetime

def is_url_image(image_url):
   image_formats = ("image/png", "image/jpeg", "image/jpg", "image/gif")
   try:
    r = requests.head(image_url)
   except:
     return False
   if r.headers["content-type"] in image_formats:
      return True
   return False
from main import tm

class util(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.Cog.listener()
  async def on_ready(self):
    print(f'{getcwd()} => cogs/util.py loaded')


  @commands.command(name="ping")
  async def ping(self, ctx, domain=None):
      logging.info(f"{sys._getframe().f_code.co_name} ran in {ctx.guild.name} ({ctx.guild.id})")
      e=discord.Embed(color=int(variables.colour.default), title="Ping", description=f"My ping is:\n```~{round((self.bot.latency*1000),2)}ms```",timestamp=datetime.datetime.utcnow())
      e.set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)
    





  @commands.command(name="avatar", aliases=["pfp", "pic", "picture", "av"])
  async def avatar(self, ctx, user=None):
    logging.info(f"{sys._getframe().f_code.co_name} ran in {ctx.guild.name} ({ctx.guild.id})")
    if not user:

      e=discord.Embed(color=int(variables.colour.default), title=f"{ctx.message.author.name}#{ctx.message.author.discriminator}")
      e.set_image(url=ctx.message.author.avatar_url)

      await ctx.reply(embed=e)
    else:
      user=user.replace("<", "").replace("!", "").replace("@", "").replace(">", "")

      try:
        int(user)
        user = await self.bot.fetch_user(user)
        e=discord.Embed(color=int(variables.colour.default), title=f"{user.name}#{user.discriminator}")
        e.set_image(url=user.avatar_url)

        await ctx.reply(embed=e)
      except:
        e=discord.Embed(color=int(variables.colour.default), title=f"Avatar", description=f"{variables.emotes.cross} This is not a valid user ID.\n```avatar <args:optional>```")
        e.set_thumbnail(url=variables.info.avatar)

        await ctx.reply(embed=e)

  @commands.command(name="invite")
  async def invite(self, ctx):
    logging.info(f"{sys._getframe().f_code.co_name} ran in {ctx.guild.name} ({ctx.guild.id})")
    e=discord.Embed(color=int(variables.colour.default), title=f"Invite me to your server", description="[Click here](https://discord.com/oauth2/authorize?client_id=942133195065929748&scope=bot&permissions=8).")
    e.set_thumbnail(url=variables.info.avatar)
    await ctx.reply(embed=e)

  @commands.command(name="colour", aliases=["color", "col"])
  async def colour(self, ctx, value=None):
    logging.info(f"{sys._getframe().f_code.co_name} ran in {ctx.guild.name} ({ctx.guild.id})")
    try:
      a=value
      
      if len(value)!=6:
        e=discord.Embed(color=int(variables.colour.default), title=f"Colour", description=f"{variables.emotes.cross} You must provide a valid hex value.\n```colour <args>```")
        e.set_thumbnail(url=variables.info.avatar)
        
        return await ctx.reply(embed=e)
      value = int(value, 16) 
    except:
      e=discord.Embed(color=int(variables.colour.default), title=f"Colour", description=f"{variables.emotes.cross} You must provide a valid hex value.\n```colour <args>```")
      e.set_thumbnail(url=variables.info.avatar)
      
      return await ctx.reply(embed=e)

    if value > 16777215:
      e=discord.Embed(color=int(variables.colour.default), title=f"Colour", description=f"{variables.emotes.cross} You must provide a valid hex value.\n```colour <args>```")
      e.set_thumbnail(url=variables.info.avatar)
      
      return await ctx.reply(embed=e)
    
    col = json.loads(requests.get(f"https://www.thecolorapi.com/id?hex={a}").text)
    img = f"https://htmlcolors.com/color-image/{a}.png"

    e=discord.Embed(color=value, title=col["name"]["value"])

    e.add_field(name="Red", value=col["rgb"]["r"])
    e.add_field(name="Green", value=col["rgb"]["g"])
    e.add_field(name="Blue", value=col["rgb"]["b"])

    e.add_field(name="Hex", value=col["hex"]["clean"], inline=True)
    e.add_field(name="Int", value=value, inline=True)
    e.add_field(name="Examples", value=f"[Click here](https://www.google.com/search?q={col['name']['value'].replace(' ', '+')}&tbm=isch)", inline=True)


    e.set_thumbnail(url=img)
    await ctx.reply(embed=e)
  
  @commands.command(name="ascii")
  async def _ascii(self, ctx, *args):
    logging.info(f"{sys._getframe().f_code.co_name} ran in {ctx.guild.name} ({ctx.guild.id})")
    emb=discord.Embed(color=int(variables.colour.default), title="ASCII", description=f"{variables.emotes.cross} This command is currently disabled.").set_thumbnail(url=variables.info.avatar)
    return await ctx.reply(embed=emb)
    if not args:
      e=discord.Embed(color=int(variables.colour.default), title=f"ASCII", description=f"{variables.emotes.cross} You need to provide a valid input.")
      e.set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)

    s=""
    for x in args:
      s+=(x+" ")


    

    text = requests.get(f"https://artii.herokuapp.com/make?text={s.replace(' ', '+')}").text
    if len(text.split("\n")[0]) > 59:
      e=discord.Embed(color=int(variables.colour.default), title=f"ASCII", description=f"{variables.emotes.cross} The text you provided was too long.\n```ascii <args>```")
      e.set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)
    e=discord.Embed(color=int(variables.colour.default), title=f"ASCII", description=f"*Only works on PC devices* | *Only works within code blocks*```{text}```")
    return await ctx.reply(embed=e)

  @commands.command(name="botstats", aliases=["bot", "uptime"])
  async def botstats(self, ctx):
    logging.info(f"{sys._getframe().f_code.co_name} ran in {ctx.guild.name} ({ctx.guild.id})")
    e=discord.Embed(color=int(variables.colour.default), title=f"prspex",timestamp=datetime.datetime.utcnow())
    e.set_thumbnail(url=variables.info.avatar)

    time_since = round(round(datetime.datetime.now().timestamp())-round(tm._time.timestamp()))
    time_ending = "seconds"
    
    if time_since > 60:
      time_since=round(time_since/60,1)
      time_ending = "minutes"
      if time_since > 60:
        time_since=round(time_since/60,1)
        time_ending = "hours"
        if time_since > 24:
          time_since = round(time_since/24,1)
          time_ending = "days"

    e.add_field(name="Uptime", value=f"{time_since} {time_ending}")
    e.add_field(name="Total servers", value=f"{str(len(self.bot.guilds))}")
    e.add_field(name="Release", value=f"{variables.version.version}")

    await ctx.reply(embed=e)

  @commands.command(name="serverinfo", aliases=["guildinfo", "si", "gi", "serverstats", "ss"])
  async def server_info(self, ctx):
    logging.info(f"{sys._getframe().f_code.co_name} ran in {ctx.guild.name} ({ctx.guild.id})")
    embed = discord.Embed(title="Server information",
      colour=int(variables.colour.default),
      timestamp=datetime.datetime.utcnow())
    
    embed.set_thumbnail(url=ctx.guild.icon_url)

    statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
    len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
    len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
    len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

    fields = [("ID", ctx.guild.id, True),
    ("Owner", ctx.guild.owner, True),
    ("Region", ctx.guild.region, True),
    ("Created at", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
    ("Members", len(ctx.guild.members), True),
    ("Humans", len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
    ("Bots", len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
    ("Banned members", len(await ctx.guild.bans()), True),
    ("Statuses", f"<:online:942730002938597426> {statuses[0]} <:idle:942730477138239498> {statuses[1]} <:dnd:942730940680130590> {statuses[2]} <:offline:942731266447528026> {statuses[3]}", True),
    ("Text channels", len(ctx.guild.text_channels), True),
    ("Voice channels", len(ctx.guild.voice_channels), True),
    ("Categories", len(ctx.guild.categories), True),
    ("Roles", len(ctx.guild.roles), True),
    ("Invites", len(await ctx.guild.invites()), True),
    ("\u200b", "\u200b", True)]

    for name, value, inline in fields:
      embed.add_field(name=name, value=value, inline=inline)

    await ctx.reply(embed=embed)

  @commands.command(name="userinfo", aliases=["memberinfo", "ui", "mi"])
  async def user_info(self, ctx, target=None):
    logging.info(f"{sys._getframe().f_code.co_name} ran in {ctx.guild.name} ({ctx.guild.id})")

    a=True if target!=None else False

    target = ctx.author if not target else target.replace("<", "").replace("!", "").replace("@", "").replace(">", "")

   
      
    
    try:
      embed = discord.Embed(title="User information",
      colour=int(variables.colour.default),
      timestamp=datetime.datetime.utcnow())
      target = ctx.guild.get_member(int(target)) if a else target
      fields = [("Name", target.name+"#"+str(target.discriminator), True),
      ("ID", target.id, True),
      ("Bot", target.bot, True),
      ("Top role", target.top_role.mention, True),
      ("Status", str(target.status).title(), True),
      ("Activity", f"{'('+str(target.activity.type).split('.')[-1].title()+')' if target.activity else 'N/A'} {target.activity.name if target.activity else ''}", True),
      ("Created at", target.created_at.strftime("%d/%m/%Y %H:%M:%S"), True),
      ("Joined at", target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), True),
      ("Boosted", bool(target.premium_since), True)]
      embed.set_thumbnail(url=target.avatar_url)
      for name, value, inline in fields:
        embed.add_field(name=name, value=value, inline=inline)
      return await ctx.reply(embed=embed)
    except:
      e=discord.Embed(color=int(variables.colour.default), title=f"User information", description=f"{variables.emotes.cross} You need to provide a valid user.\n```userinfo <args:optional>```")
      e.set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)


  @commands.command(name="embed", aliases=["emb", "e"])
  async def embed(self, ctx, *args):
    logging.info(f"{sys._getframe().f_code.co_name} ran in {ctx.guild.name} ({ctx.guild.id})")
    s = ""
    for x in args:
      s+=x+" "
    args=s.split("|")

    e=0
    for x in args:
      e+=1
    hascolour3=False
    b=3092790

    if e>=3:
      try:
        b = int(args[2], 16)
        b = 3092790 if b> 16777215 else b
        hascolour3=True
      except:
        pass
      try:
        b = int(args[3], 16)
        b = 3092790 if b> 16777215 else b
      except:
        pass


     

    if e < 2 or e > 4:
      e=discord.Embed(color=int(variables.colour.default), title=f"Embed", description=f"{variables.emotes.cross} Not enough inputs.\nUse pipe symbols to separate fields.```embed <title> | <content> | <thumbnail:optional> | <colour:hex:optional>```")
      e.set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)
    

    try:
      await ctx.send(embed=emb(args[0], args[1], "https://cdn.discordapp.com/attachments/849611723026726915/944709820794163290/unknown.png" if(e<4 and hascolour3) or e==2 else args[2], b))
      return await ctx.message.delete()
    except:
      e=discord.Embed(color=int(variables.colour.default), title=f"Embed", description=f"{variables.emotes.cross} Invalid inputs.\nUse pipe symbols to separate fields.```embed <title> | <content> | <thumbnail:optional> | <colour:hex:optional>```")
      e.set_thumbnail(url=variables.info.avatar)
      return await ctx.reply(embed=e)




    
    


  

def setup(bot):
    bot.add_cog(util(bot))