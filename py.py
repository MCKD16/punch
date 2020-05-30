import discord
import os

client = discord.Client()


@client.event
async def on_ready():
  print("login")
  print(client.user.name)
  print(client.user.id)
  print("----------------")
  await client.change_presence(game=discord.Game(name=''. type=1))
  
@client.event
async def on_message(message):
  if message.content.startswith("!help"):
    if message.channel.is_private and message.author.id == "716206205856382996":
      await message.channel.send("성공")
 

acces_token = os.environ["BOT_TOKEN"]
client.run(acces_token)
