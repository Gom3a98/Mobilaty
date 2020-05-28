from __future__ import print_function  # In python 2.7
import sys
from project import app
from flask import render_template, redirect, url_for, jsonify, request

from project.models.Store import Store
import numpy as np
import pandas as pd
store = Store()


@app.route('/store', methods=['POST'])
def index_store():
    print('show store', file=sys.stderr)
    data = request.get_json()
    response = jsonify(store.show_store(data[0]))
    response.status_code = 200
    return response


@app.route('/recommendStore', methods=['GET'])
def recommendStore():
    
    requieStore=int(request.args.get('requieStore'))
    user_Xaxis=int(request.args.get('x_axis'))
    user_Yaxis=int(request.args.get('y_axis'))
    user_rate=int(request.args.get('rate'))
    a = np.array((user_Xaxis ,user_Yaxis, user_rate))
    def Eculidian_Distance(x,y,r):
        b = np.array((x, y, r))
        return  np.linalg.norm(a-b)


    trainData=store.show_AllStore()

    requieStore = requieStore if (len(trainData)>=requieStore) else len(trainData)
    rate = False if (user_rate==-1) else True 
    location = False if (user_Xaxis==-1 and user_Yaxis==0) else True 
    
    output=[]
    for i in range(len(trainData)):
        output.append((i,Eculidian_Distance(location*trainData[i].get('latitude'),
                    location*trainData[i].get('longitude'),rate*trainData[i].get('rate'))))

    def sortSecond(val): 
        return val[1]  
    output.sort(key = sortSecond) 
    response = []
    
    for i in range(requieStore):
        response.append(trainData[output[i][0]])
    return jsonify(response)


@app.route('/store/create', methods=['POST'])
def Create_store():
    data = request.get_json()
    store.add_store(data[0])
    print('Create store!', file=sys.stderr)
    return jsonify('done')


@app.route('/store/update', methods=['POST'])
def update_store():
    data = request.get_json()
    store.update_store(data[0])
    print('Update store!', file=sys.stderr)
    return jsonify('done')


@app.route('/store/delete', methods=['POST'])
def Delete_store():
    data = request.get_json()
    store.delete_store(data[0])
    print('Delete store!', file=sys.stderr)
    return jsonify('done')
