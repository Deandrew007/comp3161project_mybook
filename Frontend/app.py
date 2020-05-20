from flask import Flask, render_template, request
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


cursor.execute("Select * from profile WHERE userID = 10")
profileData = cursor.fetchall()
cursor.execute("Select * from user WHERE userID = 10")
userData = cursor.fetchall()


bioList = []
schoolList = []
jobList = []
for x in profileData:
    bioList.append(x[3])
    schoolList.append(x[4])    
    jobList.append(x[5])

fnameList = []
lnameList = []
for i in userData:
    fnameList.append(i[2])
    lnameList.append(i[3])




cursor.close()
db.close()


app = Flask(__name__, template_folder='templates')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/', methods = ['POST'])
# def getUserInfo():
#     firstname = request.form['firstname']
#     lastname = request.form['lastname']
#     username = request.form['username']
#     email = request.form['email']
#     password = request.form['password']
#     return render_template('profile.html',firstname = firstname,username = username)

@app.route('/')
def profile():
    return render_template('p.html', firstname=fnameList[0], lastname=lnameList[0], job = jobList[0], bio = bioList[0], school = schoolList[0])

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)