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
  if message.channel.is_private and message.author.id != "716206205856382996":
      if message.content == "!help":
        await client.send_message(message.channel, "Command Help:\n```!help - Punch Bot의 명령어들을 확인합니다.\n!download - Punch PVP Client를 다운로드 할 수 있는 링크를 지급 받습니다.```")
      if message.content == "!download":
        await client.send_message(message.channel, "다운로드 링크: http://www.mediafire.com/file/bxrwd2y870369ql/Punch.zip/file")
      if message.content == "!notice":
        if message.author.id == "623502843558756394":
          if message.content[7:]:
            await client.send_message(discord.utils.get(client.get_all_channels(), id="713705245280305173"), "@everyone\n" + message.content[7:] + "")
          else:
            await client.send_message(message.channel, "```공지사항으로 등록할 메세지를 적어주세요.```")
        else:
          await client.send_message(message.channel, "```당신은 이 명령어를 사용할 권한이 없습니다.```")
      if message.content == "!update":
        if message.author.id == "623502843558756394":
          if message.content[7:]:
            await client.send_message(discord.utils.get(client.get_all_channels(), id="713704015384543262"), "@everyone\n```" + message.content[7:] + "```")
          else:
            await client.send_message(message.channel, "```업데이트으로 등록할 메세지를 적어주세요.```")
        else:
          await client.send_message(message.channel, "```당신은 이 명령어를 사용할 권한이 없습니다.```")
      if message.content == "!say":
        if message.author.id == "623502843558756394":
          if message.content[8:]:
            await client.send_message(discord.utils.get(client.get_all_channels(), id=message.content[5:23]), "@everyone\n" + message.content[24:] + "")
          else:
            await client.send_message(message.channel, "```공지사항으로 등록할 메세지를 적어주세요.```")
        else:
          await client.send_message(message.channel, "```당신은 이 명령어를 사용할 권한이 없습니다.```")
    

          

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
