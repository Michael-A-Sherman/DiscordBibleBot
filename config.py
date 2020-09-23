import os
import json

with open("config.json") as config_file:
    config = json.load(config_file)


class Config:
    DISCORD_TOKEN = config.get("DISCORD_TOKEN")
    DISCORD_GUILD = config.get("DISCORD_GUILD")