# Import the necessary files and APIs
import sys
import discord  # py -m pip install discord
import keyboard  # py -m pip install keyboard
import time

# Start defining variables
client = discord.Client()

# A dictionary of valid key presses
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

    # Ignore messages not in the CLI specified channel
    if msg.channel.name != sys.argv[2]:
        return

    # This code will interpret commands that correspond to the keydictionary above.
    # this does not do any mis-type detection, so it will cause an exception if someone mis-types
    if msg.content.startswith('!'):
        keyboard.press(keydictionary[msg.content])
        # If you make this sleep for longer, then a longer key press will happen. I commonly used 0.1 and 0.25
        time.sleep(0.1)
        keyboard.release(keydictionary[msg.content])
        # await msg.channel.send(keydictionary[msg.content]) Will echo the message back through discord

    # This code will interpret strings that start with $$,
    # inputting the entire string of letters into the keyboard system
    if msg.content.startswith('$$'):
        keyboard.write(msg.content[2:])
        # await msg.channel.send(msg.content[2:]) Will echo the message back through discord


# The real program
if len(sys.argv) != 3:
    print("Incorrect number of arguments given!")
else:
    client.run(sys.argv[1])
