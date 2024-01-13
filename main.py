from flask import Flask
from read_org_master import get_org_details
from get_profiles import get_profiles
from flask import jsonify, make_response
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    x=get_org_details();
    print(x);
    return make_response(jsonify(x), 200)

@app.route('/getprofiles', methods=['GET', 'POST'])
def getprofiles():
    x=get_profiles();
    print(x);
    return make_response(jsonify(x), 200)