from flask import Flask, jsonify, request,render_template
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource

from datasets import load_dataset, list_metrics
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import sklearn
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import torch

tokenizer = AutoTokenizer.from_pretrained("Narrativaai/deberta-v3-small-finetuned-hate_speech18")

model = AutoModelForSequenceClassification.from_pretrained("Narrativaai/deberta-v3-small-finetuned-hate_speech18")

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

dataset = load_dataset("hate_speech18", split='train')

columns = dataset.num_columns
rows = dataset.num_rows

col_name = dataset.column_names #['text', 'user_id', 'subforum_id', 'num_contexts', 'label']
#vectorizer = CountVectorizer()
#x = vectorizer.fit_transform(model)
#vectorizer.get_feature_names_out()
#print(x.toarray())
@app.route('/')
def hello_world():  # put application's code here
    print(col_name)
    print(dataset.info.features) #{'text': Value(dtype='string', id=None), 'user_id': Value(dtype='int64', id=None), 'subforum_id': Value(dtype='int64', id=None), 'num_contexts': Value(dtype='int64', id=None), 'label': ClassLabel(num_classes=4, names=['noHate', 'hate', 'idk/skip', 'relation'], id=None)}
    print(dataset)
    #print(metrics_list)

    return jsonify(col_name)


if __name__ =='__main__':
    app.debug = True
    app.run()


@app.route('/api', methods=['POST','GET'])# https://127.0.0.1:5000/api çalıştırıyoruz
def met():
    #GET request
    if request.method == 'GET':
        message = {'message': "comment.txt", 'timestamp': 'ts', 'user_id': ' '}
        print("get succes")
        return jsonify(message)

    # POST request
    if request.method == 'POST':
        request_data = request.get_json()
        inputs = tokenizer(request_data['message'], return_tensors="pt")
        with torch.no_grad():
            logits = model(**inputs).logits
        predicted_class_id = logits.argmax().item()
        # score = model.predict_classes(sklearn.feature_extraction(request_data['message']))

        print(model.config.id2label[predicted_class_id])
        return jsonify(predicted_class_id)
        if 'future' in request_data['message']:
            return jsonify(columns)
        else:
            return jsonify(rows)



