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
        
        age = float(request.form.get('age'))
        blood_pressure = float(request.form.get('blood_pressure'))
        specific_gravity = float(request.form.get('specific_gravity'))
        albumin = float(request.form.get('albumin'))
        sugar = float(request.form.get('sugar'))
        red_blood_cells = float(request.form.get('red_blood_cells'))
        pus_cell = float(request.form.get('pus_cell'))
        pus_cell_clumps = float(request.form.get('pus_cell_clumps'))
        bacteria = float(request.form.get('bacteria'))
        blood_glucose_random = float(request.form.get('blood_glucose_random'))
        blood_urea = float(request.form.get('blood_urea'))
        serum_creatinine = float(request.form.get('serum_creatinine'))
        sodium = float(request.form.get('sodium'))
        potassium = float(request.form.get('potassium'))
        haemoglobin = float(request.form.get('haemoglobin'))
        packed_cell_volume = float(request.form.get('packed_cell_volume'))
        white_blood_cell_count = float(request.form.get('white_blood_cell_count'))
        red_blood_cell_count = float(request.form.get('red_blood_cell_count'))
        hypertension = float(request.form.get('hypertension'))
        diabetes_mellitus = float(request.form.get('diabetes_mellitus'))
        coronary_artery_disease = float(request.form.get('coronary_artery_disease'))
        appetite = float(request.form.get('appetite'))
        peda_edema = float(request.form.get('peda_edema'))
        aanemia = float(request.form.get('aanemia'))

        input_list = np.array([age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, pus_cell, pus_cell_clumps, bacteria, blood_glucose_random, blood_urea, serum_creatinine, sodium, potassium, haemoglobin, packed_cell_volume, white_blood_cell_count, red_blood_cell_count, hypertension, diabetes_mellitus,  coronary_artery_disease, appetite, peda_edema, aanemia])
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



