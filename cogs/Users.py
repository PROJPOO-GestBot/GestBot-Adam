import os
import discord
from libs.Lusers import Lusers
from SQL.DBConnector import Database

from dotenv import load_dotenv
load_dotenv()


class Users(discord.Cog):

    def __init__(self, bot):
        self.bot = bot
        
        self._db = Database(
            os.environ['SQL_USERNAME'],
            os.environ['SQL_USER_PASSWORD'],
            os.environ['SQL_DB_NAME'],
        )
        
    @discord.Cog.listener()
    async def on_message(self, message):
        Lusers.add_xp(self, message.author.id, message.server.id)

    @discord.slash_command(name="level", description="donne le niveaux du compte discord")
    async def level(self,ctx):
        await ctx.send(Lusers.send_message_level(self, ctx.author.id))

    @discord.slash_command(name="supprimer", description="supprime une certaine quantiter de XP")
    async def supprimer(self, ctx, message):
        await ctx.send(Lusers.remove_xp, message)

def setup(bot):
    bot.add_cog(Users(bot))
