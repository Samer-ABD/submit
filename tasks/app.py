from flask import Flask,render_template,url_for,request,redirect
from pymongo import MongoClient




app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')

db = client['tasks']

collection = db['col']


""" for db in client.list_databases():
    print(db) """
@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
      """ col = MongoClient.db.col  """
      collection.insert_one({'key': request.form['content']})
      
    return render_template('index.html') 

if __name__ == "__main__":
    app.run(debug=True)