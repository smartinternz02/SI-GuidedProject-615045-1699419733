from flask import Flask, render_template, request, redirect
import joblib

app = Flask(__name__, static_folder='static')

model = joblib.load('fetalai_final.pkl')  

@app.route('/')
def front():
    return render_template('index.html')

@app.route('/input')
def index():
    return render_template('input.html')

@app.route('/ben')
def ben():
    return redirect('https://health.gov/myhealthfinder/pregnancy/doctor-and-midwife-visits/have-healthy-pregnancy#the-basics-tab')

@app.route('/ankit')
def ankit():
    return redirect('https://www.linkedin.com/in/ankit-kommalapati-153aa8248/')

@app.route('/madhuri')
def madhuri():
    return redirect('https://www.linkedin.com/in/madhuri-sirasanagandla-988957232/')

@app.route('/amarnath')
def amarnath():
    return redirect('https://www.linkedin.com/in/amarnath-chigurupati-3a1b5b238')

@app.route('/surya')
def surya():
    return redirect('https://www.linkedin.com/in/surya-sikhakolli-b21b84260/')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the HTML form
    acc = float(request.form['acc'])
    ld = float(request.form['ld'])
    fm = float(request.form['fm'])
    uc = float(request.form['uc'])
    asv = float(request.form['asv'])
    msv = float(request.form['msv'])
    plv = float(request.form['plv'])
    hma = float(request.form['hma'])
    m = float(request.form['m'])
    hn = float(request.form['hn'])

    # Make a prediction
    input_data = [[acc, ld, fm, uc, asv, msv, plv, hma, m, hn]]
    prediction = model.predict(input_data)

    # Pass the prediction to the result page
    return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
