import discord
import os

client = discord.Client()


@client.event
async def on_ready():
  print(client.user.id)
  print("ready")
  game = discord.Game("Commands: !help")
  await client.change.presence(status=discord.Status.online, activity=game)
  
@client.event
async def on_message(message):
  if message.content.startswith("!help"):
    await message.channel.send("성공")
 

acces_token = os.environ["BOT_TOKEN"]
client.run(acces_token)
