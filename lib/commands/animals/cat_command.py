import discord
from discord.ext import commands
import json
import os
import aiohttp

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/cat')
            catjson = await request.json() 
        embed = discord.Embed(
            title="Kot!", 
            color=discord.Color.green()
        )
        embed.set_image(url=catjson['link'])
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(MyCog(bot))