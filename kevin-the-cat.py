import discord
import os
import time
import logging

logging.basicConfig(level=logging.INFO)

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
    if client.user in mention:
        if 'hi' in message.content.lower():
            await message.channel.send('_purrs_')
        if 'play' in message.content.lower():
            guild = message.guild
            channel = await guild.create_text_channel('kevins-funhouse')
            await channel.send('my name is kevin!')
            # time.sleep(15)
            # await channel.delete()

client.run(TOKEN)