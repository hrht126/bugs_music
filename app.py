from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://pmaker126:gkfngkxm126@cluster0.pemxrix.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/chart", methods=["POST"])
def bucket_post():
    comment_receive = request.form['comment_give']
    doc = {
        'comment':comment_receive
    }
    db.comment.insert_one(doc)
    return jsonify({'msg': '저장 완료!'})
    
@app.route("/chart", methods=["GET"])
def bucket_get():
    return jsonify({'msg': 'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)