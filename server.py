from flask import Flask, request, jsonify , render_template
from flask_cors import CORS
from schema import generate_schema 
import requests


app = Flask(__name__)
CORS(app)  
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/generate', methods=['POST'])
def generate():
    user_text = request.json.get('user_text') #replace it with the user input here

    schema = generate_schema(user_text) #replace it with the user input 
    
    return jsonify(schema)

if __name__ == '__main__':
    app.run(port=5000)



# https://m0hmed.pythonanywhere.com/generate    