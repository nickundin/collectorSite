from flask import render_template
from collectorSite import app, db
from collectorSite.models import Product

# insert the code to create products from the webscraper here
# db.drop_all()
# db.create_all()
# products = []
# for product in products:
#     product_1 = Product(title='Keyboard', price = 100, condition = 'new') # modify this to read attributes from a dictionary
#     db.session.add(product_1)
#     db.session.commit()

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
