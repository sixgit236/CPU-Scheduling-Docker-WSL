from flask import Flask, render_template_string
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    try:
        db = mysql.connector.connect(host="database", user="root", password="root_password", database="scheduler_db")
        db_status = "Connected to MySQL Successfully!"
        db.close()
    except:
        db_status = "Database Connection Pending..."
    
    return render_template_string("<h1>CPU Project</h1><p>{{ s }}</p>", s=db_status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
