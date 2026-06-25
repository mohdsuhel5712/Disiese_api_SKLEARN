from flask import Flask, render_template, request,url_for
from model import predict_disease

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    fever = int(request.form['fever'])
    cough = int(request.form['cough'])
    headache = int(request.form['headache'])
    fatigue = int(request.form['fatigue'])

    result = predict_disease(fever,cough,headache,fatigue)

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)