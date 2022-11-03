import pickle
from flask import Flask, request, render_template, url_for
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 8)
    loaded_model = pickle.load(open("/home/changcw/covid-prediction/static/pkl/xgboost_1.3.1_new.pkl", "rb"))
    result = loaded_model.predict_proba(to_predict)
    return round(result[0][1]*100, 2)
 
@app.route('/', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)
        # if int(result)== 1:
        #     prediction = 'COVID-19 confirmed'
        # else:
        #     prediction = 'COVID-19 not confirmed'
        return render_template("index.html", prediction = result)

if __name__ == '__main__':
    app.run(debug=True)