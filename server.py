from flask import Flask, request, jsonify
from flask_cors import CORS
from schema import generate_schema 

app = Flask(__name__)
CORS(app)  

@app.route('/generate', methods=['POST'])
def generate():
    user_text = request.json.get('user_text')

    schema = generate_schema(user_text)
    
    return jsonify(schema)

if __name__ == '__main__':
    app.run(port=5000)