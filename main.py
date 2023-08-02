import discord
import time

TOKEN: str = ''
with open('efficiency-bot/Efficiency-Bot/not_public.txt', 'r') as tokenFile:
    TOKEN = tokenFile.read()

print(TOKEN)

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Im watching...')

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None: 
       time_log.write()
    if before.channel is not None and after.channel is None:
          print(member, " signed out of work!")



client.run(TOKEN)
