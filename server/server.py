from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/predict_machine_price', methods=['GET', 'POST'])
def predict_machine_price():
    symboling = int(request.form['symboling'])
    fueltype = str(request.form['fueltype'])
    aspiration = str(request.form['aspiration'])
    doornumber = str(request.form['doornumber'])
    carbody = str(request.form['carbody'])
    drivewheel = str(request.form['drivewheel'])
    enginelocation = str(request.form['enginelocation'])
    wheelbase = float(request.form['wheelbase'])
    carlength = float(request.form['carlength'])
    carwidth = float(request.form['carwidth'])
    carheight = float(request.form['carheight'])
    curbweight = int(request.form['curbweight'])
    enginetype = str(request.form['enginetype'])
    cylindernumber = str(request.form['cylindernumber'])
    enginesize = int(request.form['enginesize'])
    fuelsystem = str(request.form['fuelsystem'])
    boreratio = float(request.form['boreratio'])
    stroke = float(request.form['stroke'])
    compressionratio = float(request.form['compressionratio'])
    horsepower = int(request.form['horsepower'])
    peakrpm = int(request.form['peakrpm'])
    citympg = int(request.form['citympg'])
    highwaympg = int(request.form['highwaympg'])
    print("wheel base 1: ", highwaympg)
    response = jsonify({
        # populate the estimated price to the frontend
        'estimated_price': util.get_predicted_price(symboling, fueltype, aspiration, doornumber, carbody, drivewheel,
                                                    enginelocation, wheelbase,
                                                    carlength, carwidth, carheight,
                                                    curbweight, enginetype, cylindernumber, enginesize, fuelsystem,
                                                    boreratio,
                                                    stroke, compressionratio, horsepower, peakrpm, citympg, highwaympg)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_model()
    app.run(debug=True)
