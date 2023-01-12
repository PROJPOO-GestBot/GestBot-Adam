import os
import discord
from libs.Susers import Susers
from SQL.DBconnector import Database

from dotenv import load_dotenv
load_dotenv()


class Users(discord.Cog):

    def __init__(self, bot):
        self.bot = bot
        
        self._db = Database(
            os.environ['SQL_USERNAME'],
            os.environ['SQL_USER_PASSWORD'],
            os.environ['SQL_HOSTNAME'],
        )
        
    @discord.Cog.listener()
    async def on_message(self, message):
        await Susers.AddXP(1, message.author.id)

    @discord.slash_command(name="level", description="donne le niveaux du compte discord")
    async def level(self, ctx):
        await ctx.send(Susers.level(self))

    @discord.slash_command(name="supprimer", description="supprime une certaine quantiter de XP")
    async def supprimer(self, ctx, message):
        await ctx.send(Susers.RemoveXP)


def setup(bot):
    bot.add_cog(Users(bot))
