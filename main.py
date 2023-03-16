import os
import discord
import requests
import json



TOKEN = os.environ['TOKEN']

intents = discord.Intents.default()
intents.message_content = True
url= 'https://v2.jokeapi.dev/joke/Any'


client = discord.Client(intents=intents)

def get_quote():
  response = requests.get(url)

  if response.status_code == 200:
    data = response.json()
    if data["type"] == "single":
        joke = data["joke"]
        return joke
    elif data["type"] == "twopart":
        setup = data["setup"]
        delivery = data["delivery"]
        return(setup,delivery)
        (delivery)
    else:
        return("Unexpected joke type:", data["type"])
  else:
    return("Request failed with status code:", response.status_code)


  

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send(get_quote())
  
    

client.run(TOKEN)
  
  
