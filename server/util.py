import pickle
import json
import numpy as np
import pandas as pd

__model = None
__column_transformer = None


def get_predicted_price(symboling, fueltype, aspiration, doornumber, carbody, drivewheel, enginelocation, wheelbase,
                        carlength, carwidth, carheight,
                        curbweight, enginetype, cylindernumber, enginesize, fuelsystem, boreratio,
                        stroke, compressionratio, horsepower, peakrpm, citympg, highwaympg):

    feat_dict = {'symboling': symboling, 'fueltype': fueltype, 'aspiration': aspiration, 'doornumber': doornumber,
                 'carbody':carbody, 'drivewheel': drivewheel, 'enginelocation': enginelocation, 'wheelbase': wheelbase,
                 'carlength': carlength, 'carwidth': carwidth, 'carheight': carheight, 'curbweight': curbweight,
                 'enginetype': enginetype, 'cylindernumber': cylindernumber, 'enginesize': enginesize, 'fuelsystem': fuelsystem,
                 'boreratio': boreratio, 'stroke': stroke, 'compressionratio': compressionratio, 'horsepower': horsepower,
                 'peakrpm': peakrpm, 'citympg': citympg, 'highwaympg': highwaympg}

    x = pd.DataFrame(feat_dict, index=[0])

    # x = np.zeros(23)
    # x[0] = symboling
    # x[1] = fueltype
    # x[2] = aspiration
    # x[3] = doornumber
    # x[4] = carbody
    # x[5] = drivewheel
    # x[6] = enginelocation
    # x[7] = wheelbase
    # x[8] = carlength
    # x[9] = carwidth
    # x[10] = carheight
    # x[11] = curbweight
    # x[12] = enginetype
    # x[13] = cylindernumber
    # x[14] = enginesize
    # x[15] = fuelsystem
    # x[16] = boreratio
    # x[17] = stroke
    # x[18] = compressionratio
    # x[19] = horsepower
    # x[20] = peakrpm
    # x[21] = citympg
    # x[22] = highwaympg
    # # x = x.reshape(1, -1)
    ''' The inference is not working for now as the categorical variables do not have appropriate values'''
    # print("Hi")
    # return symboling
    # print("symboling: ", symboling)
    # print("wheel base: ", wheelbase)
    # for i in x.columns:
    #     print(i, ": ", type(x[str(i)][0]))
    # print("Prediction: ", __model.predict(__column_transformer.transform(x)))
    return round(__model.predict(__column_transformer.transform(x))[0], 2)


def load_saved_model():
    print("Loading the ML model...start")
    global __model
    global __column_transformer
    if __model is None:
        with open('../model/rf.model', 'rb') as f:
            __model = pickle.load(f)
    if __column_transformer is None:
        with open('../model/column_transformer', 'rb') as f:
            __column_transformer = pickle.load(f)
    print("Loading ML model...done")
