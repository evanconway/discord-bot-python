import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

from discord.ext import commands
import discord

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Hello! Bot is ready.')
    channel = bot.get_channel(CHANNEL_ID)
    if channel == None:
        print('channel could not be found')
        print('tried to find channel id: ' + CHANNEL_ID)
    else:
        await channel.send('I am the bot and I am here.')

@bot.command()
async def add(ctx, x, y):
    result = int(x) + int(y)
    await ctx.send(f"{x} + {y} = {result}")



bot.run(BOT_TOKEN)
