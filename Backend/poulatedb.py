import mysql.connector as mysql
from csv import reader, writer

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "mybookdb"
)

cursor = db.cursor()

# #cursor.execute("DROP TABLE IF EXISTS users")

# #cursor. execute("CREATE DATABASE mybookdb")

# #cursor.execute("CREATE TABLE users (email VARCHAR(255), userID INT(12) NOT NULL AUTO_INCREMENT PRIMARY KEY,   username varchar (255) not null, password varchar (30) not null)")

# userFile = open("MOCK_DATA.csv", mode = "r")
# csvReader = reader(userFile)

# for row in csvReader:
#         cursor.execute("INSERT INTO users VALUES (%s, %s, %s, %s)", (row[0], row[1], row[2], row[3]))
#         db.commit()

cursor.execute("Select * from users")
userdata = cursor.fetchall()

for x in userdata:
    print(x[3])
  
cursor.close()
db.commit()
db.close()


