import discord
import time

TOKEN: str = ''
with open('efficiency-bot/Efficiency-Bot/not_public.txt', 'r') as tokenFile:
    TOKEN = tokenFile.read()

intents = discord.Intents.all()
intents.message_content = True

bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Im watching...')

@bot.event
async def on_voice_state_update(member, before, after):
    print("Voice State Change")
    if before.channel is None and after.channel is not None:
       text_to_write = member.display_name + " Logged In @ " + str(time.time())
       print(text_to_write)
       with open("efficiency-bot/Efficiency-Bot/time_log.txt", "w") as time_log:
            time_log.write(text_to_write)
    if before.channel is not None and after.channel is None:
        text_to_write = member.display_name + " Logged Out @ " + str(time.time())
        print(text_to_write)
        with open("efficiency-bot/Efficiency-Bot/time_log.txt", "w") as time_log:
            time_log.write(text_to_write)



bot.run(TOKEN)
