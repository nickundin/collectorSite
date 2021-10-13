# import sys
# sys.path.append('../WebScraper/Ebay WebScraper')

from flask import render_template
from collectorSite import app, db
from collectorSite.models import Product

# resets the database
db.drop_all()
db.create_all()

products = [] # how I get the return of the webscraper from here? should be a list of dictionaries TODO
for product in products:
        # assigns the values of a given product dictionary to variables using the key
        theTitle = product['item_name']
        theImage = product['item_image']
        thePrice = product['item_price']
        theCondition = product['item_condition']
        theSellerInfo = product['item_seller']
        theAvailability = product['item_availability']
        theReturnPolicy = product['item_return_policy'] # wait for push
        
        # creates a new product using the values and adds newProduct to the database
        newProduct = Product(theTitle, theImage, thePrice, theCondition, theSellerInfo, theAvailability, theReturnPolicy)
        db.session.add(newProduct)
        db.session.commit()

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
