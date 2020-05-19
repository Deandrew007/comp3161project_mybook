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


cursor.execute("Select * from profile WHERE profileID = 10")
profileData = cursor.fetchall()

profileList = []
imageList = []
for x in profileData:
    profileList.append(x[5])
    print(profileList)


cursor.close()
db.close()


app = Flask(__name__, template_folder='templates')

name = 'DrewDon'

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
    return render_template('p.html', firstname=name, job = profileList[0])



if __name__ == "__main__":
    app.run(debug=True)