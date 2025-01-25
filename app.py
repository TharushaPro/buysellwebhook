import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the API"

@app.route('/buy', methods=['POST'])
def buy():
    data = request.get_json()
    if not data:
        return jsonify({"message": "No data received"}), 400

    # Process buy request (adjust this to your logic)
    amount = data.get('amount')
    if amount:
        return jsonify({"message": f"Buy request received for amount: {amount}"})
    else:
        return jsonify({"message": "Amount missing"}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Ensure your app listens on the correct port
    app.run(host='0.0.0.0', port=port, debug=True)
