import mysql.connector


def DBConnector():
    mydb = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "Pa$$w0rd"
    )
    return mydb.cursor()


def ExecuteSQLRequest(request):
    
    cursor = DBConnector
    cursor.execute(request)
