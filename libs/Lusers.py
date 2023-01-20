import os
from SQL.DBConnector import Database

from dotenv import load_dotenv
load_dotenv()


class Lusers():

    def __init__(self):        
        self._db = Database(
            os.environ['SQL_USERNAME'],
            os.environ['SQL_USER_PASSWORD'],
            os.environ['SQL_DB_NAME'],
        )

    def calcul_lvl(self, lvl, xp):
        if xp >= lvl * 10:
            return True
        return False
    
    def level(self, user_id, server_id):
        query = ("SELECT Profils.xp, Profils.level FROM Profils " + 
                "INNER JOIN Users_makes_Profils ON Profils.id = Users_makes_Profils.Profils_id " + 
                "INNER JOIN Server_has_Profils ON Profils.id = Server_has_Profils.Profils_id " + 
                "INNER JOIN Users ON Users_makes_Profils.Users_id = Users.id " + 
                "INNER JOIN Server ON Server_has_Profils.Server_id = Server.id " + 
                "WHERE Server.serverId = " + str(server_id) + " AND Users.userId = "+ str(user_id) +";")
        
        return self._db.select(query=query)

    def get_profil(self, user_id, server_id):
        query = ("SELECT Profils.xp, Profils.level, Profils.nameColor, Profils.barColor FROM Profils"
                 "INNER JOIN Users_makes_Profils ON Profils.id = Users_makes_Profils.Profils_id"
                 "INNER JOIN Server_has_Profils ON Profils.id = Server_has_Profils.Profils_id"
                 "INNER JOIN Users ON Users_makes_Profils.Users_id = Users.id"
                 "INNER JOIN Server ON Server_has_Profils.Server_id = Server.id"
                 "WHERE Server.serverId = " + str(server_id) + " AND Users.userId = " + str(user_id) + ";")

    def add_xp(self, user_id, server_id, xp=1):
        query = ("SELECT profils.id FROM Profils " +
                 "INNER JOIN Users_makes_Profils ON Profils.id=Users_makes_Profils.Profils_id " +
                 "INNER JOIN Server_has_Profils ON Profils.id=Server_has_Profils.Profils_id " +
                 "INNER JOIN Users ON Users_makes_Profils.Users_id=Users.id " +
                 "INNER JOIN Server ON Server_has_Profils.Server_id=Server.id " +
                 "WHERE Server.serverId = " + str(server_id) + " AND Users.userId= " + str(user_id) +";")
        
        current_id = self._db.select(query=query)        
        
        query = ("UPDATE Profils " +
                 "SET xp = xp + " + str(xp) + 
                 "WHERE id = "+ str(current_id[0][0])+";")
        self._db.modify(query=query)
        return

    def remove_xp(self, number_xp, user_id):
        return

    def add_users(self, user_id):
        query = ("SELECT * FROM gestbot.users " +
                 "WHERE userId="+ str(user_id) +";")
        if self._db.select(query=query) == None:
            NotADirectoryError
            #crée profil pour new user
            
    def user_have_wallpapers(self,user_id, server_id):
            query = ("SELECT Wallpapers.name FROM Profils " +
                    "INNER JOIN Users_makes_Profils ON Profils.id=Users_makes_Profils.Profils_id " +
                    "INNER JOIN Server_has_Profils ON Profils.id=Server_has_Profils.Profils_id" +
                    "INNER JOIN Users ON Users_makes_Profils.Users_id=Users.id " +
                    "INNER JOIN Server ON Server_has_Profils.Server_id=Server.id " +
                    "INNER JOIN Profils_has_Wallpapers ON Profils_has_Wallpapers.Profils_id=Profils.id " +
                    "INNER JOIN Wallpapers ON Wallpapers.id=Profils_has_Wallpapers.Wallpapers_id " + 
                    "WHERE Server.serverId = " + str(server_id) + " AND Users.userId=" + user_id + ";")
            return self._db.select(query=query)
        
    def wallpapers(self, user_id, server_id):
        query = ("SELECT Profils.xp, Profils.level, Profils.nameColor, Profils.barColor, Wallpapers.name FROM Profils " +
                "INNER JOIN Users_makes_Profils ON Profils.id = Users_makes_Profils.Profils_id " +
                "INNER JOIN Server_has_Profils ON Profils.id = Server_has_Profils.Profils_id " +
                "INNER JOIN Users ON Users_makes_Profils.Users_id = Users.id " +
                "INNER JOIN Server ON Server_has_Profils.Server_id = Server.id " +
                "INNER JOIN Wallpapers ON Profils.Wallpapers_id = Wallpapers.id " +
                "WHERE Server.serverId = " + str(server_id) + " AND Users.userId = " + user_id + ";")
        return self._db.select(query=query)