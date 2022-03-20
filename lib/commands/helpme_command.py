import discord
from discord.ext import commands
import json
import os
import aiohttp

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def helpme(self, ctx):
        embed = discord.Embed(
            title="Komendy!", 
            color=discord.Color.blurple()
        )
        embed.add_field(
            name="?fox:", value="Zwraca losowego lisa", 
            inline=True
        )
        embed.add_field(
            name="?cat:", value="Zwraca losowego kota", 
            inline=True
        )
        embed.add_field(
            name="?dog:", value="Zwraca losowego psa", 
            inline=True
        )
        embed.add_field(
            name="?kangaroo:", 
            value="Zwraca losowego kangura", 
            inline=True
        )
        embed.add_field(
            name="?raccoon:", 
            value="Zwraca losowego szopa", 
            inline=True
        )
        embed.add_field(
            name="?bird:", 
            value="Zwraca losowego ptaka", 
            inline=True
        )
        embed.add_field(
            name="?koala:", 
            value="Zwraca losową koale", 
            inline=True
        )
        embed.add_field(
            name="?panda:", 
            value="Zwraca losową pande", 
            inline=True
        )
        embed.add_field(
            name="?wassup:", 
            value="Wysyła dźwięk z serialu the office wassup!", 
            inline=True
        )
        embed.add_field(
            name="?avatar:", 
            value="?avatar ***@nazwa***", 
            inline=True
        )
        embed.add_field(
            name="Komendy:", 
            value="ADMINI", 
            inline=False
        )
        embed.add_field(
            name="?kick:", 
            value="?kick ***@nazwa*** powód", 
            inline=True
        )
        embed.add_field(
            name="?ban:", 
            value="?ban ***@nazwa*** powód", 
            inline=True
        )
        embed.add_field(
            name="?unban:", 
            value="?unban ***nazwa#12345***", 
            inline=True
        )
        embed.add_field(
            name="?warn:", 
            value="?warn ***@nazwa312345*** powód", 
            inline=True
        )
        embed.add_field(
            name="?rand:", 
            value="Zwraca randomowy cytat", 
            inline=True
        )
        await ctx.send(embed=embed) 

def setup(bot):
    bot.add_cog(MyCog(bot))