#!/usr/bin/env python3

from flask import Flask, jsonify, make_response

contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a business"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}
]

customers = ["bob", "bill", "john", "sarah"]

app = Flask(__name__)

# -------------------------
# Route: /contract/<id>
# -------------------------


@app.route('/contract/<int:id>', methods=['GET'])
def get_contract(id):
    # Look for the contract with matching id
    contract = next((c for c in contracts if c["id"] == id), None)
    if contract:
        # Contract found: return info with 200
        return jsonify(contract), 200
    else:
        # Contract not found: 404
        return jsonify({"error": "Contract not found"}), 404

# -------------------------
# Route: /customer/<customer_name>
# -------------------------


@app.route('/customer/<customer_name>', methods=['GET'])
def get_customer(customer_name):
    # Check if customer exists
    if customer_name.lower() in customers:
        # Customer found: 204 No Content
        return "", 204
    else:
        # Customer not found: 404
        return jsonify({"error": "Customer not found"}), 404


# -------------------------
# Run the app
# -------------------------
if __name__ == '__main__':
    app.run(port=5555, debug=True)
