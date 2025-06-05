from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/orders")
def get_orders():
    return jsonify([
        {"order_id": 101, "items": ["Laptop"]},
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
