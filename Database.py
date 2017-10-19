'''
Created on Oct 14, 2017

@author: Tyler-OC
'''
import sqlite3

class Database:
    conn = sqlite3.connect('./database/Aqua.db')
    c = conn.cursor()
    
    def getProducts(self):
        data = []
        self.c.execute("Select * from Products")
        for row in self.c.fetchall():
            data.append(row[1])
        print(data)
    
    def newProduct(self, Title, url):
        query = "INSERT INTO Products VALUES(NULL, '%s', '%s')" % (Title, url,)
        print(query)
        self.c.execute(query)
        self.conn.commit()
        
    def CheckProduct(self, Title):
        query = "Select Title from Products where Title = '%s'" % (Title,)
        count = 0
        for x in self.c.execute(query):
            count += 1
        if count >= 1:
            return True
        else:
            return False
