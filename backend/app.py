from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import spacy
from spacy import displacy
from temp import getText


app = Flask(__name__)
CORS(app) 
nlp = spacy.load("en_core_web_sm")


UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return jsonify({'message': 'File successfully uploaded'}), 200
    

@app.route('/ner', methods=['GET'])
def ner():

    text = getText()

    doc = nlp(text)

    html = displacy.render(doc, style="ent", page=True)

    return jsonify({"html": html})

if __name__ == '__main__':
    app.run(debug=True)