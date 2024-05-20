#Imports for various plugins/dependencies
from datetime import datetime
from flask import Flask, render_template, url_for, flash, request, jsonify, redirect
from forms import inputData
import pymysql


#Initilizing object
app = Flask(__name__)
app.config['SECRET_KEY'] = 'bSRQRwkQHl'

#Connecting to database
def db_connection():
  conn = None
  try:
    conn = pymysql.connect(host= 'sql6.freesqldatabase.com',
                            database= 'sql6683948',
                            user= 'sql6683948',
                            password= 'b2xLMrJ13R',
                            charset= 'utf8mb4',
                            cursorclass= pymysql.cursors.DictCursor)
  except pymysql.Error as e:
    print(e)
  return conn



#Counts up total calories by going through the database
def count():
  conn = db_connection()
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM book")
  cal_tol = 0
  for row in cursor.fetchall():
    cal_tol += row['calories']
  conn.close()
  return cal_tol

#REST API operations for homepage
@app.route("/", methods = ['GET','POST','DELETE'])
@app.route("/home", methods = ['GET','POST','DELETE'])
def home():
  nutr = inputData()
  conn = db_connection()
  cursor = conn.cursor()

  if request.method == 'GET':
    cursor.execute("SELECT * FROM book")
    nutrition = [
      dict(id=row['id'],food = row['food'], calories = row['calories'])
      for row in cursor.fetchall()
    ]
    if nutrition is not None:
      return render_template('home.html', title = "Today", nutr = nutr, nutrition=nutrition,goal=2000,total_calories = count())
  
  if request.method == 'POST':
    newfood = request.form['food']
    newcal = request.form['calories']
    sql = """INSERT INTO book (food, calories) VALUES (%s, %s)"""
    cursor = cursor.execute(sql, (newfood, newcal))
    conn.commit()
    flash("Added!")
    return redirect('/home')
  

@app.route("/home/<int:id>", methods = ['GET'])
def delete(id):
  conn = db_connection()
  cursor = conn.cursor()

  sql = """DELETE FROM book WHERE id=%s"""
  cursor = cursor.execute(sql, (id))
  conn.commit()
  flash("Item has been removed")
  return redirect('/home')


#REST API operations for history page
@app.route("/history")
def history():
  return render_template('history.html', title = "History")

#Run method on app object
if __name__ == "__main__":
  app.run(debug=True)
