import discord
from discord.ext import commands

TOKEN = 'ODE5MTQyMDg4NjU4MjU1OTQy.YEiThA.S-fLy9nfutFyguELZlPMhG2OjHI'

client = discord.Client()
client = commands.Bot(command_prefix='?')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

client.run(TOKEN)