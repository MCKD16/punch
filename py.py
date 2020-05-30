import discord
import os
import datetime


client = discord.Client()


@client.event
async def on_ready():
  print("login")
  print(client.user.name)
  print(client.user.id)
  print("------------------")
  await client.change_presence(game=discord.Game(name='Commands: !help', type=1))

@client.event
async def on_message(message):
  SN = "`[스넷봇 시스템]"
  serverf = "Online"
  servert = "Online"
  if message.content == "=":
    await client.send_message(message.channel, "```정확하지 않은 명령어입니다.```")
  else:
    if message.content[1:5] == "help":
      if message.channel.is_private and message.author.id == "716206205856382996":
        await client.send_message(message.channel, "Command Help:")
        await client.send_message(message.channel, "```!help - Punch Bot에 대한 명령어목록을 확인합니다.```")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
