import discord
import asyncio
import random

client = discord.Client()

token = "ODc4MjE2MzM1NjM1Njc3MjQ0.YR98sg.jCwn37hzh2rTg-JlSvdkIcWQSaY"

@client.event
async def on_ready():
    print(client.user.name)
    print("서잼 코어 by seojem0407")
    game = discord.Game("전승부대에서 일하는중")
    await client.change_presence(staus=discord.Staus.online, activity=game)

@client.event

async def on_message(message):
     if message.content == "서잼코어가 뭐에요?":
        await message.channel.send("서잼이 만든 전승부대 봇이에요")
        
     if message.content == "켈블 바보!":
        await message.channel.send("인정")
        
     if message.content == "내가 오늘 진급할 확률은..?":
        ran = random.randint(0,1)
        if ran == 0:
            d = "당신은 오늘 진급할수 없네요 ㅠ"
        if ran == 1:
            d = "당신은 오늘 진급할수 있어요!"
        await message.channel.send(d)

client.run(token)
