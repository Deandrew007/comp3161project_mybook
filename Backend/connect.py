import mysql.connector as mysql
from mysql.connector import errorcode
import time

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "mybookdb"
)

cursor = db.cursor()


cursor.execute("Select * from profile")
proifleData = cursor.fetchall()

for x in proifleData:
    print(x[3])

cursor.close()
db.close()