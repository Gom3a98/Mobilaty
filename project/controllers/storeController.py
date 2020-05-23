from __future__ import print_function  # In python 2.7
import sys
from project import app
from flask import render_template, redirect, url_for, jsonify, request

from project.models.Store import Store
import numpy as np
import pandas as pd
store = Store()


@app.route('/store', methods=['GET'])
def index_store():
    print('show store', file=sys.stderr)
    response = jsonify(store.show_store(request.json))
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
