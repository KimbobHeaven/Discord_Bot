import discord
import random
import time
from keep_running import keep_alive

token = "" # 여기다 자신의 봇 토큰 붙여넣기

class MyClient(discord.Client):
    async def on_ready(self):
        print('\nLogged on as', self.user, "\n")
    
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        
        message_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        
        print(message.author) # 메세지 친 사람
        print(message.created_at) # 메세지 친 시각 (세계 표준시)
        print(message_time) # 현재 컴퓨터 시각
        print(message.content) # 메세지 내용
        print()

        if message.content == 'ping':
            await message.channel.send('pong')

        elif message.content == '응~':
            await message.channel.send('아니야~')
        
        elif message.content == '...':
            await message.channel.send('점점점...')
        
        else:
            chat = random.randrange(1,20)
            if chat == 1:
                await message.channel.send('어쩌라고')
            elif chat == 2:
                await message.channel.send('응 아니야~')
            elif chat == 3:
                await message.channel.send('그래서 뭐')

client = MyClient()
keep_alive()
client.run(token)

################################################################################

# from discord.ext import commands

# bot = commands.Bot(command_prefix='>')

# @bot.command()
# async def ping(ctx):
#     await ctx.send('pong')

# bot.run('token')

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