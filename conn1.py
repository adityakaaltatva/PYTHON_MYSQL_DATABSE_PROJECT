
import mysql.connector

import csv
def cs():
    with open('BUG1.csv', 'r')as file:
        next(file)
        csvfile = csv.reader(file)
        for lines in csvfile:
                print(lines)
                #exit()
            
                connect(lines)
            
def connect(row):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            user='root',
                                            password='',
                                            port=3306,
                                            database="bscit"
                                            )

        
        mySql_Create_Table_Query = """CREATE TABLE IF NOT EXISTS Sheet( 
                            
                                Name varchar(250) NOT NULL,
                                certificate varchar(250) NOT NULL,
                                
                                Sap_ID int(12) NOT NULL) """
        cursor = connection.cursor()
        cursor.execute(mySql_Create_Table_Query)
        print(" Table created successfully ")
        sql=f"INSERT INTO Sheet(Name,certificate,Sap_ID) VALUES('{row[1]}','{row[2]}',{row[3]})"
        cursor.execute(sql)
        connection.commit()
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

cs()






   