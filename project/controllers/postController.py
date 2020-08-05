from __future__ import print_function  # In python 2.7
import sys
from project import app
from flask import render_template, redirect, url_for, jsonify, request

from project.models.Post import Post

post = Post()


@app.route('/post', methods=['POST'])
def index_1():
    print('show post', file=sys.stderr)
    data = request.get_json()
    response = jsonify(post.show_post(data[0]))
    response.status_code = 200
    return response


@app.route('/post/findByStoreId', methods=['POST'])
def findByStoreId():
    data = request.get_json()
    response = jsonify(post.findByStoreId(data[0]))
    response.status_code = 200
    return response


@app.route('/Allpost', methods=['GET'])
def index_2():
    print('show posts', file=sys.stderr)
    response = jsonify(post.show_AllPost())
    response.status_code = 200
    return response


@app.route('/post/create', methods=['POST'])
def Create_post():
    data = request.get_json()
    post.add_post(data[0])
    print('Create post!', file=sys.stderr)
    return jsonify('done')


@app.route('/post/update', methods=['POST'])
def update_post():
    data = request.get_json()
    post.update_post(data[0])
    print('Update post!', file=sys.stderr)
    return jsonify('done')


@app.route('/post/delete', methods=['POST'])
def Delete_post():
    data = request.get_json()
    post.delete_post(data[0])
    print('Delete post!', file=sys.stderr)
    return jsonify('done')

@app.route('/post/count_comment', methods=['POST'])
def Count_comment():
    data = request.get_json()
    print('count comment post!', file=sys.stderr)
    response = jsonify(post.count_comment(data[0]))
    response.status_code = 200
    return response

