from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string("""
    <h1>🛒 Cloud-Native E-Commerce</h1>
    <ul>
        <li><a href="/products">View Products</a></li>
        <li><a href="/cart">View Cart</a></li>
        <li><a href="/orders">View Orders</a></li>
    </ul>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
