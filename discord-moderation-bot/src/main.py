main.py:

# Python

import discord
from bot import Bot

# Create a Discord client
client = discord.Client()

# Initialize the Bot
bot = Bot(client)

# Event listener for when the bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Event listener for when a message is received
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # Process the message using the Bot
    await bot.process_message(message)

# Run the Discord client with the bot's token
client.run('your_bot_token_here')