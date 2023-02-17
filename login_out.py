import pymysql
from flask import Flask, request, json, jsonify, abort, flash, redirect, url_for, render_template, session
from search_and_add import app, User, db, Order

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

if __name__ == '__main__':
    app.run(port=2023, host='127.0.0.1')