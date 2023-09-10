import pickle
import json
import streamlit as st
import numpy as np

st.title('Banglore House Price Prediction')
location = str(st.text_input('Location'))
total_sqr_ft = st.text_input('Total Area (in square foot)')
bhk = st.text_input('No. of Bedrooms')
bath = st.text_input('No. of Bathrooms')

model = pickle.load(open('banglore_home_prices_model.pickle', 'rb'))
columns = json.load(open('columns.json', 'r'))['data_columns']


def get_estimated_price(region, sqft, bath, bhk):
    try:
        loc_index = columns.index(region.lower())
    except:
        loc_index = -1

    x = np.zeros(len(columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(model.predict([x])[0], 2)
estimate = 0
if st.button('Predict Price'):
    estimate = get_estimated_price(location, total_sqr_ft, bath, bhk)

st.subheader('Predicted Price:')
st.header(f':green[{round(estimate * 100000 / 83120, 2)} Thousand Dollars]')
