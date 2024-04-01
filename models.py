import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('Azure_db.db')
cursor = conn.cursor()


cursor.execute("""
  CREATE TABLE IF NOT EXISTS "signup" (
	"UID"	INTEGER,
	"Fsname"	VARCHAR(255) NOT NULL,
	"Lsname"	VARCHAR(255) NOT NULL,
	"EmailID"	VARCHAR(255) NOT NULL,
	"PassW"	VARCHAR(255) NOT NULL,
	PRIMARY KEY("UID" AUTOINCREMENT)
);
               """)


def add_signup(Fsname,Lsname,EmailID,PassW):
    conn = sqlite3.connect('Azure_db.db')
    cursor = conn.cursor()
    if conn:
      sql2 = "INSERT INTO signup (Fsname,Lsname,EmailID,PassW) VALUES (? , ? , ? , ?)"
      val2 = (Fsname,Lsname,EmailID,PassW)
      cursor.execute(sql2,val2)
      conn.commit()

    else:
        print("Database connection error")


cursor.execute("""
CREATE TABLE IF NOT EXISTS "contc" (
	"Cname"	VARCHAR(255) NOT NULL,
	"em_ID"	VARCHAR(255) NOT NULL,
	"MsgC"	VARCHAR(255) NOT NULL
);
               """)

def add_contc(Cname,em_ID,MsgC):
    conn = sqlite3.connect('Azure_db.db')
    cursor = conn.cursor()
    if conn:
      sql3 = "INSERT INTO contc (Cname,em_ID,MsgC) VALUES (?, ?, ?)"
      val3 = (Cname,em_ID,MsgC)
      cursor.execute(sql3,val3)
      conn.commit()
    else:
        print("Database connection error")
    

cursor.execute("""       
  CREATE TABLE IF NOT EXISTS "Products" (
	"id"	INTEGER,
	"prd_img"	BLOB,
	"prd_name"	varchar(255),
	"prd_des"	TEXT,
	"prd_prc"	decimal(10,2),
	PRIMARY KEY("id" AUTOINCREMENT)
);
  
                 """)

def add_products(prd_img,prd_name,prd_des,prd_prc):
    conn = sqlite3.connect('Azure_db.db')
    cursor = conn.cursor()
    if conn:
      sql4 = "INSERT INTO products (prd_img, prd_name, prd_des, prd_prc) VALUES (?, ?, ?, ?)"
      val4 = (prd_img,prd_name,prd_des,prd_prc)
      cursor.execute(sql4,val4)
      conn.commit()
    else:
        print("Database connection error")


cursor.execute("""       
  CREATE TABLE IF NOT EXISTS "payment" (
	"OrdId"	INTEGER,
	"cusNm"	varchar(255),
	"phNum"	INTEGER,
	"adrs"	TEXT,
	"quantity"	INTEGER,
	"price"	REAL,
	PRIMARY KEY("OrdId" AUTOINCREMENT)
);
 
                """)

def add_payment(cusNm,phNum,adrs,quantity,price):
    conn = sqlite3.connect('Azure_db.db')
    cursor = conn.cursor()
    if conn:
      sql4 = "INSERT INTO payment (cusNm,phNum,adrs,quantity,price) VALUES (?, ?, ?, ?, ?)"
      val4 = (cusNm,phNum,adrs,quantity,price)
      cursor.execute(sql4,val4)
      conn.commit()
    else:
        print("Database connection error")

conn.close()