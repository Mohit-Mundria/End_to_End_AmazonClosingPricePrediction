import joblib
from flask import Flask, request, app, jsonify, url_for, render_template, redirect
import pandas
import numpy
app=Flask(__name__)
model=joblib.load("Deep_learning_Stock_Prediction1")
scaler=joblib.load("StandardScaler1")
@app.route('/')
def home():
    return render_template('home.html')

# This is the decorator(function) do the prediction by the help of API. API by Postman Software
@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    new_data=scaler.transform(numpy.array(list(data.values())).reshape(1,-1))
    output=model.predict(new_data)
    print(output)
    
    #Here we convert the numpy array to regular python type data so that it can convert into jsonify as numpy array can't 
    # convert directly into json datatype.
    predicted_price = float(output[0])
    return jsonify({'prediction_text': f"Predicted Closing Price for is ${predicted_price:.2f}"})

# Now make a decorator(function) that enable us to give our input data on web application only not through API.
@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scaler.transform(numpy.array(data).reshape(1,-1))
    print(final_input)
    output=model.predict(final_input)[0]
    return render_template("home.html", prediction_text="The Closing price is {}".format(output))

if __name__=="__main__":
    app.run(debug=True)
    
