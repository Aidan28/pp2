import psycopg2
  

DB_NAME = "ndmsevnj"
DB_USER = "ndmsevnj"
DB_PASS = "WVw5AttKjdyH1pi9oWUVk2MexhoXAoF2"
DB_HOST = "queenie.db.elephantsql.com"
DB_PORT = "5432"


conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password = DB_PASS,
                            host = DB_HOST, port = DB_PORT)
    
print("Database connected successfully")

cur = conn.cursor()
cur.execute("""

CREATE TABLE employe
(
    ID INT PRIMARY KEY NOT NULL, 
    NAME TEXT NOT NULL,
    EMAIL TEXT NOT NULL
)

""")

conn.commit()
print("Database created successfully")
