import discord
class version:
  version = "b1.1.3"

class colour:
  default = "3092790"

class emotes:
  cross = "<:cross:873258921232568361>"
  tick = "<:tick:873258921190641706>"
  perms = "<:perms:942184651580129361>"
  heads = "<:heads:942487120218570862>"
  tails = "<:tails:942487120151453786>"
  dice = "<:dice:942494975864754186>"
  
class info:
  avatar = "https://cdn.discordapp.com/avatars/942133195065929748/f21fd46e2dc7ae1df661fd391a441c0a.webp?size=1024"

class image:
  working = "https://cdn.discordapp.com/attachments/849611723026726915/942353362165313626/ticket-pulse.gif"

class eightball:
  responses=[ "It is certain.",
              "It is decidedly so.",
              "Without a doubt.",
              "Yes definitely.",
              "You may rely on it.",
              "As I see it, yes.",
              "Most likely.",
              "Outlook good.",
              "Yes.",
              "Signs point to yes.",
              "Reply hazy, try again.",
              "Ask again later.",
              "Better not tell you now.",
              "Cannot predict now.",
              "Concentrate and ask again.",
              "Don't count on it. ",
              "My reply is no.",
              "My sources say no.",
              "Outlook not so good.",
              "Very doubtful."]
            
  statuses=["you.",
            "your mother.",
            "your grandmother.",
            "your pet.",
            "you whilst you sleep.",
            "the burning orphanage.",
            "the homeless.",
            "childline.",
            "teletubbies.",
            "paint dry.",
            "Jeremy Clarkson.",
            "Lucifer.",
            "the angels.",
            "unmentionables.",
            "@prspex"]


def emb(title, content, image=None, colour=None):
  return discord.Embed(title=title, description=content, colour=colour).set_thumbnail(url=image)




  