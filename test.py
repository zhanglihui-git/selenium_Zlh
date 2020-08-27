import mysql as mysql

conn = mysql.connector.connect(user='managecenter', password='8j8ZBNsec8B@bwpu', database='10.190.233.182:3306/managecenter')
cursor = conn.cursor()
cursor.execute('show tables')