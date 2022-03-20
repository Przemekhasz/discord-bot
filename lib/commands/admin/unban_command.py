import discord
from discord.ext import commands
import json
import os

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
    
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embedVar = discord.Embed(
                title="Unban", 
                description=f"***{user}*** sukces, odbanowano!", 
                color=0x00ff00
            )
            await ctx.send(embed=embedVar)
            return

def setup(bot):
    bot.add_cog(MyCog(bot))