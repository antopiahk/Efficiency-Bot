import discord
import time

# Discord Stuff
intents = discord.Intents.all()
intents.message_content = True

bot = discord.Client(intents=intents)

# Token Handling
TOKEN: str = ''
with open('efficiency-bot/Efficiency-Bot/not_public.txt', 'r') as tokenFile:
    TOKEN = tokenFile.read()

logging_channel = bot.get_channel(1136091862839595018)

# Logging & Calculating
users_sessions_store = {'horheyjorge': 0, 'eksno': 0, 'herecomessebastianvettel': 0}

def member_joined_office(member):
    start_clock(member)
    text_to_write = member.display_name + " Joined Office @ " + str(time.time()) + "\n"
    print(text_to_write)
def member_left_office(member):
    text_to_write = member.display_name + " Logged Out @ " + str(calculate_duration(member)) + "\n"
    logging_channel.send(text_to_write)
    with open("efficiency-bot/Efficiency-Bot/time_log.txt", "a") as time_log:
        time_log.write(text_to_write)

def start_clock(member):
    users_sessions_store[member.name] = time.time()

def calculate_duration(member):
    start_time = users_sessions_store[member.name]
    duration = time.time() - start_time
    return seconds_to_minutes(duration)

def seconds_to_minutes(seconds):
    return round(seconds / 60)


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
    if before.channel == None and after.channel != None:
      if after.channel.name == 'Office':
        member_joined_office(member)
    if before.channel != None and after.channel == None:
        if before.channel.name == 'Office': 
           member_left_office(member)
       



bot.run(TOKEN)
