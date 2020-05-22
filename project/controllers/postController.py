from __future__ import print_function  # In python 2.7
import sys
from project import app
from flask import render_template, redirect, url_for, jsonify, request

from project.models.Post import Post

post = Post()


@app.route('/post', methods=['GET'])
def index_1():
    print('show post', file=sys.stderr)
    response = jsonify(post.show_post(request.json))
    response.status_code = 200
    return response


@app.route('/post/findByStoreId', methods=['GET'])
def findByStoreId():
    response = jsonify(post.findByStoreId(request.json))
    response.status_code = 200
    return response


@app.route('/Allpost', methods=['GET'])
def index_2():
    print('show posts', file=sys.stderr)
    response = jsonify(post.show_AllPost())
    response.status_code = 200
    return response


@app.route('/post/create', methods=['GET'])
def Create_post():
    post.add_post(request.json)
    print('Create post!', file=sys.stderr)
    return jsonify('done')


@app.route('/post/update', methods=['POST'])
def update_post():
    post.update_post(request.json)
    print('Update post!', file=sys.stderr)
    return jsonify('done')


@app.route('/post/delete', methods=['GET'])
def Delete_post():
    post.delete_post(request.json)
    print('Delete post!', file=sys.stderr)
    return jsonify('done')
