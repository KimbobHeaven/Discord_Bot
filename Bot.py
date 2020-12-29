import discord
import random
import time

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        print(message.author)
        print(message.created_at)
        print(message.content)
        print(time.strftime('%Y-%m-%d %M:%S', time.localtime(time.time())))
        print()
        
        # if message.content == 'ping':
        #     await message.channel.send('pong')

        # elif message.content == '응~':
        #     await message.channel.send('아니야~')

        # else:
        #     chat = random.randrange(1,4) 
        #     if chat == 1:
        #         await message.channel.send('어쩌라고')
        #     elif chat == 2:
        #         await message.channel.send('응 아니야~')
        #     elif chat == 3:
        #         await message.channel.send('그래서 뭐')

client = MyClient()
client.run('token')

################################################################################

from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('token')

################################################################################

# client = discord.Client()

# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('$hello'):
#         await message.channel.send('Hello!')

# client.run('your token here')