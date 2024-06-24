import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello! I am your new bot.')

# always remove the token when pushing the code and enter when you have code locally
bot.run('MTI1NDY4NTgyMDUzOTg5NTkzMQ.GbqqzC.vwk0d4OqTCu5M0SNOtQAKFCY_ItAf4PxWeY7N0')