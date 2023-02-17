import pymysql
from flask import Flask, request, json, jsonify, abort, flash, redirect, url_for, render_template, session
from sqlalchemy import or_
# from sqlalchemy.dialects.mysql import pymysql

from search_and_add import app, User, db, Order

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
            user = User(name=request.form['name'], pwd=request.form['pwd'], mobileNumber=request.form['mobileNumber'])
            db.session.add(user)
            db.session.commit()
            return '成功注册！'
        else:
            return '该用户名已被注册！'
    return error

@app.route('/changeInfo', methods=['GET', 'POST'])
def changeInfo():
    error = None
    db = pymysql.connect(host="localhost", user="root", password="154813029!Ax", database="runoob", charset="utf8")
    cursor = db.cursor()
    name = request.values.get('name')
    sql1 = "select * from User_tb where name='" + name + "'"
    cursor.execute(sql1)
    results = cursor.fetchall()
    if request.method == 'POST':
        if request.form['pwd'] != request.form['repeatChangePwd']:
            error = '两次密码不相同'
        elif len(results) == 0:
            error = '查询不到用户信息'
        else:
            mobileNumber = request.values.get('mobileNumber')
            pwd = request.values.get('pwd')
            User.query.filter(User.name == name).update({'pwd':pwd , 'mobileNumber':mobileNumber})
            return "更新成功"
    return error

if __name__ == '__main__':
    app.run(port=2023, host='127.0.0.1')