import discord
import datetime
from keep_running import keep_alive
import os
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
# .env 에서 토큰 관리
latest_message = {}
latest_time = {}
# 시간, 메세지를 딕셔너리로 저장


class MyClient(discord.Client):
    async def on_ready(self):
        print('\nLogged on as', self.user)
        # 디코 봇 온라인(로그인) 메세지

    async def on_message(self, message):
        if message.author == self.user:
            return
        # 해당 봇이 입력하는 메세지는 제외

        author, sharp_num = str(message.author).split('#')  # 이름#1234 형태를 #을 기준으로 분리
        now = message.created_at + datetime.timedelta(hours=9)  # 세계 표준시 + 9시간
        now -= datetime.timedelta(microseconds=now.microsecond)  # 마이크로초 생략

        print()  # 가시성 공백
        print(author)  # 메세지 작성자
        print(message.content)  # 메세지 내용
        print(now)  # 메세지 작성 시간

        async def message_send(author_factor):
            await message.channel.send(author_factor)  # 메세지 작성자
            await message.channel.send(latest_message[author_factor])  # 메세지 내용
            await message.channel.send(latest_time[author_factor])  # 메세지 작성 시간
            await message.channel.send('-' * 10)  # 가시성 줄

        if message.content == '!log':
            await message.channel.send('-' * 10)
            for latest_time_keys in latest_time.keys():  # 작성 기록이 있는 작성자 모두 해당
                await message_send(latest_time_keys)

        elif message.content.split(' ')[0] == '!log':  # !log [작성자]
            if message.content[5:] in latest_time.keys():  # 명시한 작성자의 기록이 있을시
                await message.channel.send('-' * 10)
                await message_send(message.content[5:])

            else:  # [작성자]를 잘못 입력했거나 입력한 [작성자]의 기록이 없을시
                await message.channel.send('There is no matching name.\nTry : ' + author)

        latest_message[author] = message.content
        latest_time[author] = now
        # 작성 시간, 메세지 딕셔너리 업데이트


client = MyClient()  # ?
keep_alive()  # 서버 24시간 구동
client.run(token)  # 디코 토큰

################################################################################

# from discord.ext import commands

# bot = commands.Bot(command_prefix='>')

# @bot.command()
# async def ping(ctx):
#     await ctx.send('pong')

# bot.run(token)

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
