# Import the necessary files and APIs
import sys
import discord
import keyboard
import time

# Start defining variables
client = discord.Client()


# Log into discord
@client.event
async def on_ready():
    print('Logged in!')


@client.event
async def on_message(msg):
    # Ignore messages sent by the bot
    if msg.author == client.user:
        return

    if msg.channel.name != sys.argv[2]:
        return

    # Up message commands
    if msg.content.startswith('!up'):
        # Send up command
        await msg.channel.send('UP !')
        keyboard.press('w')
        time.sleep(1)
        keyboard.release('w')

    # Down message commands
    if msg.content.startswith('!down'):
        # Send up command
        await msg.channel.send('DOWN !')
        keyboard.press('s')
        time.sleep(1)
        keyboard.release('s')

    # Left message commands
    if msg.content.startswith('!left'):
        # Send up command
        await msg.channel.send('LEFT !')
        keyboard.press('a')
        time.sleep(1)
        keyboard.release('a')

    # Right message commands
    if msg.content.startswith('!right'):
        # Send up command
        await msg.channel.send('right !')
        keyboard.press('d')
        time.sleep(1)
        keyboard.release('d')


# The real program
if len(sys.argv) == 2:
    print("Incorrect number of arguments given!")
else:
    client.run(sys.argv[1])
