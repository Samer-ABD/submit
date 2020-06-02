from flask import Flask, render_template,request,Response,redirect,url_for # For flask implementation    
from bson import ObjectId # For ObjectId to work    
from pymongo import MongoClient  




client = MongoClient('localhost',27017)

db = client['pfe']

collection = db['mycol']

app = Flask (__name__)

@app.route('/')
def index():
    render_template('index.html')

@app.route('/', methods =['POST'])
def getvalue(): 
    fname = request.form['fname']
    lname = request.form['lname']
    return render_template('index.html', ln=lname, fn=fname)
    
  
if __name__== '__main__':
   app.run(debug=True) 
   


""" d = {'a':0,'b':5}
print('d: {}'.format(d['a']))
l=[]
list_col = l.append(collection['samer'])
for element in list_col:
    print(element) """
""" d = {'samer':'abderrahim','nadim':'abderrahim','hamzah':'ismail','anis':'bouzahar'}
x = collection.insert_one(d) """
""" from pprint import pprint

cursor = collection.find({'Name':'Samer'})
for document in cursor: 
    pprint(document) """