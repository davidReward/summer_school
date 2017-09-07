import mysql.connector as mdb
from config import *

def connectToDB():
	return mdb.connect(**configDB)
	
def writeDB(name, pos, description, date):
    DBconn = connectToDB()
    queryCurs = DBconn.cursor()

    queryCurs.execute(
	'INSERT INTO Manifesto (name, pos, description, date) VALUES (%s, %s, %s, %s)', (name, pos, description, date ))

    DBconn.commit()


def readDB(name):
    DBconn = connectToDB()
    # This enables column access by name: row['column_name']
    # DBconn.row_factory = sqlite3.Row
    queryCurs = DBconn.cursor(dictionary=True)

    queryCurs.execute(
        'SELECT name, pos, description, date '
        'FROM Manifesto '
        'WHERE name LIKE %s; ', (name,))

    row = queryCurs.fetchall()
    row_json = [dict(rec) for rec in row]

    DBconn.close()
    return row_json


	
