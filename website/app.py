from flask import Flask, request, redirect, render_template
from test1 import pytest as pt
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

@app.route("/")
def upload_form():
    return render_template("home.html")
@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        image = request.files['image']
        filename = image.filename
        
        image.save(filename)
        print("uploaded")
    

    def sqlupdate():

        tnd = pt(filename)
        try:
            connection = mysql.connector.connect(host="localhost",user="root", password = "",database = "college_finance_db" )

            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("INSERT INTO exam_fees (`serial_number`, `NAME`, `USN`, `SEM`, `DEPARTMENT`, `TRANSACTION _ID`, `PAID_EXAM_FEES`, `DATE`) VALUES (' ',' ',' ',' ',' ',%s,' ',%s)",(tnd[0],tnd[1]))
                connection.commit()
                print("Record inserted successfully")

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
    sqlupdate()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
    
