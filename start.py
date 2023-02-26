import os, nextcord, random, asyncio, youtube_dl, sys, dismusic, nextwave
from dotenv import load_dotenv
from nextcord import SlashOption, FFmpegPCMAudio, TextChannel
from nextcord.ext import commands
from nextcord.utils import get
from youtube_dl import YoutubeDL



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = nextcord.Client(intents=nextcord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=nextcord. Activity(type=nextcord.ActivityType.listening, name='Phil Ochs'))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    channel = message.author.voice.channel
    voice = message.guild.voice_client
    if message.content.startswith('6chair'):
            await message.channel.send('A chair is a piece of furniture with a raised surface used to sit on, commonly for use by one person. Chairs are most often supported by four legs and have a back; however, a chair can have three legs or could have a different shape. A chair without a back or arm rests is a stool, or when raised up, a bar stool. A chair with arms is an armchair and with folding action and inclining footrest, a recliner. A permanently fixed chair in a train or theater is a seat or, in an airplane, airline seat; when riding, it is a saddle and bicycle saddle, and for an automobile, a car seat or infant car seat. With wheels it is a wheelchair and when hung from above, a swing. A chair for more than one person is a couch, sofa, settee, or loveseat; or a bench. A separate footrest for a chair is known as an ottoman, hassock or pouffe. The chair is known for its antiquity and simplicity, although for many centuries it was an article of state and dignity rather than an article of ordinary use. The chair is still extensively used as the emblem of authority in the House of Commons in the United Kingdom and Canada, and in many other settings.')
            print("Chair was cool")
    elif message.content.startswith('6join'):
            await channel.connect()
            print("My boy has arrived")
    elif message.content.startswith('6gtfo'):
            await voice.disconnect()
            print("He ran away I am very sad")   
        
client.run(TOKEN)
