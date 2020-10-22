import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = "NzY4NDgyNzAzNDMwNzc4ODgw.X5BHSg.SNtFUnMsHR1mz8TL24XuC3CJJDA"
client = discord.Client()

@client.event
async def on_ready():
    print('im in as {0.user}'.format(client))


@client.event

async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith('hello'):
        await message.channel.send('hey fellow saiyan')

    elif message.content.startswith('Hello'):
        await message.channel.send('hey fellow saiyan')

    elif message.content.startswith('are u saiyan enough'):
        await message.channel.send('go ask bulma if im man enough')

    elif message.content.startswith('Are u saiyan enough'):
        await message.channel.send('go ask bulma if im man enough')   
    


client.run(TOKEN)
