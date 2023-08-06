import mysql.connector
from flask import Flask,request,render_template


app = Flask(__name__)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "paskall14",
    database = "storedb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM shop")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

#------ADD VAlUES TO DATABASE

@app.route("/add", methods = ['POST', 'GET'])
def add():
    adding()
    return render_template("add.html")
  

def adding():
    if request.method == 'POST':
        global product, price

        product = request.form['product']
        price = request.form['price']
        
        mycursor.execute("INSERT INTO shop (product, price) VALUES (%s ,%s)",(product, price))
        
        mydb.commit()

        
        print("record inserted.")
    else:
        print("NOT RECORDED!!")


#---------SHOW DATA FRAM DATABASES------

