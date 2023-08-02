import asyncio
import discord
import time
from discord.ext import commands

from utils import calculate_duration, minutes_to_hours

# Discord Stuff
intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='$', intents=intents)

# Token Handling
TOKEN: str = ''
with open('efficiency-bot/Efficiency-bot/not_public.txt', 'r') as tokenFile:
    TOKEN = tokenFile.read()


# Logging & Calculating {'member.name': session_start_time}
users_sessions = {'horheyjorge': 0, 'eksno': 0, 'herecomessebastianvettel': 0}

async def member_joined_office(member):
    start_clock_for_member(member)
    logging_channel = discord.utils.get(client.get_all_channels(), name="hour-logging")
    display_text = member.display_name + " Logged In."

    # Send Session Report
    await logging_channel.send(display_text)

async def member_left_office(member):
    # Variables
    session_duration = calculate_duration(member, users_sessions[member.name])
    logging_channel = discord.utils.get(client.get_all_channels(), name="hour-logging")
    display_text = member.display_name + " Logged Out with a Duration of " + str(session_duration) + " Minutes"

    # Send Session Report
    await logging_channel.send(display_text)

    # Log to file
    log = member.name + " " +  str(session_duration) +  "\n"
    with open("efficiency-bot/Efficiency-bot/time_logs.txt", "a") as time_logs:
        time_logs.write(log)

def start_clock_for_member(member):
    users_sessions[member.name] = time.time()

def weekly_hours(member):
    minutes_sum = 0
    with open("efficiency-bot/Efficiency-bot/time_logs.txt", "r") as time_logs:
        for line in time_logs:
            if line.split(" ")[0] == member.name:
                minutes_sum += float(line.split(" ")[1])
    return minutes_to_hours(minutes_sum)



# Discord Functions

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
@client.command()
async def weekly_log(ctx, member: discord.Member = None):
    if (member == None):
        member = ctx.author
    display_text = str(member.display_name) + " Accumulated a Total of " + str(weekly_hours(member)) + " Hours this Week."
    await ctx.send(display_text)


@client.event
async def on_voice_state_update(member, before, after):
    print("Voice State Change")
    if before.channel == None and after.channel != None:
        if after.channel.name == 'Office':
            await member_joined_office(member)
    if before.channel != None and after.channel == None:
        if before.channel.name == 'Office': 
            await member_left_office(member)
       

client.run(TOKEN)
