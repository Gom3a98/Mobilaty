'''
import numpy as np
import pandas as pd

data = pd.read_csv('train.csv')
x = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
m, n = len(x), len(x[0])+1
x = np.append(arr = np.ones((m, 1)).astype(int), values = x, axis = 1)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

pipe = make_pipeline(StandardScaler(), LogisticRegression())
pipe.fit(x_train, y_train)
y_pred = pipe.predict(x_train)

print(pipe.score(x_train, y_train))#0.975625
print(pipe.score(x_test, y_test)) #0.965

joblib.dump(pipe, 'predictPrice.pkl')
'''
from project import app
from flask import render_template, redirect, url_for, jsonify, request


from sklearn.externals import joblib
import pandas as pd
import numpy as np
@app.route('/predictPrice', methods=['GET'])
def Create_store():
    arr= np.zeros(21)
    arr[0]=int(request.args.get('battery_power'))
    #arr[1]=int(request.args.get('blue'))
    #arr[2]=int(request.args.get('clock_speed'))
    #arr[3]=int(request.args.get('dual_sim'))    
    #arr[4]=int(request.args.get('fc'))
    arr[5]=int(request.args.get('four_g'))
    arr[6]=int(request.args.get('int_memory'))
    #arr[7]=int(request.args.get('m_dep'))
    arr[8]=int(request.args.get('mobile_wt'))
    arr[9]=int(request.args.get('n_cores'))
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

    pipe = joblib.load('../public/predictPrice.pkl')
    pred = pd.Series(pipe.predict([arr]))
    return jsonify(pred)