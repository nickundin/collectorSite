from flask import render_template
from collectorSite import app
from collectorSite.models import Product

# gets the actual products from the database
products = Product.query.all()

# simulates data in the database for now
# products = [
#     {
#         'name': 'Keyboard',
#         'price': 100,
#         'description': 'A funny description'
#     },
#     {
#         'name': 'Shoes',
#         'price': 200,
#         'description': 'Test'
#     }
# ]


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/products')
def displayProducts():
    return render_template('products.html', products=products)
