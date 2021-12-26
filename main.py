import discord
from discord.ext import commands
import aiohttp
from discord.voice_client import VoiceClient
import os
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()
client = commands.Bot(command_prefix='?', case_insensitive=True)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

class ManageUser:
    @client.command()
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, user: discord.Member, *, reason=None):
        await user.kick(reason=reason)
        embedVar = discord.Embed(
            title="Kick", 
            description=f"***{user}*** wyrzucony", 
            color=0xe35f00
        )
        embedVar.add_field(
            name="Powód:", 
            value=reason, 
            inline=True
        )
        await ctx.send(embed=embedVar)
    
    @client.command()
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, user: discord.Member, *, reason=None):
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

    @client.command()
    async def unban(ctx, *, member):
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

    @client.command()
    @commands.has_permissions(kick_members=True)
    async def warn(ctx, member: discord.Member, *, arg, reason=None):
        user = member.mention
        embed = discord.Embed(title="Ostrzeżenie: ", color=0xf40000)
        embed.add_field(name="Ostrzeżenie: ", value=f'Powód: {arg}', inline=False)
        embed.add_field(name="Ostrzeżenie użytkownika: ", value=f'{member.mention}', inline=False)
        embed.add_field(name="Ostrzegany przez: ", value=f'{ctx.author}', inline=False)
        
        await member.send(f'Zostałes ostrzeżony za: **{arg}**!')
        message = await ctx.send(embed=embed)

class Animals:
    @client.command()
    async def dog(ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/dog')
            dogjson = await request.json() 
        embed = discord.Embed(
            title="Pies!", 
            color=discord.Color.blue()
        )
        embed.set_image(url=dogjson['link'])
        await ctx.send(embed=embed)

    @client.command()
    async def cat(ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/cat')
            catjson = await request.json() 
        embed = discord.Embed(
            title="Kot!", 
            color=discord.Color.green()
        )
        embed.set_image(url=catjson['link'])
        await ctx.send(embed=embed)

    @client.command()
    async def fox(ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/fox')
            foxjson = await request.json() 
        embed = discord.Embed(
            title="Lis!", 
            color=discord.Color.green()
        )
        embed.set_image(url=foxjson['link'])
        await ctx.send(embed=embed)

    @client.command()
    async def panda(ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animal/panda')
            pandajson = await request.json() 
        embed = discord.Embed(
            title="Panda!", 
            color=discord.Color.green()
        )
        embed.set_image(url=pandajson['image'])
        await ctx.send(embed=embed)

    @client.command()
    async def koala(ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animal/koala')
            koalajson = await request.json() 
        embed = discord.Embed(
            title="Koala!", 
            color=discord.Color.green()
        )
        embed.set_image(url=koalajson['image'])
        await ctx.send(embed=embed)

    @client.command()
    async def bird(ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animal/birb')
            birdjson = await request.json() 
        embed = discord.Embed(
            title="Bird!", 
            color=discord.Color.green()
        )
        embed.set_image(url=birdjson['image'])
        await ctx.send(embed=embed)

    @client.command()
    async def raccoon(ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animal/raccoon')
            raccoonjson = await request.json() 
        embed = discord.Embed(
            title="Raccoon!", 
            color=discord.Color.green()
        )
        embed.set_image(url=raccoonjson['image'])
        await ctx.send(embed=embed)

    @client.command()
    async def kangaroo(ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animal/kangaroo')
            kangaroojson = await request.json() 
        embed = discord.Embed(
            title="kangaroo!", 
            color=discord.Color.green()
        )
        embed.set_image(url=kangaroojson['image'])
        await ctx.send(embed=embed)

@client.command()
async def wassup(ctx):
    await ctx.send(file=discord.File(r'./sounds/wassup.mp3'))

@client.command()
async def helpme(ctx):
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

@client.command()
async def rand(ctx):
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

# Add clear command

client.run(TOKEN)