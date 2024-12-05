import sqlite3
con = sqlite3.connect("lecture.db")
cur = con.cursor()

#sql = "select * from student"                      # showing nothing in database
#result = cur.execute(sql)
#print (f" first row: {result.fetchone()}")

sql = "insert into student values ('mary', 'SD', 'Female')"
cur.execute(sql)
con.commit()                                        # need to commit to save the changes

#sql = "select * from student"                       # showing values
#result = cur.execute(sql)
#print (f" first row: {result.fetchone()}")


con.close()