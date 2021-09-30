from flask import Flask, render_template

app = Flask(__name__, template_folder='../frontEnd/templates')

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
