import pymysql
from flask import Flask, request, json, jsonify, abort, flash, redirect, url_for, render_template, session
from random import seed, randint
from search_and_add import app, User, db, Order

@app.route('/productList/<id>/', methods=['GET', 'POST'])
def get_productList_by_type(id):
    db = pymysql.connect(host="localhost", user="root", password="154813029!Ax", database="runoob", charset="utf8")
    cursor = db.cursor()
    sql = "select * from Product_tb where type='" + id + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) == 0:
        return 'no'
    else:
        resultList = {"code": 200, "resultList": results}
        return json.dumps(resultList, ensure_ascii=False)

@app.route('/order', methods=['POST'])
def order():
    randomId = randint(100000, 2000000)
    order = Order(refId=randomId, productName=request.form['productName'], amount=request.form['amount'])
    db.session.add(order)
    db.session.commit()
    return 'you have brought the products successfully'

if __name__ == '__main__':
    app.run(port=2023, host='127.0.0.1')