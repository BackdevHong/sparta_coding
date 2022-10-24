from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://test:1234@Cluster0.tmrbb2j.mongodb.net/?retryWrites=true&w=majority')
db = client.testC

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        "name" : name_receive,
        "comment" : comment_receive
    }
    db.fans.insert_one(doc)
    return jsonify({'msg':'기록 완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    all_fans = list(db.fans.find({},{'_id' : False}))
    return jsonify({'all_fans': all_fans})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)