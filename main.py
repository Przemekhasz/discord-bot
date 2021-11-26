import discord
from discord.ext import commands
import aiohttp

TOKEN = 'ODE5MTQyMDg4NjU4MjU1OTQy.YEiThA.GBQTw9wfBXeSJRstWYzWQUoH0lM'

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
        embedVar = discord.Embed(title="Kick", description=f"***{user}*** wyrzucony", color=0xe35f00)
        embedVar.add_field(name="Powód:", value=reason, inline=True)
        await ctx.send(embed=embedVar)

    @client.command()
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, user: discord.Member, *, reason=None):
        await user.ban(reason=reason)
        embedVar = discord.Embed(title="Ban", description=f"***{user}*** zbanowany", color=0xc90000)
        embedVar.add_field(name="Powód:", value=reason, inline=True)
        await ctx.send(embed=embedVar)

    @client.command()
    async def unban(ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
    
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            embedVar = discord.Embed(title="Unban", description=f"***{user}*** sukces, odbanowano!", color=0x00ff00)
            await ctx.send(embed=embedVar)
            return
            
ManageUser.kick
ManageUser.ban
ManageUser.unban

class Animals:
    @client.command()
    async def dog(ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/dog')
            dogjson = await request.json() 
        embed = discord.Embed(title="Pies!", color=discord.Color.blue())
        embed.set_image(url=dogjson['link'])
        await ctx.send(embed=embed)

    @client.command()
    async def cat(ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/cat')
            dogjson = await request.json() 
        embed = discord.Embed(title="Kot!", color=discord.Color.green())
        embed.set_image(url=dogjson['link'])
        await ctx.send(embed=embed)

    @client.command()
    async def fox(ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/fox')
            dogjson = await request.json() 
        embed = discord.Embed(title="Lis!", color=discord.Color.green())
        embed.set_image(url=dogjson['link'])
        await ctx.send(embed=embed)

Animals.dog
Animals.cat
Animals.fox

client.run(TOKEN)