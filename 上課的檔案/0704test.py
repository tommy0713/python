import pymysql

db = pymysql.connect(host='127.0.0.1', user='QvQ',
                     passwd='19950713', database='mdu')

cursor = db.cursor()
sql="insert in to account (name,account,password,priority) values ('qqq','aaa','zzz','2')"

cursor.execute(sql)
db.commit()
db.close()