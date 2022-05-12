from flask import Flask, jsonify, request,render_template
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello_world():  # put application's code here
    return 'hellooo'
    return render_template('/Users/ilaydakuran/Desktop/ext/options.html')


if __name__ == '__main__':
    app.debug= True
    app.run()

@app.route('/api', methods=[ 'POST','GET']) # https://127.0.0.1:5000/test çalıştırıyoruz
def met():
    # GET request
    if request.method == 'GET':
       message = {'message':"comment.txt", 'timestamp':'ts', 'user_id':' '}
       print("succes")
       return jsonify(message)  # serialize and use JSON headers


    # POST request
    if request.method == 'POST':
        #name = request.form.get('name')
        print(**request.get_json())  # parse as JSON
        #message = {'greeting': 'Hello from Flask!', 'timestamp': 'ts', 'user_id': '123'}
        #return jsonify(message)  # serialize and use JSON headers
        return 'Sucesss', 200