import discord
from user import * 


bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.event
async def on_message(message):
    user.lol()

bot.run("MTA0MzA3ODk4MTA5MzY5NTUzOQ.GIEHVb.p_ktQhqcrRxa-ZcDYkbZtVs-_5V1s3tD1tcTes")