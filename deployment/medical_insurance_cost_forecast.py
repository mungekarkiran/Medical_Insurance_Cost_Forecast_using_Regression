import pickle

def predict(input_val):
    sc = pickle.load(open('../model/medical_insurance_cost_forecast_scaler.pkl', 'rb'))
    model = pickle.load(open('../model/medical_insurance_cost_forecast_model.pkl', 'rb')) 
    pred_val = model.predict(sc.transform(input_val))[0]
    return round(pred_val, 2)
    