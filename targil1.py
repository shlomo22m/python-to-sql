import sys
from dotenv import load_dotenv
import pandas as pd
import pyodbc
import mysql.connector
import os
from datetime import datetime
import pandas
class Targil1:
    load_dotenv()
    server=os.getenv('SERVER')
    connection = None
    mycursor = None
    file=None


    def writeToFile(self, string):
        """"date:18.1.23 name:shlomo function: write all the logs to a file"""
        os.chdir(os.getcwd())
        try:
            self.file = open("logfile.txt", "a")
            string+= datetime.now().strftime(" %d/%m/%Y %H:%M:%S\n")
            self.file.write(string)
            self.file.flush()
            self.file.close()
        except Exception as e:
            self.writeToFile("Something went wrong: " + str(e))
            print("Exception: " + str(e))
            sys.exit(1)


    def connect(self):
        test=0
        try:
            self.connection = pyodbc.connect(f'Driver=sql server native client 11.0;Server={self.server};Database=targil1;Trusted_Connection=yes;')
            self.writeToFile('connection is on')
            self.mycursor=self.connection.cursor()
            test=1
        except pyodbc.OperationalError:
            self.writeToFile('bad connection string')
            test=0
            sys.exit(1)
        #return self.mycursor
        return test


    def id(self,name1):
        try:
            self.mycursor.execute(f"SELECT ID FROM Cust where name='{name1}'")
            self.writeToFile('id query is activated')
        except pyodbc.ProgrammingError:
            self.writeToFile('bad query syntax')
        for x in self.mycursor:
            row_to_list = x[0]
            return row_to_list


    def order_list(self,id):
        sqllist = []
        try:
            self.mycursor.execute(f"SELECT sum FROM Orders where cust_id='{id}'")
            self.writeToFile('order list query is activated')
        except pyodbc.ProgrammingError:
            self.writeToFile('bad query syntax')
        for x in self.mycursor:
            sqllist.append(x[0])
        return sqllist

    def order_sum(self,orders):

        sum = 0
        for x in self.mycursor:
             print(x)
        for x in orders:
            sum += x
        print(sum)
        return sum

    def closeconnection(self):
        try:
            self.connection.close()
            self.writeToFile('connection close')
        except:
            self.writeToFile('connection is still open')


