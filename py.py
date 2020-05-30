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
  if message.content.startwith(".help"):
      await client.send_message(message.channel, "Command Help")
      await client.send_message(message.channel, "```!help - Show Punch Bot's Commands\n!download - Sends you the latest version of Punch")
 

acces_token = os.environ["BOT_TOKEN"]
client.run(acces_token)
