import discord
from discord.ext import commands

TOKEN = 'ODE5MTQyMDg4NjU4MjU1OTQy.YEiThA.S-fLy9nfutFyguELZlPMhG2OjHI'

client = discord.Client()
client = commands.Bot(command_prefix='?')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
  await user.kick(reason=reason)
  await ctx.send(f"***{user}*** Wydupcony z powodu ***{reason}*** :wave:")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
  await user.ban(reason=reason)
  await ctx.send(f"***{user}*** został|a zbanowany|a z powodu ***{reason}*** :wave:")

@client.command()
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user
  
  if (user.name, user.discriminator) == (member_name, member_discriminator):
    await ctx.guild.unban(user)
    await ctx.send(f"***{user}*** sukces, odbanowano! :white_check_mark:")
    return

client.run(TOKEN)