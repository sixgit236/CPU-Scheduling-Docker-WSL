import flask
import mysql.connector
import os
app = flask.Flask(__name__)
def connect_to_db():
 return mysql.connector.connect(
 host=os.getenv('DB_HOST', 'database'),
 user=os.getenv('DB_USER', 'root'),
 password=os.getenv('DB_PASSWORD', 'root_password'),
 database=os.getenv('DB_NAME', 'scheduling_db')
 )
@app.route('/')
def index():
 try:
 conn = connect_to_db()
 cursor = conn.cursor()
 cursor.execute("SELECT VERSION();")
 db_version = cursor.fetchone()
 cursor.close()
 conn.close()
 return f"Connected to MySQL Successfully! Database Version: {db_version[0]}"
 except Exception as e:
 return f"Database Connection Failed: {str(e)}"
if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)
