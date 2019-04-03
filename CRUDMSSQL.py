import pymssql
import configparser
config = configparser.RawConfigParser()
config.read('config.ini')

hostname = config['DEFAULT']['ServerName']



class CRUDMSSQL:
      def __init__(self):
            self.connection = ""
            self.cursor1 = ""


      def ExecuteQuery(self, query):
            cur = self.cursor1()
            cur.execute(query)
            self.connection.commit
            self.connection.close()

      def setConnection(self, hostname, usrname, pwd, dbname):
            self.connection = pymssql.connect(host=hostname, user='usrnm', password='passwd', Database='mydb')

      def ExecuteSelect(self, selectq):
            cur = self.cursor1()
            cur.execute(selectq)
            row = cur.fetchone()
            while row:
      #Index column fields in database always from 0
                   print (row[0],row[1])
                   row = cur.fetchone()
            self.connection.close()

