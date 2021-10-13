from collectorSite import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # unique id for the product
# ALL OF THE STRINGS HAVE A MAX LENGTH OF 100 FOR NOW. WILL CHANGE LATER
    title = db.Column(db.String(100), unique=True, nullable=False)
    image = db.Column(db.String(100), nullable=False,
                      default='default.jpg')
    price = db.Column(db.String(100)) # change to float later
    condition = db.Column(db.String(100))
    sellerInfo = db.Column(db.String(100))
    availability = db.Column(db.String(100))
    returnPolicy = db.Column(db.String(100))
    link = db.Column(db.String(100)) # to be implemented

    # describes how the object will be printed out as a string
    def __repr__(self):
        return f"Product('{self.title}', '{self.price}', '{self.condition}')"
