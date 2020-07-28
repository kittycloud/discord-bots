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
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False),
                guild.me: discord.PermissionOverwrite(send_messages=True)
            }
            channel = await guild.create_text_channel('kevins-funhouse', overwrites=overwrites)
            await channel.send('my name is kevin!')
            # time.sleep(15)
            # await channel.delete()
        if '$create_guild' in message.content.lower():
            new_guild = await client.create_guild('Kevin`s Cathouse')
            new_guild_invite = await new_guild.create_invite()
            await message.channel.send(f"Come join me here! {new_guild_invite}")

client.run(TOKEN)