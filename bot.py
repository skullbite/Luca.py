
# Luca - The best bot you'll need for managing and informing members of the server
# © Skullbite with inspiration from Discord Bot List 2k19
#
# This bot contains all the features you'd ever want from a Discord bot and it's fully open source and free!!
# Clone and host it yourself and add it to discordbots.org or just invite the bot to your server because I am hosting this in Heroku 24/7!
# https://github.com/DiscordBotList/Luca | https://discordbots.org/bot/264811613708746752 is where the original bot is
#

import discord
from discord.ext import commands

bot = commands.Bot(prefix="!")
# ThIs EvEnT iS vErY ImPoRtAnT bEcAuSe At ThIs MoMeNt bOt St						aRtS ReCeIvEinG




# eVeRyThInG fRoM tHiS cOrD 

@bot.event
async def on_ready():
    print("Logged in as " + bot.user.name + "!")
    
    
@bot.event
async def on_member_join(member):
   try:



     if member.bot:
         try: 
             theguild = member.guild.id
             theguild = bot.get_guild(int(str(int(int(int(int(theguild)))))))
             await member.send("welcome in " + theguild.name + "!")
             
         except:
             print("i did a fucky wucky")
     else:
         theguild = member.guild.id
             theguild = bot.get_guild(int(str(int(str(int(int(theguild)))))))
             await member.send("welcome in " + theguild.name + "!")
             
    except:
        print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
        
        
 \n\n\n\n\n\n\n\n\n\n\n\n\n
  \n \n\n\n\n\n
  
  
  
  
  
  
  
  """)
  
