import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("mongodb://sumagunawan:sugunjenk10@ac-pig4g6g-shard-00-00.lm8jmgi.mongodb.net:27017,ac-pig4g6g-shard-00-01.lm8jmgi.mongodb.net:27017,ac-pig4g6g-shard-00-02.lm8jmgi.mongodb.net:27017/?ssl=true&replicaSet=atlas-w3dsec-shard-0&authSource=admin&retryWrites=true&w=majority&appName=AtlasApp")
DB_NAME =  os.environ.get("fanproject")

client = MongoClient("mongodb://sumagunawan:sugunjenk10@ac-pig4g6g-shard-00-00.lm8jmgi.mongodb.net:27017,ac-pig4g6g-shard-00-01.lm8jmgi.mongodb.net:27017,ac-pig4g6g-shard-00-02.lm8jmgi.mongodb.net:27017/?ssl=true&replicaSet=atlas-w3dsec-shard-0&authSource=admin&retryWrites=true&w=majority&appName=AtlasApp")

db = client["fanproject"]

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    # sample_receive = request.form['sample_give']
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name': name_receive,
        'comment': comment_receive,
    }
    db.fanmessages.insert_one(doc)
    return jsonify({'msg':'Comment Posted!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    message_list = list(db.fanmessages.find({}, {'_id': False}))
    return jsonify({'messages': message_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)