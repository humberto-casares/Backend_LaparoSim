import mysql.connector
from datetime import datetime
import random
import string

class Database:
    def __init__(self):
        self.host="localhost"
        self.user="root"
        self.passwd="LabPro!23"
        self.database="sistemaweb"
        
    def run_query(self, query, flag):
        connection = None  # Initialize the connection variable
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.passwd,
                database=self.database
            )
            mycursor = connection.cursor()
            mycursor.execute(query)
            if flag == 0:
                res = mycursor.fetchall()
            elif flag == 1:
                res = 1
            return res
        except Exception as e:
            print("Insertion Error: ", e)
            return e
        finally:
            if connection is not None:
                connection.commit()
                connection.close()
            
    def getData(self, id):
        qr = "SELECT * FROM data WHERE userKey ='"+id+"';"
        print("Query: ", qr)
        res=self.run_query(qr, 0)
        
        return res  

    def assignActivity(self, idMember, idAdmin, idPoll):
        qr="INSERT INTO assign_act_users(acu_user)VALUES('{idMember}')".format(idMember=idMember,)
        res=self.run_query(qr, 1)
        return res
    
    def now_datetime(self):
        now_datetime = datetime.now()
        return now_datetime.strftime('%Y-%m-%d %H:%M:%S')

    def generate_token(self):
        # get random string of letters and digits
        src = string.ascii_letters + string.digits
        token = ''.join((random.choice(src) for i in range(14)))
        return token
        
'''
obj = Database()
data=obj.getData("2")
print(data)
'''