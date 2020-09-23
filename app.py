import requests
import discord
from config import Config
import random 


# verse = 'Romans 8:32'
# api_call = requests.get(f'https://bible-api.com/{verse}?translation=KJV')

# verse = api_call.json()['text']

# print(verse)

TOKEN = Config.DISCORD_TOKEN
GUILD = Config.DISCORD_GUILD

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content[0] == '+':
        passage = message.content[1:]
        api_call = requests.get(f'https://bible-api.com/{passage}?translation=KJV')

        response = api_call.json()['text']
        await message.channel.send(response)

client.run(TOKEN)