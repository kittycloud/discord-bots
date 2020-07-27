import discord
import os

client = discord.Client()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name='Making Lists'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    mention = message.mentions
    if (client.user in mention) and (message.content.contains("hi")):
       await message.channel.send('🎶 Hi! My name is {0.user.name}, I am an orange cat, and I have come here.. to help make shopping lists! 🎶'.format(client))

client.run(TOKEN)