import os
from dotenv import load_dotenv
import discord
import requests
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
FORTNITE_TOKEN = os.getenv('FORTNITE_TOKEN')

client = discord.Client()
bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@bot.command(name='say_hello', help='Say Hello :)')
async def hello(ctx, name):
    await ctx.send("Hello {} ! Nice to have you there !".format(name))

@bot.command(name='fornite_info', help='retrieve fortnite player info')
async def fornite(ctx, username):

    url = "https://fortnite-api.com/v2/stats/br/v2?name={}".format(username)
    payload={}
    headers = {
        'Authorization': FORTNITE_TOKEN
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    data = response.json()
    user_score = data["data"]["stats"]["all"]["overall"]["score"]

    await ctx.send("User {} score is {} !".format(username,user_score))


client.run(TOKEN)