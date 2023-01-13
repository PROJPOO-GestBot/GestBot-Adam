import os
from SQL.DBConnector import Database

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
    def level(self, user_id):
        #requete crée par ethann
        query = '''SELECT Profils.xp, Profils.level, Profils.nameColor, Profils.barColor FROM Profils
                    INNER JOIN Users_makes_Profils ON Profils.id = Users_makes_Profils.Profils_id
                    INNER JOIN Server_has_Profils ON Profils.id = Server_has_Profils.Profils_id
                    INNER JOIN Users ON Users_makes_Profils.Users_id = Users.id
                    INNER JOIN Server ON Server_has_Profils.Server_id = Server.id
                    WHERE Server.serverId = 983809784753049611 AND Users.userId = 386200134628671492; '''
        return self._db.Select(query=query)

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

def wallpeper(self):
    # requete crée par ethann
    query = '''SELECT Profils.xp, Profils.level, Profils.nameColor, Profils.barColor, Wallpapers.name FROM Profils 
                INNER JOIN Users_makes_Profils ON Profils.id = Users_makes_Profils.Profils_id
                INNER JOIN Server_has_Profils ON Profils.id = Server_has_Profils.Profils_id
                INNER JOIN Users ON Users_makes_Profils.Users_id = Users.id
                INNER JOIN Server ON Server_has_Profils.Server_id = Server.id
                INNER JOIN Wallpapers ON Profils.Wallpapers_id = Wallpapers.id
                WHERE Server.serverId = 983809784753049611 AND Users.userId = 386200134628671492; '''
    return self._db.Select(query=query)
