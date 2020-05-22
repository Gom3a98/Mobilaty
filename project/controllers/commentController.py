
from __future__ import print_function # In python 2.7
import sys
from project import app
from flask import render_template, redirect, url_for ,jsonify,request
  

from project.models.Comment import Comment

comment=Comment()

@app.route('/comment', methods = ['GET'])
def index():
    print('show comment', file=sys.stderr)
    return jsonify(comment.show_comment(request.args))
@app.route('/comment/create', methods = ['POST'])
def Create():
    comment.add_comment(request.get_json())
    print('Create Comment!', file=sys.stderr)
    return jsonify('done')

@app.route('/comment/update', methods = ['GET'])
def update():
    comment.update_comment(request.get_json())
    print('Update Comment!', file=sys.stderr)
    return jsonify('done')
@app.route('/comment/delete', methods = ['POST'])
def Delete():
    comment.delete_comment(request.get_json())
    print('Delete Comment!', file=sys.stderr)
    return jsonify('done')

    