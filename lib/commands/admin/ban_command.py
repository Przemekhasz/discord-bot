import discord
from discord.ext import commands
import json
import os

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason=None):
        await user.ban(reason=reason)
        embedVar = discord.Embed(
            title="Ban", 
            description=f"***{user}*** zbanowany", 
            color=0xc90000
        )
        embedVar.add_field(
            name="Powód:", 
            value=reason, 
            inline=True
        )
        await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(MyCog(bot))