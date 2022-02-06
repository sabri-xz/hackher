
from flask import Flask, render_template, request, session
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import math
import time
import psycopg2
import os
import sqlite3


# the app we use to manage the routes and run the app
app = Flask(__name__)
app.secret_key = "gotti"
# main homepage of the website
@app.route('/', methods=['GET'])
def home():
    con = sqlite3.connect('girlboss.db')
    cur = con.cursor()
    #if not session['uname']:
    #    return render_template("login.html")
    #else:   
    return render_template("index.html")  
@app.route('/login', methods=['GET', 'POST'])
def login():
    con = sqlite3.connect('girlboss.db')
    cur = con.cursor()
    if request.method=='GET':
        return render_template("login.html")  
    session['uname'] = request.args.get('uname')
    session['pwd'] = generate_password_hash(request.args.get('pwd'))
    session['plant'] = request.args.get('plant')
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
        username TEXT NOT NULL PRIMARY KEY,
        password TEXT NOT NULL,
        plant INTEGER NOT NULL
        );
        """)
    cur.execute("SELECT * FROM users WHERE uname=?", (session['uname'],))
    user = cur.fetchone()
    if user is None:
        cur.execute("""
        INSERT INTO users(username, password, plant)
        VALUES (%s, %s, %s)
        """, (session['uname'], generate_password_hash(session['pwd']), session['plant']))
    elif check_password_hash(session['pwd'], user[2]):
        con.commit()
        con.close()
        return render_template("index.html")
    con.commit()
    con.close()
    return render_template("index.html")  

@app.route('/logout', methods = ['GET'])
def logout():
    session.clear()
    return render_template("login.html")

# runs our app using Flask
if __name__ == "__main__":
    app.run(debug = True)
