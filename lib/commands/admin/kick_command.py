import discord
from discord.ext import commands
import json
import os

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        await user.kick(reason=reason)
        embedVar = discord.Embed(
            title="Kick", 
            description=f"***{user}*** wyrzucono", 
            color=0xe35f00
        )
        embedVar.add_field(
            name="Powód:", 
            value=reason, 
            inline=True
        )
        await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(MyCog(bot))