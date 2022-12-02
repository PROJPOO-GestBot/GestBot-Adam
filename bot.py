import discord
import os
from libs.Susers import Susers

bot = discord.Bot()


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')    



@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

bot.run("MTA0MzA3ODk4MTA5MzY5NTUzOQ.GIEHVb.p_ktQhqcrRxa-ZcDYkbZtVs-_5V1s3tD1tcTes")