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
    '.u': 'up',
    '!down': 'down',
    '.d': 'down',
    '!left': 'left',
    '.l': 'left',
    '!right': 'right',
    '.r': 'right',
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

    # Convert the message to lowercase
    message = msg.content.lower()

    # Use space as a delimiter to split multiple commands in the same message
    commands = message.split(' ')
    for command in commands:
        if command.startswith('!') and command in keydictionary.keys():
            keyboard.press(keydictionary[command])
            # Wait between pressing and releasing a key
            time.sleep(0.1)
            keyboard.release(keydictionary[command])
            # Echo the message back to discord (useful for debugging)
            await msg.channel.send(keydictionary[command])

        if command.startswith('$$'):
            # Send the messages straight to the keyboard to write
            keyboard.write(command[2:])
            # Echo the message back to discord (useful for debugging)
            await msg.channel.send(command[2:])

# The real program
if len(sys.argv) != 3:
    print("Incorrect number of arguments given!")
else:
    client.run(sys.argv[1])
