from application import app
from application.models import Store
from flask import render_template


@app.route('/')
@app.route('/home')
def main_page():
    return render_template('home.html')


@app.route('/products')
def products():
    return render_template('products.html', products=Store.select_all_products())
