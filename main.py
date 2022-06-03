import discord
import time
import threading

async def auto_bump():
  global channel
  while True:
    await channel.send('/bump')
    time.sleep(1800)
    
started = False
token = input("Type your token here: ")
client = discord.Client()
thread = threading.Thread(target=auto_bump, daemon=True)
  
def on_start():
  global started, thread
  thread.start()
  started = True

def on_stop():
  global started, thread
  thread._stop()
  started = False
  
@client.event
async def on_ready():
  print('The bot initialized successfully!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  global started
  if message.content.startswith('$start') and not started:
    global channel
    channel = message.channel
    on_start()
    await message.channel.send('The auto-bump operation was successfully started!')

  if message.content.startswith('$stop') and started:
    on_stop()
    await message.channel.send('The auto-bump operation was successfully stopped!')

client.run(token)
