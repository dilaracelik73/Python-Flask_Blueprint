from flask import Blueprint, render_template
product_bp =Blueprint("product_bp", __name__)

#blueprint ile yönlendirmeyi app.py dosyası üzerinden yapabiliriz.

@product_bp.route("/")
def show_products():
    products = ["phone","television","tablet","laptop"]
    return render_template("products.html", products=products)

@product_bp.route("/<product_name>")
def show_product(product_name):
    return f"Product Name: {product_name}"
