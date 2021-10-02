from flask import Flask,render_template,request,session
import pandas as pd

from sklearn.metrics import accuracy_score
import joblib

app = Flask(__name__)



@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/prediction')
def predict():
    return render_template('prediction.html')

@app.route('/prediction1',methods =["POST","GET"])
def pred():
    s = []
    if request.method== "POST":
        age = request.form['age']
        job = request.form['job']
        salary = request.form['salary']
        education = request.form['education']
        defaults = request.form['default']
        balance = request.form['balance']
        housing = request.form['housing']
        loan = request.form['loan']
        campaign = request.form['campaign']

        s.extend([age,job,salary,education,defaults,balance,housing,loan,campaign])
        model = joblib.load('varu.pkl')
        Y_pred = model.predict([s])
        return render_template('prediction.html',msg="success",op=Y_pred)


if __name__ == '__main__':
    app.secret_key="hai"
    app.run(debug=True)