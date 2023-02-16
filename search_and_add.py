from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

with app.app_context():
    app.config['SECRET_KEY']='154813029!Ax' # 密码
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:154813029!Ax@localhost:3306/runoob'
    # 协议：mysql+pymysql
    # 用户名：root
    # 密码：2333
    # IP地址：localhost
    # 端口：3306
    # 数据库名：runoob #这里的数据库需要提前建好
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_ECHO'] = True
    db=SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'User_tb'
    mid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    pwd = db.Column(db.String(64), unique=True)

class Product(db.Model):
    __tablename__ = 'product_tb'
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    type = db.Column(db.String(32))

# db.drop_all()
# with app.app_context():
#     db.create_all()

if __name__ == '__main__':

    per_one = User(name='masthan', pwd='01Sb2')
    per_two = User(name='rajiv', pwd='123456')
    per_three = User(name='kala', pwd='uat')
    per_four = User(name='shilpa', pwd='hi')
    per_five = User(name='fiona', pwd='kong')
    with app.app_context():
        db.session.add_all([per_one, per_two, per_three, per_four, per_five])
        db.session.commit()

    phone_one = Product(name='iPhone13', type='e')
    phone_two = Product(name='iPad air', type='e')
    phone_three = Product(name='Mac plus', type='e')
    phone_four = Product(name='milk2', type='m')
    phone_five = Product(name='hotdog', type='f')
    phone_six = Product(name='tshirt', type='c')
    with app.app_context():
        db.session.add_all([phone_one, phone_two, phone_three, phone_four, phone_five, phone_six])
        db.session.commit()

    app.run(port='2022', host='127.0.0.1')