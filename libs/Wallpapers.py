import os
from SQL.DBConnector import Database

from dotenv import load_dotenv
load_dotenv()

class Wallpapers():
    
    def __init__(self, bot):
        self.bot = bot

        self._db = Database(
            os.environ['SQL_USERNAME'],
            os.environ['SQL_USER_PASSWORD'],
            os.environ['SQL_DB_NAME'],
        )


    def user_have_wallpapers(self,user_id):
        query= ("SELECT Wallpapers.name FROM Profils " +
                "INNER JOIN Users_makes_Profils ON Profils.id=Users_makes_Profils.Profils_id " +
                "INNER JOIN Server_has_Profils ON Profils.id=Server_has_Profils.Profils_id" +
                "INNER JOIN Users ON Users_makes_Profils.Users_id=Users.id " +
                "INNER JOIN Server ON Server_has_Profils.Server_id=Server.id " +
                "INNER JOIN Profils_has_Wallpapers ON Profils_has_Wallpapers.Profils_id=Profils.id " +
                "INNER JOIN Wallpapers ON Wallpapers.id=Profils_has_Wallpapers.Wallpapers_id " + 
                "WHERE Server.serverId=1042740561909653535 AND Users.userId=" + user_id + ";")
        return self._db.Select(query=query)
    
    def wallpaper(self, user_id):
            # requete crée par ethann
        query = ("SELECT Profils.xp, Profils.level, Profils.nameColor, Profils.barColor, Wallpapers.name FROM Profils " +
                "INNER JOIN Users_makes_Profils ON Profils.id = Users_makes_Profils.Profils_id " +
                "INNER JOIN Server_has_Profils ON Profils.id = Server_has_Profils.Profils_id " +
                "INNER JOIN Users ON Users_makes_Profils.Users_id = Users.id " +
                "INNER JOIN Server ON Server_has_Profils.Server_id = Server.id " +
                "INNER JOIN Wallpapers ON Profils.Wallpapers_id = Wallpapers.id " +
                "WHERE Server.serverId = 983809784753049611 AND Users.userId = " + user_id + ";")
        return self._db.Select(query=query)
            

