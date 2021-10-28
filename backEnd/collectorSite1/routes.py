from flask import render_template
from collectorSite1 import app, db
from collectorSite1.models import Product
from collectorSite1.WebScraper.WebPageWebScraper import PageParser

# resets the database
db.drop_all()
db.create_all()

website = PageParser("https://www.ebay.com/b/Collectible-Funko-Bobbleheads-1970-Now/149372/bn_3017826")
products = website.parse_all(2)
print("NOW PRINTING PRODUCTS")
print(products)
print("NOW FINISHED")

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
        # this is super ugly but it works for now, FIX LATER TODO
        newProduct = Product(title=theTitle, image=theImage, price=thePrice, condition=theCondition, sellerInfo=theSellerInfo, availability=theAvailability, returnPolicy=theReturnPolicy) # doesn't work
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
