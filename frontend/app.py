import requests
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


@app.route("/products")
def products():
    try:
        resp = requests.get("http://localhost:5001/products")
        resp.raise_for_status()
        products = resp.json().get("products", [])
    except:
        products = []
    items_html = "<ul>" + "".join(f"<li>{p}</li>" for p in products) + "</ul>"
    return render_template_string("""
    <h1>Products</h1>
    {{ items|safe }}
    <a href="/">Back to Home</a>
    """, items=items_html)


@app.route("/cart")
def cart():
    try:
        resp = requests.get("http://localhost:5002/cart")
        resp.raise_for_status()
        cart_items = resp.json().get("cart", [])
    except:
        cart_items = []
    items_html = "<ul>" + "".join(f"<li>{item}</li>" for item in cart_items) + "</ul>"
    return render_template_string("""
    <h1>Cart</h1>
    {{ items|safe }}
    <a href="/">Back to Home</a>
    """, items=items_html)


@app.route("/orders")
def orders():
    try:
        resp = requests.get("http://localhost:5003/orders")
        resp.raise_for_status()
        orders = resp.json().get("orders", [])
    except:
        orders = []
    items_html = "<ul>" + "".join(f"<li>{o}</li>" for o in orders) + "</ul>"
    return render_template_string("""
    <h1>Orders</h1>
    {{ items|safe }}
    <a href="/">Back to Home</a>
    """, items=items_html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
