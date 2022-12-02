import discord
from users import * 


bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.event
async def on_message(message):
    users.AddXP(1, message.author.id)


@bot.slash_command(name = "level", description = "donne le niveaux du compte discord")
async def level(ctx):
    await ctx.send(users.LevelXP)

@bot.slash_command(name = "supprimer", description = "supprime une certaine quantiter de XP")
async def supttrimer(ctx, message):
    await ctx.send(users.RemoveXP)

bot.run("MTA0MzA3ODk4MTA5MzY5NTUzOQ.GIEHVb.p_ktQhqcrRxa-ZcDYkbZtVs-_5V1s3tD1tcTes")