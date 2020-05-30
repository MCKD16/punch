import discord
import os

client = discord.Client()


@client.event
async def on_ready():
  print("login")
  print(client.user.name)
  print(client.user.id)
  print("----------------")
  await client.change_presence(game=discord.Game(name=''. type1))
  
@client.event
async def on_message(message):
  if message.content.startswith("!help"):
    if message.channel.is_private and message.author.id != "716206205856382996":
      await client.send_message(message.author.id, "Commands:")
      await client.send_message(message.author.id, "```!help - Punch Bot에 대한 명령어들을 확인합니다.")
 

acces_token = os.environ["BOT_TOKEN"]
client.run(acces_token)
