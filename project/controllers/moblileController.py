from __future__ import print_function
from project import app
from flask import render_template, redirect, url_for, jsonify, request

from project.models.mobile import Mobile
import sys
from sklearn.externals import joblib
import pandas as pd
import numpy as np
import pickle
import os

mobile = Mobile()

path = os.getcwd()
parent = os.path.dirname(path) 
print(parent)
@app.route('/predictPrice', methods=['GET'])
def PredictPrice():
    arr= np.zeros(21)
    arr[0]=(request.args.get('battery_power'))
    """
    #arr[1]=int(request.args.get('blue'))
    #arr[2]=int(request.args.get('clock_speed'))
    #arr[3]=int(request.args.get('dual_sim'))    
    #arr[4]=int(request.args.get('fc'))
    # arr[5]=int(request.args.get('four_g'))
    # arr[6]=int(request.args.get('int_memory'))
    #arr[7]=int(request.args.get('m_dep'))
    # arr[8]=int(request.args.get('mobile_wt'))
    # arr[9]=int(request.args.get('n_cores'))
    #arr[10]=int(request.args.get('pc'))
    arr[11]=int(request.args.get('px_height'))
    arr[12]=int(request.args.get('px_width'))
    arr[13]=int(request.args.get('ram'))
    #arr[14]=int(request.args.get('sc_h'))
    #arr[15]=int(request.args.get('sc_w'))
    #arr[16]=int(request.args.get('talk_time'))
    arr[17]=int(request.args.get('three_g'))
    arr[18]=int(request.args.get('touch_screen'))
    arr[19]=int(request.args.get('wifi'))
    """
    pipe = joblib.load(os.path.join(parent,'Mobilaty\\project\\public\\predictPrice.pkl'))
    pred = pd.Series(pipe.predict([arr]))
    return jsonify(pred)

@app.route('/croped_image', methods=['POST'])
def crop_image():
    data = request.get_json()
    return jsonify(mobile.Crop_image(data[0]))

@app.route('/classifiy_phone', methods=['POST'])
def Classifiy_phone():
    data = request.get_json()
    return mobile.Mobile_Classifier(data[0])

@app.route('/croped_video', methods=['POST'])
def crop_video():
    data = request.get_json()
    return jsonify(mobile.Crop_video(data[0]))

@app.route('/recommendMobile', methods=['POST'])
def Recommend_Mobile():
    cosine_sim = pickle.load(open(os.path.join(parent,'Mobilaty\\project\\public\\RecoomendMobile.sav'), 'rb'))
    data = request.get_json()
    Recommended=mobile.recommendations(data[0],cosine_sim)
    return Recommended


@app.route('/mobile', methods=['POST'])
def showMobile():
    print('show mobile', file=sys.stderr)
    data = request.get_json()
    response = jsonify(mobile.show_mobile(data[0]))
    response.status_code = 200
    return response


@app.route('/mobile/findByMobileId', methods=['POST'])
def findByMobileId():
    data = request.get_json()
    response = jsonify(mobile.findByMobileId(data[0]))
    response.status_code = 200
    return response


@app.route('/Allmobile', methods=['GET'])
def showAllmobile():
    print('show mobiles', file=sys.stderr)
    response = jsonify(mobile.show_AllMobile())
    response.status_code = 200
    return response


@app.route('/mobile/create', methods=['POST'])
def Create_mobile():
    data = request.get_json()
    mobile.add_mobile(data[0])
    print('Create mobile!', file=sys.stderr)
    return jsonify('done')


@app.route('/mobile/update', methods=['POST'])
def Update_mobile():
    data = request.get_json()
    mobile.update_mobile(data[0])
    print('Update mobile!', file=sys.stderr)
    return jsonify('done')


@app.route('/mobile/delete', methods=['POST'])
def Delete_mobile():
    data = request.get_json()
    mobile.delete_mobile(data[0])
    print('Delete mobile!', file=sys.stderr)
    return jsonify('done')