import requests
import os
import discord
from dotenv  import load_dotenv
from discord.ext import commands
from discord.ext.commands import has_role
from discord import Member
from discord.utils import get
#from array import *

load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']
print(TOKEN)
#client = discord.Client()
key=os.environ['BOOKBOTCLUBAPI']
H={"api_key":key}
url="https://api.airtable.com/v0/appB7YoaWh3su8mAO/BookClubBot?maxRecords=999&view=Grid%20view"
r=requests.get(url,params=H)
books_dict=r.json()
book_list = books_dict["records"]


def printout_book(books_dict):
    book=books_dict['fields']
    print(book['Title'])
    print(book['Author'])
    print(book["Genre"])
    print(book["Content Warnings"])
    print(book["Description"])


client = commands.Bot(command_prefix="$")

@client.command(name="b")
async def b(ctx):
    book=book_list[0]
    print(book)
    book_info=book['fields']
    await ctx.channel.send("Here's my suggestion")
    await ctx.channel.send("Title: "+book_info['Title'])
    await ctx.channel.send("Author(s): "+book_info['Author'])
    await ctx.channel.send("Genre(s): "+book_info['Genre'])
    await ctx.channel.send("Content Warning(s): "+book_info['Content Warnings'])
    await ctx.channel.send("Description: "+book_info['Description'])


@client.command(name="c")
async def c(ctx):
    await ctx.channel.send("I'm leaving in 2 minutes, good-bye.")
    await client.close()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.run(TOKEN)

