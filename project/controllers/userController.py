from __future__ import print_function  # In python 2.7
import sys
from project import app
from flask import render_template, redirect, url_for, jsonify, request
import json
from project.models.user import User

User = User()


# comment=Comment()

@app.route('/login', methods=['GET'])
def Loginget():
    print('LoginGet', file=sys.stderr)
    print(request.json)
    Result = User.LogInGet(request.json)
    return jsonify(Result)


@app.route('/login', methods=['POST'])
def LogInpost():
    print('LoginPost', file=sys.stderr)
    return jsonify(User.LogInPost(request.json))


@app.route('/signup', methods=['GET'])
def Signupget():
    print('SignupGET', file=sys.stderr)
    return jsonify(User.SignupGet(request.json))


@app.route('/signup', methods=['POST'])
def Signuppost():
    print('SignupPost', file=sys.stderr)
    return jsonify(User.SignupPost(request.json))


@app.route('/getuserbyid', methods=['GET'])
def get_User_By_Id():
    print('get_All_Users', file=sys.stderr)
    return jsonify(User.getUserById(request.json))


@app.route('/createuser', methods=['POST'])
def create_user():
    print('createuser', file=sys.stderr)
    User.createuser(request.json)
    return jsonify("Done!")


@app.route('/removeuser', methods=['POST'])
def remove_user():
    print('removeuser', file=sys.stderr)
    User.removeuser(request.json)
    return jsonify("Done!")


@app.route('/finduserByUserName', methods=['GET'])
def find_user_By_User_Name():
    print('get_All_Users', file=sys.stderr)
    return jsonify(User.finduserByUserName(request.json))
