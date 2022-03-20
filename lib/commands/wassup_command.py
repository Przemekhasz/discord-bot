import discord
from discord.ext import commands
import json
import os
import aiohttp

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wassup(self, ctx):
        await ctx.send(file=discord.File(r'./sounds/wassup.mp3'))

def setup(bot):
    bot.add_cog(MyCog(bot))