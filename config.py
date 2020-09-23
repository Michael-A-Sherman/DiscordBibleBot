import os
import json
import pathlib

with open(pathlib.Path.cwd()/'config.json') as config_file:
    config = json.load(config_file)


class Config:
    DISCORD_TOKEN = config.get("DISCORD_TOKEN")
    DISCORD_GUILD = config.get("DISCORD_GUILD")