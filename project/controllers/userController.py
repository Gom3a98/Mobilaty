from __future__ import print_function  # In python 2.7
import sys
from project import app
from flask import render_template, redirect, url_for, jsonify, request
import json
from project.models.user import User

User = User()


# comment=Comment()

@app.route('/login', methods=['POST'])
def Loginget():
    print('LoginGet', file=sys.stderr)
    data = request.get_json()
    Result = User.LogInGet(data[0])
    return jsonify(Result)


@app.route('/login', methods=['POST'])
def LogInpost():
    print('LoginPost', file=sys.stderr)
    data = request.get_json()
    return jsonify(User.LogInPost(data[0]))


@app.route('/signup', methods=['POST'])
def Signupget():
    print('SignupGET', file=sys.stderr)
    data = request.get_json()
    return jsonify(User.SignupGet(data[0]))


@app.route('/signup', methods=['POST'])
def Signuppost():
    print('SignupPost', file=sys.stderr)
    data = request.get_json()
    return jsonify(User.SignupPost(data[0]))


@app.route('/getuserbyid', methods=['POST'])
def get_User_By_Id():
    print('get_All_Users', file=sys.stderr)
    data = request.get_json()
    return jsonify(User.getUserById(data[0]))


@app.route('/createuser', methods=['POST'])
def create_user():
    print('createuser', file=sys.stderr)
    data = request.get_json()
    User.createuser(data[0])
    return jsonify("Done!")


@app.route('/removeuser', methods=['POST'])
def remove_user():
    print('removeuser', file=sys.stderr)
    data = request.get_json()
    User.removeuser(data[0])
    return jsonify("Done!")


@app.route('/finduserByUserName', methods=['POST'])
def find_user_By_User_Name():
    data = request.get_json()
    return jsonify(User.finduserByUserName(data[0]))
