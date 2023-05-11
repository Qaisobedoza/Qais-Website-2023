from flask import Flask, render_template, g
import sqlite3

DATABASE = 'database.db'
#initiliaze the app
app = Flask(__name__)



def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    cursor = get_db().cursor()
    sql = "SELECT * FROM case_information;"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('index.html', results = results)

if __name__=='__main__':
    app.run(debug=True)