from flask import Flask, render_template, request, session, redirect, jsonify
from models import *
import pymysql
import base64
import sqlite3


app=Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('Azure_db.db')
    return conn

users = []

#USER REGISTER
@app.route("/")
def sign():
    return render_template('homePg.html')

@app.route('/signing', methods=['POST'])
def signing():
    global user_count
    if request.method == "POST":
        Fsname = request.form['Fsname']
        Lsname = request.form['Lsname']
        EmailID = request.form['EmailID']
        PassW = request.form['PassW']
        add_signup(Fsname, Lsname, EmailID, PassW)
        users.append({'Fsname': Fsname, 'Lsname': Lsname, 'EmailID': EmailID})
        user_count = len(users)
        return render_template('homePg.html', user_count=user_count)
    else:
        return "Method Not Allowed", 405



@app.route('/home')
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    u_id= request.args.get('u_id')
    cursor.execute("select * from signup where UID=?", (u_id,))
    user = cursor.fetchone()
    cursor.close()  
    conn.close()  
    return render_template("homePg.html", user=user)

@app.route('/UserL')
def UserL():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("select * from signup")
    cus=cursor.fetchall()
    return render_template("/admin/UM.html",cus=cus)


#User Login
@app.route('/loging', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'EmailID' in request.form and 'PassW' in request.form:
        EmailID = request.form['EmailID']
        PassW = request.form['PassW']
        conn = sqlite3.connect('Azure_db.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM signup WHERE EmailID = ? AND PassW = ?', (EmailID, PassW))
        user = cursor.fetchone()


        conn.commit()
        conn.close()

        if user:
            return render_template('homePg.html', user=user)
        else:
            return 'NOT A MEMBER'
    
    return render_template('homePg.html')
 

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('Uname', None)
    session.pop('emailID', None)
    return render_template('/homePg.html')

#Contact Info
@app.route('/contact', methods=['POST'])
def contact():
    if request.method == "POST":
        Cname = request.form['Cname']
        em_ID = request.form['em_ID']
        MsgC = request.form['MsgC']
        add_contc(Cname,em_ID,MsgC)
        return render_template('CONTACT1.html')
    else:
        return "Method Not Allowed", 405


@app.route('/NCntc')
def NCntc():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("select * from contc")
    cusq=cursor.fetchall()
    return render_template("/admin/Help.html",cusq=cusq)

@app.route('/about')
def about():
    u_id=request.args.get('u_id')
    return render_template("ABOUT1.html", u_id=u_id)

@app.route('/shop')
def shop():
    u_id=request.args.get('u_id')
    return render_template("SHOP1.html", u_id=u_id)

@app.route('/Cnt')
def Cnt():
    u_id=request.args.get('u_id')
    return render_template("CONTACT1.html", u_id=u_id)

@app.route('/cart')
def cart():
    u_id=request.args.get('u_id')
    return render_template("CART1.html", u_id=u_id)

@app.route('/chat')
def chat():
    u_id=request.args.get('u_id')
    return render_template("Chat.html", u_id=u_id)

@app.route('/car')
def car():
     conn = get_db_connection()
     cursor = conn.cursor()
     cursor.execute("select * from products")
     PrdAd=cursor.fetchall()
     PrdAd_image = []
     cursor.close()
     conn.close()
     for PD in PrdAd:
         PrdAd_list = list(PD)
         image_data = PrdAd_list[1]
         encoded_image = base64.b64encode(image_data).decode('utf-8')
         PrdAd_list[1] = encoded_image 
         PrdAd_image.append(tuple(PrdAd_list))
     return render_template("CAR.html",PrdAd_image = PrdAd_image)
    


@app.route('/adminL')
def adminL():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("select count(*) from signup ")
    user_count=cursor.fetchone()
    cursor.execute("select count(*) from products")
    product_count=cursor.fetchone()
    cursor.execute("select count(*) from payment")
    orders_count=cursor.fetchone()
    cursor.execute("select sum(price) from payment")
    total_rate = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template("/admin/ad.html",user_count=user_count[0],product_count=product_count[0],orders_count=orders_count[0],total_rate=total_rate[0])


@app.route('/PrdAdd', methods=['POST','GET'])
def PrdAdd():
    
    if request.method == "POST":
        img = request.files['prd_img']
        prd_img = img.read()
        prd_name = request.form['prd_name']
        prd_des = request.form['prd_des']
        prd_prc = request.form['prd_prc']
        add_products(prd_img, prd_name, prd_des, prd_prc)
        return render_template("/admin/AP.html")
    else:
        return "Method Not Allowed", 405
    
@app.route('/prdd')
def prdd():
    return render_template("/admin/AP.html")

@app.route('/PrdDetl')
def PrdDetl():
     conn = get_db_connection()
     cursor = conn.cursor()
     cursor.execute("select * from products")
     PrdAd=cursor.fetchall()
     PrdAd_image = []
     cursor.close()
     conn.close()
     for PD in PrdAd:
         PrdAd_list = list(PD)
         image_data = PrdAd_list[1]
         encoded_image = base64.b64encode(image_data).decode('utf-8')
         PrdAd_list[1] = encoded_image 
         PrdAd_image.append(tuple(PrdAd_list))
     return render_template("/admin/PrdDet.html",PrdAd_image = PrdAd_image)



@app.route('/delete_product/<int:id>', methods=['DELETE'])
def delete_product(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
     
        # Delete the product from the database
        cursor.execute("DELETE FROM products WHERE id = ?", (id,))
        conn.commit()

        return jsonify({'success': True}), 200
    except Exception as e:
        # If an error occurs, return an error response
          return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/Ords')
def Ords():
    return render_template("/admin/Orders.html")

@app.route('/AdLogt')
def AdLogt():
    return render_template("/admin/ADlogin.html")


@app.route('/Shipping')
def Shipping():
    return render_template('Pay.html')

@app.route('/paying', methods=['POST'])
def paying():
    if request.method == "POST":
        cusNm = request.form['cusNm']
        phNum = request.form['phNum']
        adrs = request.form['adrs']
        quantity = request.form['quantity']
        price = request.form['price']
        add_payment(cusNm,phNum,adrs,quantity,price)
        return render_template('Pay.html')
    else:
        return "Method Not Allowed", 405

@app.route('/PayD')
def PayD():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("select * from payment")
    pays = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("/admin/Orders.html",pays=pays)


if __name__ =="__main__":
    app.run(debug=True)
