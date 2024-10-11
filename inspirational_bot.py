import discord
import random
import asyncio

# Create the client instance
intents = discord.Intents.default()
client = discord.Client(intents=intents)

TOKEN = open("key.txt").read()
CHANNEL_ID = open("channel_id.txt").read()

# List of inspirational quotes
inspirational_quotes = [
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    "Act as if what you do makes a difference. It does. – William James",
    "You are never too old to set another goal or to dream a new dream. – C.S. Lewis"
]

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    # Start sending daily quotes when the bot is ready
    client.loop.create_task(send_daily_quote())

@client.event
async def on_message(message):
    # If the author of the message is the bot itself, ignore
    if message.author == client.user:
        return

    # Trigger command to get an inspirational quote
    if message.content.lower() == '!inspire':
        quote = random.choice(inspirational_quotes)
        await message.channel.send(quote)

async def send_daily_quote():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    while not client.is_closed():
        quote = random.choice(inspirational_quotes)
        await channel.send(quote)
        await asyncio.sleep(86400)  # Sends once every 24 hours (86400 seconds)

# This is the proper way to run the client in an asynchronous context
async def main():
    async with client:
        await client.start(TOKEN)

asyncio.run(main())