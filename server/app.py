#!/usr/bin/env python3

from flask import Flask, jsonify

# Sample data
contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a business"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}
]

customers = ["bob", "bill", "john", "sarah"]

# Initialize Flask app
app = Flask(__name__)


# Route: /contract/<id>


@app.route('/contract/<int:id>', methods=['GET'])
def get_contract(id):

    contract = next((c for c in contracts if c["id"] == id), None)

    if contract:
        return contract["contract_information"], 200

    return jsonify({"error": "Contract not found"}), 404


# Route: /customer/<customer_name>
@app.route('/customer/<customer_name>', methods=['GET'])
def get_customer(customer_name):

    if customer_name.lower() in [c.lower() for c in customers]:

        return "", 204

    return jsonify({"error": "Customer not found"}), 404


# Run the server
if __name__ == '__main__':
    app.run(port=5555, debug=True)
