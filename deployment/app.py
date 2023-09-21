# lib's
from flask import Flask, render_template, request, jsonify
from medical_insurance_cost_forecast import predict
import numpy as np

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
        
        input_val = np.array([val])
        pred_val = predict(input_val)
        
        return render_template('home.html', msg = pred_val)
        
if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=False,host='0.0.0.0', port=5000)



