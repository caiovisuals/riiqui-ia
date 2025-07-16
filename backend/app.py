from flask import Flask, request, jsonify
from flask_cors import CORS
from model.ia_model import responder

app = Flask(__name__)
CORS(app)

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("message", "")
    respost = responder(question)
    return jsonify({"response": respost})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
