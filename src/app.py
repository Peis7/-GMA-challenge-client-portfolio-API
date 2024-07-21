from flask import Flask,jsonify,request
from dotenv import load_dotenv
from flask_pymongo import PyMongo
from bson import json_util, ObjectId
import os
import json

load_dotenv('../.env') # take environment variables from .env.


app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
mongo = PyMongo(app)

def parse_json(data):
    return json.loads(json_util.dumps(data))

@app.route("/v1/portfolio/client/<id>")
def portfolio_by_client(id):
    client_portfolio_data =  mongo.db.client_portfolios.find_one({"clientId": id})
    data = parse_json(client_portfolio_data if client_portfolio_data else {'message': 'No client portfolio found'})
    return data, 200

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0",port=5001)