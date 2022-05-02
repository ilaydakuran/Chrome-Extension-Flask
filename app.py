from flask import Flask, jsonify, request,render_template
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'



if __name__ == '__main__':
    app.run(debug=True)

@app.route('/test', methods=['GET', 'POST']) # https://127.0.0.1:5000/test çalıştırıyoruz
def testfn():
    # GET request
    if request.method == 'GET':
        message = {'greeting':'Hello from Flask!', 'timestamp':'ts', 'user_id':'123', 'metadata':{"smt":50} }
        return jsonify(message)  # serialize and use JSON headers


    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200