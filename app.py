
import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('html.html')

@app.route('/predict',methods=['POST'])
def predict():
    age=int(request.value['age'])
    weight=int(request.value['weight'])
    attack=int(request.value['ATTACK'])
    midfiled=int(request.value['MIDFILED'])
    defence=int(request.value['DEFENCE'])
    mentality=int(request.value['MENTALITY'])
    foot=request.values['foot']
    if(foot==RIGHT):
        foot=0
    else:
        foot=1
    work=request.values['wr']
    if(work=='LOW\LOW'):
        work=1
    elif(work=='LOW\MEDIUM'):
        work=2
    elif(work=='LOW\HIGH'):
            work=3
    elif(work=='MEDIUM\LOW'):
            work=4
    elif(work=='MEDIUM\MEDIUM'):
            work=5
    elif(work=='MEDIUM\HIGH'):
            work=6
    elif(work=='HIGH\LOW'):
            work=7
    elif(work=='HIGH\MEDIUM'):
        work=8
    elif(work=='HIGH\HIGH'):
            work=9
    else:
            work=0
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = prediction
    return render_template('html.html', prediction_text='Player Rating is {}'.format(output))

        

if __name__=="__main__":
    app.run(debug=True)