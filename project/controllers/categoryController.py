from __future__ import print_function  # In python 2.7
import sys
from project import app
from flask import render_template, redirect, url_for, jsonify, request

from project.models.category import Category

category = Category()


@app.route('/category', methods=['POST'])
def show_category():
    print('show category', file=sys.stderr)
    data = request.get_json()
    response = jsonify(category.show_category(data[0]))
    response.status_code = 200
    return response


@app.route('/category/findByCategoryId', methods=['POST'])
def findBy_Category_Id():
    print('findByCategoryId category', file=sys.stderr)
    data = request.get_json()
    response = jsonify(category.findByCategoryId(data[0]))
    response.status_code = 200
    return response


@app.route('/Allcategory', methods=['GET'])
def All_category():
    print('show category', file=sys.stderr)
    response = jsonify(category.show_AllCategory())
    response.status_code = 200
    return response


@app.route('/category/create', methods=['POST'])
def Create_category():
    data = request.get_json()
    category.add_category(data[0])
    print('Create category!', file=sys.stderr)
    return jsonify('done')


@app.route('/category/update', methods=['POST'])
def update_category():
    data = request.get_json()
    category.update_category(data[0])
    print('Update category!', file=sys.stderr)
    return jsonify('done')


@app.route('/category/delete', methods=['POST'])
def Delete_category():
    data = request.get_json()
    category.delete_category(data[0])
    print('Delete category!', file=sys.stderr)
    return jsonify('done')
