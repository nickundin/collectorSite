from collectorSite import db


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
        return f"Product('{self.title}', '{self.price}', '{self.condition}')"
