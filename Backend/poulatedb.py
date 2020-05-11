import mysql.connector as mysql
from mysql.connector import errorcode
from csv import reader, writer
import time

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "mybookdb"
)

cursor = db.cursor()

cursor. execute("DROP DATABASE mybookdb")
cursor. execute("CREATE DATABASE mybookdb")
cursor. execute("USE mybookdb")

sqlTables = {}

sqlTables ['userTable'] = (
    "CREATE TABLE user ("
    "userID int(15) NOT NULL auto_increment," 
    "firstname varchar(60) not null,"
    "lastname varchar(60) not null,"
    "username varchar (60) not null,"
    "email VARCHAR(60) not null,"
    #"passwordSalt varchar (255) not null,"
    #"passwordHash varchar (255) not null,"
    "PRIMARY KEY(userID))")

sqlTables ['profileTable'] = (
    "CREATE TABLE profile ("
    "profileID int(15) not null,"
    "userID int(15) not null," 
    "gender varchar (10) NOT NULL,"
    "bio varchar (255) not null,"
    "school varchar (60) not null,"
    "job varchar (60) not null,"    
    "profilephoto varchar(60) NOT NULL,"
    "PRIMARY KEY(profileID, userID),"
    "FOREIGN KEY(userID) REFERENCES user(userID)) ")

sqlTables ['aboutTable'] = (
    "CREATE TABLE about("
    "aboutID int(15) not null," 
    "profileID int(15) not null,"
    "street varchar (60)," 
    "city varchar(60)," 
    "country varchar(60),"
    "DOB DATE NOT NULL," 
    "hobby varchar(60) not null,"
    "telephone varchar(60) NOT NULL,"
    "PRIMARY KEY(profileID, aboutID),"
    "FOREIGN KEY(profileID) REFERENCES profile(profileID))")

sqlTables ['photoTable'] = (
    "CREATE TABLE photo("
    "photoID int(15) NOT NULL,"
    "profileID INT(15) not null,"
    "photoLink varchar(60) not null,"
    "title varchar(60) not null,"
    "PRIMARY KEY(profileID, photoID),"
    "FOREIGN KEY(profileID) REFERENCES profile(profileID))")

sqlTables ['friendTable'] = (
    "CREATE TABLE friend("
    "profileID INT(15) not null,"
    "friendID int(15) not null,"
    "friendType varchar(60) not null,"
    "PRIMARY KEY(profileID, friendID),"
    "FOREIGN KEY(profileID) REFERENCES profile(profileID))")

sqlTables ['groupTable'] = (
    "CREATE TABLE groupTable("
    "groupID int(15) not null,"
    "groupName varchar(60) not null,"
    "groupDesc varchar(255) not null,"
    "groupCreator varchar(60) not null,"
    "creationDate DATE NOT NULL,"
    "PRIMARY KEY (groupID))")

sqlTables ['membership'] = (
    "CREATE TABLE membership("
    "groupID int (15) not null,"
    "profileID int (15) not null,"
    "memberType int (60) not null,"
    "PRIMARY KEY(profileID, groupID),"
    "FOREIGN KEY(profileID) REFERENCES profile(profileID),"
    "FOREIGN KEY(groupID) REFERENCES groupTable(groupID))")

sqlTables ['postTable'] = (
    "CREATE TABLE postTable("
    "postID INT(15) not null,"
    "text varchar(255) NOT NULL,"
    "image varchar(60) not null,"
    "postDate DATE not null,"
    "PRIMARY KEY (postID))")

sqlTables ['post'] = (
    "CREATE TABLE postrship("
    "postID INT(15) not null,"
    "profileID INT(15) not null,"
    "PRIMARY KEY (postID, profileID),"
    "FOREIGN KEY(postID) REFERENCES postTable(postID),"
    "FOREIGN KEY(profileID) REFERENCES profile(profileID))")

sqlTables ['commentTable']= (
    "CREATE TABLE commentTable("
    "commentID int (15) not null,"
    "commentDate DATE not null,"
    "text varchar(255) not null,"
    "imageLink varchar(60) not null,"
    "PRIMARY KEY(commentID))")

sqlTables ['comment'] = (
    "CREATE TABLE comment("
    "commentID int (15) not null,"
    "postID int(15) not null,"
    "PRIMARY KEY(commentID, postID),"
    "FOREIGN KEY(commentID) REFERENCES commentTable(commentID),"
    "FOREIGN KEY(postID) REFERENCES postTable(postID))")

for tableName in sqlTables:
    table = sqlTables[tableName]
    cursor.execute(table)
    print("Created Table {}: ".format(tableName),end="")


cursor.close()
db.commit()
db.close()


# userFile = open("MOCK_DATA.csv", mode = "r")
# csvReader = reader(userFile)

# for row in csvReader:
#         cursor.execute("INSERT INTO users VALUES (%s, %s, %s, %s)", (row[0], row[1], row[2], row[3]))
#         db.commit()

# cursor.execute("Select * from users")
# userdata = cursor.fetchall()

# for x in userdata:
#     print(x[3])
  