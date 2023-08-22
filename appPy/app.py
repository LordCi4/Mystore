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

#------ADD VAlUES TO DATABASE

@app.route("/", methods = ['POST', 'GET'])
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

        
        return render_template("index.html")
    else:
        return render_template("add.html")



#---------SHOW DATA FRAM DATABASES------
@app.route("/index", methods = ['POST', 'GET'])
def index():
    if request.method == 'GET':
        mycursor.execute('SELECT * FROM shop')    
        
        result = mycursor.fetchall()

        mycursor.execute('SELECT price FROM shop')
        
        total = sum(value[0] for value in mycursor)

        return render_template('index.html', result = result, total=total)
   
    """if request.method == 'GET':
        sumPrice = mycursor.execute('SELECT price FROM shop')

        for x in range(sumPrice):
            total = total + x

        

        return render_template('index.html', total = total)"""

    
