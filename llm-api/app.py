from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Simulate LLM processing
    return jsonify({
        "prompt": data.get("prompt"),
        "response": "Mock LLM response",
        "model": os.getenv("MODEL_NAME", "default")
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)