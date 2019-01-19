

# Luca - The best bot you'll need for managing and informing members of the server
# © Skullbite with inspiration from Discord Bot List 2k19
#
# This bot contains all the features you'd ever want from a Discord bot and it's fully open source and free!!
# Clone and host it yourself and add it to discordbots.org or just invite the bot to your server because I am hosting this in Heroku 24/7!
# https://github.com/DiscordBotList/Luca | https://discordbots.org/bot/264811613708746752 is where the original bot is
#

import discord
from discord.ext import commands

import random

import requests as requests

bot = commands.Bot(command_prefix="!")
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
        print("""\n\n\n\n\n\n\n\n\n\no\n\n\n\n\n\n\n\n\nh\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nn\n\n\n\n\n\no\n\n\n\n
        
        
 \n\n\n\n\n\n\n\n\n\n\n\n\n
  \n \n\n\n\n\n
  
  
  
  
  
  
  
  """)
  
@bot.event
async def on_message(message):
    if message.content == 'ping' or message.content == '!ping':
        return await message.channel.send(message.author.mention + ", Pong!")
    
@bot.event
async def on_message(message):
    if message.content == '@everyone':
        return await message.channel.send(message.author.mention + ", @everyone ping ping @everyone")
    
@bot.event
async def on_message(message):
    cat = requests.get('https://aws.random.cat/meow')
    if message.content == '!cat':
        cat = cat.json()
        return await message.channel.send(message.author.mention + ", " + cat["file"]) 
    
@bot.event
async def on_message(message):
    if message.content == 'sa':
        return await message.channel.send(message.author.mention + ', Aleyküm selam.') 
    elif message.content == '!help':
        return await message.author.send('Commands: `!help`, `!avatar`, `!about`, `!thonk`, `!cat`, `!ping`, `!8ball`, `!roll`, `!eval`, `!say`, `!randomcat`')
        
@bot.event
async def on_message(message):
    if ''.join(message.content.split('')) == '!8ball':
        replies = ["It is certain",
		"It is decidedly so",
			"Without a doubt",
		"Yes, definitely",
			"You may rely on it",
		"As I see it, yes",
			"Most likely",
		"Outlook good",
			"Yes",
		"Signs point to yes",
			"Reply hazy try again",
		"Ask again later",
			"Better not tell you now",
		"Cannot predict now",
			"Concentrate and ask again",
		"Don't count on it",
			"My reply is no",
		"My sources say no",
			"Outlook not so good",
"Very doubtful"]
        await message.channel.send(message.author.mention + ', ' + random.choice(replies))
	
@bot.event
async def on_message(message):
	if message.content.startswith('!'):
		await message.channel.send(message.author.mention + ", Unknown Command!")

@bot.event
async def on_message(message):
	randomnumeral = random.randint(1, 100)
	if randomnumeral >= 95:
		await message.channel.send(message.author.mention + f", LEVEL UP! YOU ARE NOW LEVEL **{random.randint(1, 21)}**")

@bot.event
async def on_message(message):
	if message.content.startswith('!eval '):
		ev = eval(message.content.replace('!eval ', ''))
		await message.channel.send(message.author.mention + ', ' + str(ev))
		
@bot.event
async def on_message(message):
	if message.content == '!randomcat' and True:
		randomcat = 'https://i.imgur.com/jjqKt7t.gifv'
		await message.channel.send(message.author.mention + f', here is ur random cat {randomcat}')
		return randomcat
	return 'hi'
        
@bot.event
async def on_message(message):
	if message.content.startswith('!say '):
		await message.channel.send(message.author.mention + ', ' + message.content.replace('!say ', ''))

@bot.event
async def on_message(message):
	if 'fuck' in message.content:
		await message.channel.send(message.author.mention + ', nO swearing!!111!1')
		
		
@bot.event
async def on_message(message):
    boolean = True
    if bool(boolean) != False and bool(boolean) == True:
        if 'discord.gg' in message.content:
            await message.delete()
            return await message.channel.send(message.author.mention + ', No Invites!!1! You will get baned soon.')
        else:
            pass
    else:
        pass

bot.login("NTM0NzkwMzIyMjExNzgyNjc2.Dx-9Kg.8QJoYfQwvXy-hUGZbls93tDvANA")
