import os
from SQL.DBconnector import Database

from dotenv import load_dotenv
load_dotenv()

class Susers():

    def __init__(self, bot):
        self.bot = bot
        """""
        self._db = Database(
            os.environ['SQL_USERNAME'],
            os.environ['SQL_USER_PASSWORD'],
            os.environ['SQL_HOSTNAME'],
        )
        """""
    # calcul lvl return boolean value. Either change function name, or return type
    def calcul_lvl(self, lvl, xp):
        if xp >= lvl * 10:
            return True
        return False

    # function name must be an action. Level must be changed.
    def level(self):
        query = 'INSERT INTO `mydb`.`users`(`id`, `userId`) value(5, "sa fonctionne")'
        self._db.Modify(query=query)
        
        
        
    def add_xp(self, number_xp, user_id):
        # requete SQL
        lvl = Susers.level(user_id)
        xp_total = NotImplemented  # requete SQL pour optenire le nombre total de XP
        if Susers.calcul_lvl(lvl, xp_total):
            NotImplemented  # requete SQL pour augmenter le niveau de 1
        return

    def remove_xp(self, number_xp, user_id):
        # requete SQL
        return
