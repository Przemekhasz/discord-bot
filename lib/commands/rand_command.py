import discord
from discord.ext import commands
import json
import os
import aiohttp

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rand(self, ctx):
        quotations = [
            '"Przepraszam za spoznienie, waliłem gruchę ~ Dr House"', 
            '"Potrafię dochować tajemnicy. Nikomu nie powiedziałem, że Wilson nadal moczy się w nocy" ~ Dr House', 
            '"Cameron : Mamy krwawienie z odbytu: House: Wszyscy?" ~ Dr House',
            '"Podstawowa prawda o ludziach jest taka że wszyscy kłamią, jedyna zmienna to to w jakiej sprawie." ~ Dr House',
            '"Ci którzy mnie znają uważają mnie za drania i dupka, ci którzy nie, widzą kalekę, i za takiego mnie uważają. Tylko samolubny drań by tego nie wykorzystał!" ~ Dr House',
            '"Bóg ma dobrze, bo nie kuleje." ~ Dr House',
            '"Jeśli do trzech godzin się nie zaszczepisz, będę musiał znaleźć innego murzyna." ~ Dr House',
            'Dr Wilson: "Nawet ja cię nie lubię". Dr House: "Wiesz, słowa mogą ranić." ~ Dr House',
            '"Jeśli rozmawiasz z Bogiem, jesteś religijny. Kiedy Bóg przemawia do ciebie jesteś chory psychicznie." ~ Dr House',
            '"Biblioteka jest bramą w czasie."',
            '"Ja się pieprzę z każdą książką, a jeżeli nie zostawiam na niej śladu, to znaczy, że nie mam orgazmu."',
            '"Żyj tak jakby każdy dzień był twoim ostatnim" ~ Berlin (La casa de papel)',
            '"Jeżeli czegoś nie da się zrobić, potrzebny jest ktoś kto o tym nie wie, przyjdzie i to zrobi" ~ Poranek Kojota',
            '"Lew nie przejmuje się opiniami owiec." ~ Tywin Lannister',
            '"Powrót do domu nocą też jest straszny, ale tłumicie strach i idziecie dalej" ~ Nairobi (La casa de papel)',
            '"Wykorzystaj siłę wroga na swoją korzyść" ~ Profesor (La casa de papel)',
            '"Jednakże wielcy ludzi nie rodzą się wielkimi, tylko się nimi stają" ~ Ojciec Chrzestny',
            '"Najlepszą zemstą jest ogromny sukces" ~ Frank Sinatra'
        ]
        await ctx.send(f"{random.choice(quotations)}")

def setup(bot):
    bot.add_cog(MyCog(bot))