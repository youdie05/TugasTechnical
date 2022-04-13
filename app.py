from flask import Flask, render_template, url_for, redirect, request
import pickle
import joblib


app = Flask(__name__)
# model = pickle.load(open('./model/berat_badan_model_linreg.pkl', 'rb'))
model = joblib.load(open('./model/berat_badan_model_linreg.pkl', 'rb'))

@app.route('/')
def home():
	return redirect(url_for('predict_weight'))

@app.route('/predict_weight', methods = ['GET', 'POST'])
def predict_weight():

	if request.method == 'POST':
		gender = request.form['gender']
		height = request.form['height']
		height = float(height)
		weight = model.predict([[gender,height]])
		return render_template("index.html", weight = weight[0])
	return render_template("index.html")


if __name__ == '__main__':
	app.run(debug = True)