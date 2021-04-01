from discord.ext import commands
import discord
import json, os, time

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def daniel(ctx):
    pairs = dict()
    for user in ctx.guild.members:
        try:
            if not user.display_name == 'daniel':
                pairs[user.id] = user.display_name
            await user.edit(nick='daniel')
        except Exception as e:
            print(user, e)
    if os.path.isfile(f'resources/{ctx.guild}.json'):
        os.rename(f'resources/{ctx.guild}.json', f'resources/{ctx.guild}_{time.time()}.json')
    with open(f'resources/{ctx.guild}.json', 'w') as f:
        f.write(json.dumps(pairs))
    await ctx.send('daniel complete')

@bot.command()
async def undaniel(ctx, args=None):
    pairs = dict()
    with open(args if args else f'resources/{ctx.guild}.json', 'r') as f:
        pairs = json.loads(f.read())
    for user in ctx.guild.members:
        try:
            if str(user.id) in pairs and pairs[str(user.id)] != 'daniel':
                await user.edit(nick=pairs[str(user.id)])
        except Exception as e:
            print(user, e)
    await ctx.send('undaniel complete')

@bot.command()
async def danieltonormal(ctx):
    await ctx.send('danieltonormal start')
    for user in ctx.guild.members:
        try:
            if user.display_name == 'daniel':
                await user.edit(nick=user.name)
        except Exception as e:
            ctx.send(f'Error on {user}: {e}')
    await ctx.send('danieltonormal complete')


@bot.command()
async def hello(ctx):
    await ctx.send('Hello world!')

@bot.command()
async def messagehere(ctx, *, args):
    await ctx.send(args)

with open('resources/token', 'r') as f:
    bot.run(f.read())
