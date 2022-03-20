import discord
from discord.ext import commands
import json
import os
import aiohttp

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, *,  avamember : discord.Member=None):
        userAvatarUrl = avamember.avatar_url
        embed = discord.Embed(
            title=str(avamember), 
            color=discord.Color.green()
        )
        embed.set_image(url=userAvatarUrl)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(MyCog(bot))