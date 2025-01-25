from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Trading Bot!"

@app.route('/buy', methods=['POST'])
def buy():
    try:
        # Check if the request contains JSON data
        data = request.get_json()

        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        # Assuming the 'amount' field is required
        amount = data.get("amount")
        if amount is None:
            return jsonify({"error": "'amount' field is missing in the JSON data"}), 400
        
        # Process the buy request (add your buy logic here)
        return jsonify({"message": f"Buy request received for amount: {amount}"}), 200

    except Exception as e:
        # In case of any unexpected errors
        return jsonify({"error": str(e)}), 500


@app.route('/sell', methods=['POST'])
def sell():
    try:
        # Check if the request contains JSON data
        data = request.get_json()

        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        # Assuming the 'amount' field is required
        amount = data.get("amount")
        if amount is None:
            return jsonify({"error": "'amount' field is missing in the JSON data"}), 400
        
        # Process the sell request (add your sell logic here)
        return jsonify({"message": f"Sell request received for amount: {amount}"}), 200

    except Exception as e:
        # In case of any unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
