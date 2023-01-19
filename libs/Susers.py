import os
from SQL.DBConnector import Database

from dotenv import load_dotenv
load_dotenv()


class Susers():

    def __init__(self, bot):
        self.bot = bot
        
        self._db = Database(
            os.environ['SQL_USERNAME'],
            os.environ['SQL_USER_PASSWORD'],
            os.environ['SQL_DB_NAME'],
        )
        
    def send_message_level(self,user_id):
        xp_and_profil = Susers.level(self,user_id)
        
        return "Vous avex " + str(xp_and_profil[0][0]) + " et etes niveaux" + str(xp_and_profil[0][1])

    def calcul_lvl(self, lvl, xp):
        if xp >= lvl * 10:
            return True
        return False
    # function name must be an action. Level must be changed.
    def level(self, user_id):
        print (user_id)
        query = ("SELECT Profils.xp, Profils.level FROM Profils " + 
                    "INNER JOIN Users_makes_Profils ON Profils.id = Users_makes_Profils.Profils_id " + 
                    "INNER JOIN Server_has_Profils ON Profils.id = Server_has_Profils.Profils_id " + 
                    "INNER JOIN Users ON Users_makes_Profils.Users_id = Users.id " + 
                    "INNER JOIN Server ON Server_has_Profils.Server_id = Server.id " + 
                    "WHERE Server.serverId = 983809784753049611 AND Users.userId = "+ str(user_id) +";")
        
        return self._db.Select(query=query)

    def profil():
        # requete crée par ethann
        query = ("SELECT Profils.xp, Profils.level, Profils.nameColor, Profils.barColor FROM Profils"
                 "INNER JOIN Users_makes_Profils ON Profils.id = Users_makes_Profils.Profils_id"
                 "INNER JOIN Server_has_Profils ON Profils.id = Server_has_Profils.Profils_id"
                 "INNER JOIN Users ON Users_makes_Profils.Users_id = Users.id"
                 "INNER JOIN Server ON Server_has_Profils.Server_id = Server.id"
                 "WHERE Server.serverId = 983809784753049611 AND Users.userId = " + str(user_id) + ";")

    def AddXP(self, user_id):
        query = ("SELECT profils.id FROM Profils " +
                 "INNER JOIN Users_makes_Profils ON Profils.id=Users_makes_Profils.Profils_id " +
                 "INNER JOIN Server_has_Profils ON Profils.id=Server_has_Profils.Profils_id " +
                 "INNER JOIN Users ON Users_makes_Profils.Users_id=Users.id " +
                 "INNER JOIN Server ON Server_has_Profils.Server_id=Server.id " +
                 "WHERE Server.serverId=983809784753049611 AND Users.userId= " + str(user_id) +";")
        
        current_id = self._db.Select(query=query)        
        
        query = ("UPDATE Profils " +
                 "SET xp = xp + 1 " + 
                 "WHERE id = "+ str(current_id[0][0])+";")
        self._db.Modify(query=query)
        return

    def remove_xp(self, number_xp, user_id):
        # requete SQL
        return

def wallpaper(self,user_id):
    # requete crée par ethann
    query = ("SELECT Profils.xp, Profils.level, Profils.nameColor, Profils.barColor, Wallpapers.name FROM Profils " +
                "INNER JOIN Users_makes_Profils ON Profils.id = Users_makes_Profils.Profils_id " +
                "INNER JOIN Server_has_Profils ON Profils.id = Server_has_Profils.Profils_id " +
                "INNER JOIN Users ON Users_makes_Profils.Users_id = Users.id " +
                "INNER JOIN Server ON Server_has_Profils.Server_id = Server.id " +  
                "INNER JOIN Wallpapers ON Profils.Wallpapers_id = Wallpapers.id " +
                "WHERE Server.serverId = 983809784753049611 AND Users.userId = " + user_id + ";")
    return self._db.Select(query=query)
