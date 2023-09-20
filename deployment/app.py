# lib's
from flask import Flask, render_template, request, jsonify
import numpy as np
import time
import pickle

# start app
app = Flask(__name__)

# routing
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/getResult', methods=['POST'])
def getResult():
    if request.method == 'POST':
        # age, sex, bmi, smoker, children, region_northwest, region_southeast, region_southwest
        age = int(request.form.get('age'))
        sex = int(request.form.get('sex'))
        bmi = float(request.form.get('bmi'))
        smoker = int(request.form.get('smoker'))
        children = int(request.form.get('children'))
        region = request.form.get('children')
        val = [age, sex, bmi, smoker, children]
        
        if region == 'northwest':
            val.extend([1, 0, 0])
        elif region == 'southeast':
            val.extend([0, 1, 0])
        elif region == 'southwest':
            val.extend([0, 0, 1])
        else:
            val.extend([0, 0, 0])
        
        input_list = np.array(val)
        
        rf_model = pickle.load(open('models//rf_Classifier.pkl', 'rb')) 
        rf_pred = rf_model.predict([input_list])[0]
        print(rf_pred)
        if rf_pred == 0:
            msg = 'Patient have a Chronic Kidney Disease and need to received medical treatment from a doctor.'
        else:
            msg = 'Patient not have a Chronic Kidney Disease.'
        return render_template('home.html', msg = msg)
        

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False,host='0.0.0.0', port=5000)



