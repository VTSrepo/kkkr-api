from flask import Flask,render_template
from read_org_master import get_org_details
from get_profiles import get_profiles
from flask import jsonify, make_response
from flask_cors import CORS
app = Flask(__name__, static_folder='./web', static_url_path='/')
CORS(app)
@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/")
def index():
    return app.send_static_file('index.html')

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

if __name__ == "__main__":
 app.run()