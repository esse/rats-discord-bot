import os

import discord

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!help':
        await message.channel.send("Dostępne komendy: !legacy !etpro")
    elif message.content == '!legacy':
        await message.channel.send("adres serwera: rats2.szmielew.pl")
    elif message.content == '!etpro':
        await message.channel.send("adres serwera: rats.szmielew.pl:26010")
  #      await message.channel.send("OK")
  #  elif message.content == 'stopserver!':
  #      await message.channel.send("OK2")

client.run(TOKEN)
