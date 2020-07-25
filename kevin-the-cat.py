import discord
import os

client = discord.Client()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    mention = message.mentions
    # if message.content.startswith('{0.user}'.format(client)):
    if client.user in mention:
       await message.channel.send('🎶 Hi! My name is {0.user.name}, I am an orange cat, and I have come here.. to help make shopping lists! 🎶'.format(client))

client.run(TOKEN)