import joblib
from flask import Flask, request, app, jsonify, url_for, render_template, redirect
import pandas
import numpy
app=Flask(__name__)
model=joblib.load(r"D:\End to end project\End_to_End_Bitcoin_Project\Deep_learning_Stock_Prediction1",'rb')
scaler=joblib.load(r"D:\End to end project\End_to_End_Bitcoin_Project\StandardScaler1")
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    new_data=scaler.transform(numpy.array(list(data.values())).reshape(1,-1))
    output=model.predict(new_data)
    print(output)
    return jsonify(output[0])
if __name__=="__main__":
    app.run(debug=True)
    