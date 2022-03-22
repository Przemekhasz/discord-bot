import discord
from discord.ext import commands
import json
import os
import aiohttp

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def mem(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('http://szprinktrap.ddns.net:1410/kurla.json')
            memjson = await request.json(content_type='text/html') 
        embed = discord.Embed(
            title="Losowy mem", 
            color=discord.Color.green()
        )
        embed.set_image(url=memjson['file'])
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(MyCog(bot))