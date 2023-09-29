import os
from dotenv import load_dotenv
from discord.ext import commands
import discord
from dataclasses import dataclass

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

@dataclass
class Session:
    is_active: bool = False
    start_time: int = 0

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
session = Session()

@bot.event
async def on_ready():
    print('Hello! Bot is ready.')
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('I am the bot and I am here.')

@bot.command()
async def start(ctx):
    if session.is_active:
        await ctx.send('A session is already active.')
        return
    session.is_active = True
    session.start_time = ctx.message.created_at.timestamp()
    readable_time = ctx.message.created_at.strftime("%H:%M:%S")
    await ctx.send(f'New study session started at {readable_time}')

@bot.command()
async def stop(ctx):
    if (not session.is_active):
        await ctx.send('Session is not active.')
        return
    session.is_active = False
    await ctx.send('Study session stopped.')

bot.run(BOT_TOKEN)
