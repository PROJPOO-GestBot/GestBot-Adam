import discord



bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.send("sus!")

@bot.slash_command(name = "test", description = "rwar")
async def test(ctx):
    await ctx.send("testFonctionnnelle")

@bot.event
async def on_message():
    










bot.run("MTA0MzA3ODk4MTA5MzY5NTUzOQ.GIEHVb.p_ktQhqcrRxa-ZcDYkbZtVs-_5V1s3tD1tcTes")