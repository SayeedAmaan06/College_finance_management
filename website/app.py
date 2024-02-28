from flask import Flask, request, redirect, render_template
from test1 import pytest as pt
import mysql.connector
from mysql.connector import Error
from amount import recognize_text as rt

app = Flask(__name__)

@app.route("/")
def upload_form():
    return render_template("home.html")
@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        usn = request.form['usn']
        image = request.files['image']
        filename = image.filename
        image.save(filename)
        print("uploaded")
    

    def sqlupdate():

        tnd = pt(filename)
        amt = rt(filename)
        fetched_data = None
        try:
            connection = mysql.connector.connect(host="localhost",user="root", password = "",database = "college_finance_db" )

            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
               # Fetch the data from the 'college_and_hostel_fees' table
                cursor.execute("SELECT NAME,BRANCH,SEM FROM college_and_hostel_fees WHERE USN= %s",(usn,))
                fetched_data = cursor.fetchone()
                # Insert the fetched data into the 'exam_fees' table
                cursor.execute("INSERT INTO exam_fees (`serial_number`,`NAME`,`USN`,`DEPARTMENT`, `SEM`,`TRANSACTION _ID`, `PAID_EXAM_FEES`, `DATE`) VALUES (' ', %s, %s, %s, %s,%s,%s,%s)",(fetched_data[0],usn,fetched_data[1],fetched_data[2],tnd[0],amt,tnd[1]))
                connection.commit()
                print("Record inserted successfully")
                print(tnd)
                print(usn)
                print(fetched_data)

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
    
