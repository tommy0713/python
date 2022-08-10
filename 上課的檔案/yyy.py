import mysql.connector

db = mysql.connector.connect(
       host="localhost",
       user="QvQ",
       passwd="0713",
       database="AddressBook"
   )

 
sql = "select * from UserInfo"
cursor = db.cursor(dictionary=True)
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    print("帳號:{uid},姓名:{cname}".format(**row))