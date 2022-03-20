import discord
from discord.ext import commands
import aiohttp
from discord.voice_client import VoiceClient
import os
import random
import json
from dotenv import load_dotenv

# token from .env file
load_dotenv()

TOKEN = os.getenv("TOKEN")

client = discord.Client()
client = commands.Bot(command_prefix='?', case_insensitive=True)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# . is path folder -> lib/commands
base_path = 'lib.commands.'
client.load_extension(base_path + "avatar_command")
client.load_extension(base_path + 'helpme_command')
client.load_extension(base_path + 'wassup_command')

# admin commands
admin_path = base_path + 'admin.'
client.load_extension(admin_path + 'ban_command')
client.load_extension(admin_path + 'kick_command')
client.load_extension(admin_path + 'unban_command')
client.load_extension(admin_path + 'warn_command')

# animals commands
animals_path = base_path + 'animals.'
client.load_extension(animals_path + 'bird_command')
client.load_extension(animals_path + 'cat_command')
client.load_extension(animals_path + 'dog_command')
client.load_extension(animals_path + 'fox_command')
client.load_extension(animals_path + 'kangaroo_command')
client.load_extension(animals_path + 'koala_command')
client.load_extension(animals_path + 'panda_command')
client.load_extension(animals_path + 'raccoon_command')

client.run(TOKEN)