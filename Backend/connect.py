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


cursor.execute("Select * from profile WHERE profileID >= 10 and profileID <= 20")
profileData = cursor.fetchall()

jobList = []
for x in profileData:
    print (x)

cursor.close()
db.close()