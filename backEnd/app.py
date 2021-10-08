from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='../frontEnd/templates')

# START OF DATABASE STUFF
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # unique id for the product
    image = db.Column(db.String(20), nullable=False,
                      default='default.jpg')
# ALL OF THE STRINGS HAVE A MAX LENGTH OF 20 FOR NOW. WILL CHANGE LATER
    title = db.Column(db.String(20), unique=True, nullable=False)
    price = db.Column(db.Float)
    condition = db.Column(db.String(20))
    sellerInfo = db.Column(db.String(20))
    availability = db.Column(db.String(20))
    returnPolicy = db.Column(db.String(20))

    # describes how the object will be printed out as a string
    def __repr__(self):
        return f"Post('{self.title}', '{self.price}', '{self.condition}'"

# END OF DATABASE STUFF


# simulates data in the database for now
products = [
    {
        'name': 'Keyboard',
        'price': 100,
        'description': 'A funny description'
    },
    {
        'name': 'Shoes',
        'price': 200,
        'description': 'Test'
    }
]

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products')
def displayProducts():
    return render_template('products.html', products=products)


if __name__ == "__main__":
    app.run(debug=True)
