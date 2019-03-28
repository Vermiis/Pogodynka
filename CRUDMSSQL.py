import pymssql
import configparser
config = configparser.RawConfigParser()
config.read('config.ini')

hostname = config['DEFAULT']['ServerName']


#przyklad z neta, trzeba rozbic na funckje  :)

conn = pymssql.connect(host=hostname, user='usrnm', password='passwd', Database='mydb')
cur = conn.cursor()

#CREATE , INSERT , UPDATE, SELECT always use execute command
cur.execute('CREATE TABLE test(id INT, name VARCHAR(100))')
cur.execute("INSERT INTO test(id,name) VALUES('3','mahendra')")
cur.execute("UPDATE test set name='rony' where id='1'")
cur.execute("DELETE from test where id='1'")
conn.commit() # don't forget to commit after manipulating database

#To retrieve data / select you can do this
cur.execute('SELECT * from test')
row = cur.fetchone()

while row:
      #Index column fields in database always from 0
      print (row[0],row[1])
      row = cur.fetchone()

conn.close() #don't forget close connection after all process CRUD complete
