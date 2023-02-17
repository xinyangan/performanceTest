import pymysql
import traceback
from flask import Flask, request, json, jsonify, abort, flash, redirect, url_for, render_template, session
from typing import List

from sqlalchemy.sql.elements import or_
from sqlalchemy.sql.functions import random
from werkzeug.security import generate_password_hash, check_password_hash
from random import seed, randint
from search_and_add import app, User, db, Order


def request_parse(req_data):
    if req_data.method == 'POST':
        data = req_data.json
    elif req_data.method == 'GET':
        data = req_data.args
    return data

# users = {
#     "john": generate_password_hash("hello"),
#     "susan": generate_password_hash("bye"),
#     "tom": generate_password_hash("hhh"),
#     "xinyang": generate_password_hash("pptt"),
#     "yuqian": generate_password_hash("gugu"),
#     "shanshan": generate_password_hash("dudh"),
#     "hrini": generate_password_hash("test"),
#     "vipul": generate_password_hash("bingfa"),
#     "niels": generate_password_hash("gaga"),
#     "alok": generate_password_hash("qnjw"),
#     "masthan": generate_password_hash("01Sb2"),
#     "rajiv": generate_password_hash("123456"),
#     "kala": generate_password_hash("uat"),
#     "shilpa": generate_password_hash("hi"),
#     "fiona": generate_password_hash("kong")
# }

# productInventory = [
#     ['jacket', 'c'],
#     ['iPhone', 'e'],
#     ['iPad', 'e'],
#     ['Mac', 'e'],
#     ['kindle', 'e'],
#     ['milk', 'm'],
#     ['bread', 'f'],
# ]

# 注册检验（用户名、邮箱验证）
def vaild_regist(name):
    user = User.query.filter(or_(User.name == name)).first()
    if user:
        return False
    else:
        return True


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        if request.form['pwd'] != request.form['password']:
            error = '两次密码不相同'
        elif vaild_regist(request.form['name']):
            user = User(name=request.form['name'], pwd=request.form['pwd'])
            db.session.add(user)
            db.session.commit()
            return '成功注册！'
        else:
            return '该用户名已被注册！'
    return error

@app.route('/login', methods=['GET', 'POST'])
def login():
    db = pymysql.connect(host="localhost", user="root", password="154813029!Ax", database="runoob", charset="utf8")
    cursor = db.cursor()
    name = request.values.get('name')
    pwd = request.values.get('pwd')
    sql = "select * from User_tb where name='" + name + "' and pwd='" + pwd + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) == 1:
        return '登录成功'
    else:
        return '用户名或密码不正确'

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    return '您已登出'


@app.route('/productList', methods=['GET', 'POST'])
def get_productList_by_type():
    db = pymysql.connect(host="localhost", user="root", password="154813029!Ax", database="runoob", charset="utf8")
    cursor = db.cursor()
    list_id = request.values.get('list_id')
    sql = "select * from Product_tb where type='" + list_id + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    if len(results) == 0:
        return 'no'
    else:
        resultList = {"code": 200, "resultList": results}
        return json.dumps(resultList, ensure_ascii=False)

# 不连接数据库
# @app.route('/login', methods=['GET', "POST"])  # 路由默认接收请求方式位POST，然而登录所需要请求都有，所以要特别声明。
# def login():
#     name = request.values.get('name')
#     pwd = request.values.get('pwd')
#     if name and pwd:
#         if name in users and check_password_hash(users.get(name), pwd):
#             result = {"code": 200, "message": "login successfully!"}
#             return json.dumps(result, ensure_ascii=False)
#         else:
#             result = {"code": 403, "message": "forbidden"}
#             return json.dumps(result, ensure_ascii=False)
#
# @app.route('/productList', methods=['GET', 'POST'])
# def get_productList():
#     list_id = request.values.get('list_id')
#     filter_list = list(filter(lambda t: t[1] == list_id, productInventory))
#     if len(filter_list) == 0:
#         abort(403)
#     else:
#         return filter_list

@app.route('/order', methods=['POST'])
def order():
    randomId = randint(100000, 2000000)
    order = Order(refId=randomId, productName=request.form['productName'], amount=request.form['amount'])
    db.session.add(order)
    db.session.commit()
    return 'you have brought the products successfully'

if __name__ == '__main__':
    app.run(port=2023, host='127.0.0.1')