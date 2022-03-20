import discord
from discord.ext import commands
import json
import os
import aiohttp

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fox(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/fox')
            foxjson = await request.json() 
        embed = discord.Embed(
            title="Lis!", 
            color=discord.Color.green()
        )
        embed.set_image(url=foxjson['link'])
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(MyCog(bot))