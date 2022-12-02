import discord
from libs.Susers import Susers

class Users(discord.Cog):
    def __init__(self, bot) -> None:
        self._bot = bot
        
    @discord.Cog.listener()
    async def on_message(self, message):
        Susers.AddXP(1, message.author.id)


    @discord.slash_command(name = "level", description = "donne le niveaux du compte discord")
    async def level(self, ctx):
        await ctx.send(Susers.LevelXP)

    @discord.slash_command(name = "supprimer", description = "supprime une certaine quantiter de XP")
    async def supprimer(self, ctx, message):
        await ctx.send(Susers.RemoveXP)
        
        
        
def setup(bot):
    bot.add_cog(Users(bot))