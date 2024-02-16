from flask import *

from flask_cors import CORS
from functools import wraps
import pymongo
from bson.json_util import dumps

app = Flask(__name__,static_folder='./static/',static_url_path='')
CORS(app)

myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb = myclient["local"]
CNC1_col = mydb["CNC1"]
CNC2_col = mydb["CNC2"]
CNC3_col = mydb["CNC3"]
AGV_col = mydb["AGV"]
LASER_col = mydb["LASER"]
print(list(AGV_col.find()))


