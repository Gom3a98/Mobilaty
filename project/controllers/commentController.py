from __future__ import print_function  # In python 2.7
import sys
from project import app
from flask import render_template, redirect, url_for, jsonify, request

from project.models.Comment import Comment

comment = Comment()


@app.route('/comment', methods=['GET'])
def index():
    print('show comment', file=sys.stderr)
    response = jsonify(comment.show_comment(request.json))
    response.status_code = 200
    return response


@app.route('/Allcomment', methods=['GET'])
def index2():
    print('show comment', file=sys.stderr)
    response = jsonify(comment.show_AllComment())
    response.status_code = 200
    return response


@app.route('/comment/create', methods=['POST'])
def Create():
    comment.add_comment(request.json)
    print('Create Comment!', file=sys.stderr)
    return jsonify('done')


@app.route('/comment/update', methods=['POST'])
def update():
    comment.update_comment(request.json)
    print('Update Comment!', file=sys.stderr)
    return jsonify('done')


@app.route('/comment/delete', methods=['GET'])
def Delete():
    comment.delete_comment(request.json)
    print('Delete Comment!', file=sys.stderr)
    return jsonify('done')
