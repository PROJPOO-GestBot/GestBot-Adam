import discord
import os
from dotenv import load_dotenv
from libs.Susers import Susers

load_dotenv()

bot = discord.Bot()

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

bot.run(os.environ['BOT_TOKEN'])
