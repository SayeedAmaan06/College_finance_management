import mysql.connector
from mysql.connector import Error

def sqlupdate():
        
        try:
            connection = mysql.connector.connect(host="localhost",user="root", password = "",database = "college_finance_db" )

            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("INSERT INTO exam_fees (`TRANSACTION _ID`) VALUES (%s)",)
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