from flask import Flask, request, json, jsonify, abort, flash, redirect, url_for, render_template, session
from sqlalchemy import or_

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
            user = User(name=request.form['name'], pwd=request.form['pwd'])
            db.session.add(user)
            db.session.commit()
            return '成功注册！'
        else:
            return '该用户名已被注册！'
    return error

if __name__ == '__main__':
    app.run(port=2023, host='127.0.0.1')