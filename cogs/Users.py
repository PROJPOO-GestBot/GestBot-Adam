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
        Lusers.add_xp(self, message.author.id, message.guild.id)

    @discord.slash_command(name="level", description="donne le niveaux du compte discord")
    async def level(self,ctx):
        xp_and_level = Lusers.level(self, ctx.author.id, ctx.guild.id)
        await ctx.send(print("Vous avez : " + str(xp_and_level[0][0]) + "Xp et etes niveaux : " + str(xp_and_level[0][1])))

    @discord.slash_command(name="supprimer", description="supprime une certaine quantiter de XP")
    async def supprimer(self, ctx, message):
        await ctx.send(Lusers.remove_xp, message)

def setup(bot):
    bot.add_cog(Users(bot))
