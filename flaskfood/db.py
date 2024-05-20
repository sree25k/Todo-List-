import pymysql

#Establish connection to MySQL database
conn = pymysql.connect(
  host= 'sql6.freesqldatabase.com',
  database= 'sql6683948',
  user= 'sql6683948',
  password= 'b2xLMrJ13R',
  charset= 'utf8mb4',
  cursorclass= pymysql.cursors.DictCursor
)

#Creates a MySQL table based on the given query
cursor = conn.cursor()
sql_query = """ CREATE TABLE book (
id integer NOT NULL AUTO_INCREMENT,
food text NOT NULL,
calories integer NOT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1"""
cursor.execute(sql_query)
conn.close()