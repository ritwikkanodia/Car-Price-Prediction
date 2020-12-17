import pandas as pd
import pickle



with open('column_transformer', 'rb') as f:
    column_transformer = pickle.load(f)

with open('rf.model', 'rb') as f:
    rf_model = pickle.load(f)

def predict(data):
    return rf_model.predict(column_transformer.transform(data))


if __name__ == '__main__':
    test_data = pd.read_csv('CarPrice_Assignment.csv')
    test_data = test_data.drop(['car_ID', 'price', 'CarName'], axis=1)
    print(test_data.columns)
    for i in test_data.columns:
        print(i, ": ", type(test_data[str(i)][0]))
    print(predict(test_data.iloc[[20]]))
