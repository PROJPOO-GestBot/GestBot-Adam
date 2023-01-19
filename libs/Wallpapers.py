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
