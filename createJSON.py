import mysql.connector as mdb
from config import *

def connectToDB():
	return mdb.connect(**configDB)
	
def testDB(name, pos, description, date):
    DBconn = connectToDB()
    queryCurs = DBconn.cursor()

    queryCurs.execute(
	'INSERT INTO Manifesto (name, pos, description, date) VALUES (%s, %s, %s, %s)', (name, pos, description, date ))

    DBconn.commit()


	
