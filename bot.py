import requests
import os
import discord
from dotenv  import load_dotenv
from discord.ext import commands
from discord.ext.commands import has_role
from discord import Member
from discord.utils import get

load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']
print(TOKEN)
#client = discord.Client()
key=os.environ['BOOKBOTCLUBAPI']
H={"api_key":key}
url="https://api.airtable.com/v0/appB7YoaWh3su8mAO/BookClubBot?maxRecords=999&view=Grid%20view"
r=requests.get(url,params=H)
books_dict=r.json()
print(books_dict)

client = commands.Bot(command_prefix="$")

@client.command(name="b")
async def b(ctx):
    await ctx.channel.send("read a book lil nigga")

@client.command(name="c")
async def c(ctx):
    await ctx.channel.send("I'm leaving in 2 minutes, good-bye.")
    await client.close()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run(TOKEN)

