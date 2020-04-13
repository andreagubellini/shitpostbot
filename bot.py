import discord
from discord.ext import commands
from scraper import scraper

client = commands.Bot(command_prefix='.')
token = 'my-token'

@client.event
async def on_ready():
    print('bot is ready.')

@client.event
async def on_message(message):
    if message.content.startswith('!shitpost'):
        channel = client.get_channel(int('my-channel-id'))
        img = scraper.scrape()
        await channel.send("Ecco la tua daily dose di shitpost: \n"+img)
        
client.run(token)