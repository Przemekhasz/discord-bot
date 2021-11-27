import discord
from discord.ext import commands
import aiohttp
from discord.voice_client import VoiceClient

# ! before push remove token
TOKEN = 'your token'

client = discord.Client()
client = commands.Bot(command_prefix='?')

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
            dogjson = await request.json() 
        embed = discord.Embed(
            title="Kot!", 
            color=discord.Color.green()
        )
        embed.set_image(url=dogjson['link'])
        await ctx.send(embed=embed)

    @client.command()
    async def fox(ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/fox')
            dogjson = await request.json() 
        embed = discord.Embed(
            title="Lis!", 
            color=discord.Color.green()
        )
        embed.set_image(url=dogjson['link'])
        await ctx.send(embed=embed)

    @client.command()
    async def panda(ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animal/panda')
            dogjson = await request.json() 
        embed = discord.Embed(
            title="Panda!", 
            color=discord.Color.green()
        )
        embed.set_image(url=dogjson['image'])
        await ctx.send(embed=embed)

    @client.command()
    async def koala(ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animal/koala')
            dogjson = await request.json() 
        embed = discord.Embed(
            title="Koala!", 
            color=discord.Color.green()
        )
        embed.set_image(url=dogjson['image'])
        await ctx.send(embed=embed)

    @client.command()
    async def ptak(ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animal/birb')
            dogjson = await request.json() 
        embed = discord.Embed(
            title="Ptak!", 
            color=discord.Color.green()
        )
        embed.set_image(url=dogjson['image'])
        await ctx.send(embed=embed)

    @client.command()
    async def szop(ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animal/raccoon')
            dogjson = await request.json() 
        embed = discord.Embed(
            title="Szop pracz!", 
            color=discord.Color.green()
        )
        embed.set_image(url=dogjson['image'])
        await ctx.send(embed=embed)

    @client.command()
    async def kangur(ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animal/kangaroo')
            dogjson = await request.json() 
        embed = discord.Embed(
            title="Kangur!", 
            color=discord.Color.green()
        )
        embed.set_image(url=dogjson['image'])
        await ctx.send(embed=embed)

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
        name="?kangur:", 
        value="Zwraca losowego kangura", 
        inline=True
    )
    embed.add_field(
        name="?szop:", 
        value="Zwraca losowego szopa", 
        inline=True
    )
    embed.add_field(
        name="?ptak:", 
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
    await ctx.send(embed=embed) 

# Add clear command

# Fucking MusicPlayer is not working
class MusicPlayer():
    players = {}

    def __init__(self, players) -> None:
        self.players = players

    @client.command()
    async def join(ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
        await channel.connect()
        
    @client.command(pass_context=True)
    async def leave(ctx):
        server = ctx.message.server
        voice_client = client.voice_client_in(server)
        await voice_client.disconnect()

    @client.command(pass_context=True)
    async def play(self, ctx, url):
        server = ctx.message.server
        voice_client = client.voice_client_in(server)
        player = await voice_client.create_ytdl_player(url)
        self.players[server.id] = player
        player.start()

    @client.command(pass_context=True)
    async def stop(self, ctx):
        id = ctx.message.server.id
        self.players[id].stop()

    @client.command(pass_context=True)
    async def resume(self, ctx):
        id = ctx.message.server.id
        self.players[id].resume()

client.run(TOKEN)