from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://test:1234@Cluster0.tmrbb2j.mongodb.net/?retryWrites=true&w=majority')
db = client.testC



@app.route('/')
def home():
   return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']
    bucket_all = list(db.bucket.find({},{'_id' : False}))
    count = len(bucket_all) + 1
    doc = {
        'b_index' : count,
        'b_content' : bucket_receive,
        'b_complate' : False
    }
    db.bucket.insert_one(doc)
    return jsonify({'msg': '기록 완료!'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    num_receive = request.form['num_give']
    db.bucket.update_one({'b_index':int(num_receive)}, {'$set':{'b_complate':True}})
    return jsonify({'msg': 'POST(완료) 연결 완료!'})

@app.route("/bucket", methods=["GET"])
def bucket_get():
    bucket_all = list(db.bucket.find({},{'_id' : False}))
    return jsonify({'bucket_all' : bucket_all})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)