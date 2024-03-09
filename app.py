from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = '1F7VkTpXpSB09P6UskV9Kq$23QWD9FG440'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Info.db'
db = SQLAlchemy(app)


class Shop(db.Model):
    __tableName__ = 'Shop'
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String, nullable=False)

    def __init__(self, id, area):
        self.id = id
        self.area = area


class Trade(db.Model):
    __tableName__ = 'Trade'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    shop = db.Column(db.String, nullable=False)
    vendor_code = db.Column(db.Integer, primary_key=True)
    operation = db.Column(db.String, nullable=False)
    count = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, primary_key=True)

    def __init__(self, id, date, shop, vendor_code, operation, count, price):
        self.id = id
        self.date = date
        self.shop = shop
        self.vendor_code = vendor_code
        self.operation = operation
        self.count = count
        self.price = price


class Product(db.Model):
    __tableName__ = 'Product'
    vendor_code = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String, nullable=False)
    product_name = db.Column(db.String, nullable=False)
    count_box = db.Column(db.Integer, primary_key=True)
    count_in_box = db.Column(db.Integer, primary_key=True)
    provider = db.Column(db.String, nullable=False)

    def __init__(self, vendor_code, department, product_name, count_box, count_in_box, provider):
        self.vendor_code = vendor_code
        self.department = department
        self.product_name = product_name
        self.count_box = count_box
        self.count_in_box = count_in_box
        self.provider = provider


@app.route('/shop_list')
def shop_list():  # put application's code here
    s = []
    for shop in Shop.query.all():
        print(shop.id)
        print(shop.area)
        s.append(shop.id)
        s.append(shop.area)
    return str(s)


@app.route('/trade_list')
def trade_list():  # put application's code here
    b = []
    for trady in Trade.query.all():
        print(trady.id)
        print(trady.date)
        print(trady.shop)
        print(trady.vendor_code)
        print(trady.operation)
        print(trady.count)
        print(trady.price)
        b.append(trady.id)
        b.append(trady.date)
        b.append(trady.shop)
        b.append(trady.vendor_code)
        b.append(trady.operation)
        b.append(trady.count)
        b.append(trady.price)
    return str(b)


@app.route('/product_list')
def product_list():  # put application's code here
    a = []
    for prod in Product.query.all():
        print(prod.vendor_code)
        print(prod.department)
        print(prod.product_name)
        print(prod.count_box)
        print(prod.count_in_box)
        print(prod.provider)
        a.append(prod.vendor_code)
        a.append(prod.department)
        a.append(prod.product_name)
        a.append(prod.count_box)
        a.append(prod.count_in_box)
        a.append(prod.provider)

    return str(a)


if __name__ == '__main__':
    app.run(debug=True)
