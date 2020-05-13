from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/p.html', methods = ['POST'])
def getUserInfo():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    return render_template('p.html',firstname = firstname,username = username)



if __name__ == "__main__":
    app.run(debug=True)