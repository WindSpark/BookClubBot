# token for book bot line 2
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import has_role
from discord import Member
from discord.utils import get

load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']
print(TOKEN)
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)