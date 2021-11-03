# collectorSite
CodeHub project

To run, type "python backEnd\run.py" in the terminal from the root directory

### DATABASE STUFF 
To initialize the site.db file with items MANUALLY via the command line:
* cd backEnd
* python
* from collectorSite import db
* db.create_all()
* from collectorSite.models import Product
* product_1 = Product(title='Keyboard', price = 100, condition = 'new'), or whatever attributes are needed
* db.session.add(product_1)
* product_2 = Product(title='Shoes', price = 200, condition = 'new')
* db.session.add(product_2)
* db.session.commit()
    
This should create the site.db file with two products, which is then displayed by the products route.
All that's left now is to hook up the webscraper to the database.
