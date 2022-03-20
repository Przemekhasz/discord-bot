import discord
from discord.ext import commands
import json
import os

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member: discord.Member, *, arg, reason=None):
        user = member.mention
        embed = discord.Embed(title="Ostrzeżenie: ", color=0xf40000)
        embed.add_field(name="Ostrzeżenie: ", value=f'Powód: {arg}', inline=False)
        embed.add_field(name="Ostrzeżenie użytkownika: ", value=f'{member.mention}', inline=False)
        embed.add_field(name="Ostrzegany przez: ", value=f'{ctx.author}', inline=False)
        
        await member.send(f'Zostałes ostrzeżony za: **{arg}**!')
        message = await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(MyCog(bot))