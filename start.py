import os, discord, random, sys, asyncio, subprocess, yt_dlp, fakeyou, json
from dotenv import load_dotenv
from discord import FFmpegPCMAudio, TextChannel
from discord.ext import commands
from discord.utils import getfakeyou
from mcstatus import JavaServer



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='6', intents=discord.Intents.all())



@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord. Activity(type=discord.ActivityType.listening, name='Phil Ochs'))



@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!', flush=True)
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('mc-server-start'):
            if(subprocess.call(["systemctl", "is-active", "--quiet", "mcserver"]) == 0): 
                await message.channel.send('Server already on')
            else:
                await message.channel.send('Server Startup Initiated')
                os.system("sudo systemctl start mcserver")
    elif message.content.startswith('mc-server-stop'):
            if(subprocess.call(["systemctl", "is-active", "--quiet", "mcserver"]) == 0): 
                await message.channel.send('Server Shutdown Initiated')
                os.system(f"/usr/local/bin/mcrcon/mcrcon -H {os.getenv('MinecraftServerAddress')} -p {os.getenv('MinecraftRCONPassword')} -w 5 'say Server is restarting!' save-all stop")
                await message.channel.send('Server Shutdown Complete')
            else:
                await message.channel.send('Server already off')
    await client.process_commands(message)

@client.command()
async def join(ctx):
    if ctx.message.content.startswith("6join"):
        await ctx.message.author.voice.channel.connect()
@client.command()
async def leave(ctx):
    if ctx.message.content.startswith("6leave"):
        await ctx.guild.voice_client.disconnect()
@client.command()
async def play(ctx, link):
    if ctx.message.content.startswith('6play'):
        try:
            os.system("rm /silver-vinyl/yownloader.mp3")
        finally:
            yt_dlp.YoutubeDL({'format': 'bestaudio/best','outtmpl': '/silver-vinyl/yownloader.%(ext)s','no_playlist': True,'extract_audio': True,'audio_format': 'mp3','prefer_ffmpeg': True,'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192',}]}).download(link)
        try:
            ctx.message.guild.voice_client.stop()
        finally:
            ctx.message.guild.voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg", source="/silver-vinyl/yownloader.mp3"))

client.run(TOKEN)
