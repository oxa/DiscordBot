import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@bot.command(name='say_hello', help='Say Hello :)')
async def hello(ctx, name):
    await ctx.send("Hello {} ! Nice to have you there !".format(name))

client.run(TOKEN)