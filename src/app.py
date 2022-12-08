from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from decouple import config

config.encoding = "cp1251"

app = Flask(__name__)
mysql = MySQL()

app.config["SECRET_KEY"] = config("SECRET_KEY")
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = config("DATABASE_PWD")
app.config["MYSQL_DATABASE_HOST"] = "localhost"
app.config["MYSQL_DATABASE_DB"] = "buy_book"

mysql.init_app(app)

@app.route("/")
def index():
    data = "hello"
    return render_template("index.html", data=data)



@app.route("/login")
def login():
    # conn = mysql.connect()
    # cursor =conn.cursor()
    # cursor.execute("SELECT * from User")
    # data = cursor.fetchone()
    return render_template("login.html")


if __name__ == '__app__':
    app.run(debug=True)



