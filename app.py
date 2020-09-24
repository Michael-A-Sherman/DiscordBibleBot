import requests
import discord
from config import Config

TOKEN = Config.DISCORD_TOKEN
GUILD = Config.DISCORD_GUILD

client = discord.Client()


@client.event
async def on_message(message):
    # ignore messages from bot
    if message.author == client.user:
        return

    if message.content[0] == "+":
        passage = message.content[1:]
        api_call = requests.get(f"https://bible-api.com/{passage}?translation=KJV")

        response = api_call.json()

        if "error" in response.keys():
            await message.channel.send("verse not found")
            pass

        else:
            for verses in response["verses"]:
                verse_number = verses["verse"]
                verse_text = verses["text"].strip()
                await message.channel.send(f"{verse_number}: {verse_text}")


client.run(TOKEN)
