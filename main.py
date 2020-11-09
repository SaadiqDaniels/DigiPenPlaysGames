# Import the necessary files and APIs
import sys
import discord  # py -m pip install discord
import keyboard  # py -m pip install keyboard
import time

# Start defining variables
client = discord.Client()
keydictionary = {
    '!up': 'up',
    '!down': 'down',
    '!left': 'left',
    '!right': 'right',
    '! ': 'space',
    '!space': 'space',
    '!shift': 'shift',
    '!rshift': 'right shift',
    '!lshift': 'left shift',
    '!alt': 'alt',
    '!ralt': 'right alt',
    '!lalt': 'left alt',
    '!a': 'a',
    '!b': 'b',
    '!c': 'c',
    '!d': 'd',
    '!e': 'e',
    '!f': 'f',
    '!g': 'g',
    '!h': 'h',
    '!i': 'i',
    '!j': 'j',
    '!k': 'k',
    '!l': 'l',
    '!m': 'm',
    '!n': 'n',
    '!o': 'o',
    '!p': 'p',
    '!q': 'q',
    '!r': 'r',
    '!s': 's',
    '!t': 't',
    '!u': 'u',
    '!v': 'v',
    '!w': 'w',
    '!x': 'x',
    '!y': 'y',
    '!z': 'z'
}


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

    if msg.content.startswith('!'):
        keyboard.press(keydictionary[msg.content])
        # await msg.channel.send(keydictionary[msg.content])
        time.sleep(0.25)
        keyboard.release(keydictionary[msg.content])

    if msg.content.startswith('$$'):
        keyboard.write(msg.content[2:])
        # await msg.channel.send(msg.content[2:])


# The real program
if len(sys.argv) == 2:
    print("Incorrect number of arguments given!")
else:
    client.run(sys.argv[1])
