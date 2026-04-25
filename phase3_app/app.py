from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            duration = float(request.form['duration'])
            votes = float(request.form['votes'])
            year = float(request.form['year'])
            reviews_users = float(request.form['reviews_from_users'])
            reviews_critics = float(request.form['reviews_from_critics'])

            input_data = np.array([[duration, votes, year, reviews_users, reviews_critics]])
            prediction = model.predict(input_data)[0]
        except:
            prediction = "Invalid input. Please enter numbers only."
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)