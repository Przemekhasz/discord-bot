import discord
from discord.ext import commands
import json
import os
import aiohttp

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bird(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animal/birb')
            birdjson = await request.json() 
        embed = discord.Embed(
            title="Bird!", 
            color=discord.Color.green()
        )
        embed.set_image(url=birdjson['image'])
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(MyCog(bot))