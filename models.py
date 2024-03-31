import mysql.connector

db=mysql.connector.connect(
    user='root',
    password='7519', 
    db='azure_db', 
    host= '127.0.0.1'
)


cursor= db.cursor()


cursor.execute("""
        CREATE TABLE IF NOT EXISTS signup (
    UID INT AUTO_INCREMENT PRIMARY KEY,
    Fsname VARCHAR(255) NOT NULL,
    Lsname VARCHAR(255) NOT NULL,
    EmailID VARCHAR(255) NOT NULL,
    PassW VARCHAR(255) NOT NULL
);

               """)


def add_signup(Fsname,Lsname,EmailID,PassW):
    sql2 = "INSERT INTO signup (Fsname,Lsname,EmailID,PassW) VALUES (%s, %s, %s, %s)"
    val2 = (Fsname,Lsname,EmailID,PassW)
    cursor.execute(sql2,val2)
    db.commit()




cursor.execute("""
        CREATE TABLE IF NOT EXISTS contc (
    Cname VARCHAR(255) NOT NULL,
    em_ID VARCHAR(255) NOT NULL,
    MsgC VARCHAR(255) NOT NULL
);

               """)

def add_contc(Cname,em_ID,MsgC):
    sql3 = "INSERT INTO contc (Cname,em_ID,MsgC) VALUES (%s, %s, %s)"
    val3 = (Cname,em_ID,MsgC)
    cursor.execute(sql3,val3)
    db.commit()

cursor.execute("""       
     CREATE TABLE IF NOT EXISTS Products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prd_img longblob,
    prd_name VARCHAR(255),
    prd_des TEXT,
    prd_prc DECIMAL(10, 2)
);
            """)

def add_products(prd_img,prd_name,prd_des,prd_prc):
    sql4 = "INSERT INTO products (prd_img, prd_name, prd_des, prd_prc) VALUES (%s, %s, %s, %s)"
    val4 = (prd_img,prd_name,prd_des,prd_prc)
    cursor.execute(sql4,val4)
    db.commit()


cursor.execute("""       
  CREATE TABLE IF NOT EXISTS payment (
    OrdId INT AUTO_INCREMENT PRIMARY KEY,
    cusNm VARCHAR(255),
    phNum BIGINT,
    adrs TEXT,
    quantity INT,
    price FLOAT
);
 
                """)

def add_payment(cusNm,phNum,adrs,quantity,price):
    sql4 = "INSERT INTO payment (cusNm,phNum,adrs,quantity,price) VALUES (%s, %s, %s, %s, %s)"
    val4 = (cusNm,phNum,adrs,quantity,price)
    cursor.execute(sql4,val4)
    db.commit()
