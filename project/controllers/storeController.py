from __future__ import print_function  # In python 2.7
import sys
from project import app
from flask import render_template, redirect, url_for, jsonify, request

from project.models.Store import Store

store = Store()


@app.route('/store', methods=['GET'])
def index_store():
    print('show store', file=sys.stderr)
    response = jsonify(store.show_store(request.json))
    response.status_code = 200
    return response


@app.route('/Allstore', methods=['GET'])
def index2_store():
    print('show posts', file=sys.stderr)
    response = jsonify(store.show_AllStore())
    response.status_code = 200
    return response


@app.route('/store/create', methods=['GET'])
def Create_store():
    store.add_store(request.json)
    print('Create store!', file=sys.stderr)
    return jsonify('done')


@app.route('/store/update', methods=['POST'])
def update_store():
    store.update_store(request.json)
    print('Update store!', file=sys.stderr)
    return jsonify('done')


@app.route('/store/delete', methods=['GET'])
def Delete_store():
    store.delete_store(request.json)
    print('Delete store!', file=sys.stderr)
    return jsonify('done')
