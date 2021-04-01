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

@bot.command()
async def undaniel(ctx):
    pairs = dict()
    with open(f'resources/{ctx.guild}.json', 'r') as f:
        pairs = json.loads(f.read())
    for user in ctx.guild.members:
        try:
            if str(user.id) in pairs:
                print(True)
                await user.edit(nick=pairs[str(user.id)])
            else:
                print(False)
        except Exception as e:
            print(user, e)

@bot.command()
async def hello(ctx):
    await ctx.send('Hello world!')

with open('resources/token', 'r') as f:
    bot.run(f.read())
