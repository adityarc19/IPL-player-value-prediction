
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import OrthogonalMatchingPursuit

st.write("""
# IPL Player Value Prediction App
This app predicts the **player value** in IPL!
Data obtained from [Cricmetric](http://www.cricmetric.com/ipl/ranks/).
""")

st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/adityarc19/IPL-analysis/main/data/2020.csv)
""")

# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader(
    "Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    def user_input_features():
        Team = st.sidebar.selectbox('Team', ('Mumbai Indians', 'Kings XI Punjab', 'Delhi Capitals', 
        'Royal Challengers Bangalore', 'Sunrisers Hyderabad', 'Chennai Super Kings', 'Rajasthan Royals', 'Kolkata Knight Riders'))
        RAA = st.sidebar.slider('RAA', -292.00, -21.00, 410.00)
        Wins = st.sidebar.slider('Wins', -0.98, -0.07, 1.41)
        EFscore = st.sidebar.slider('EFscore', 0.00, 0.04, 0.24)
        data = {'Team': Team,
                'RAA': RAA,
                'Wins': Wins,
                'EFscore': EFscore}
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()

# Main Panel

# Print specified input parameters
st.header('Specified Input parameters')
st.write(input_df)
st.write('---')

# Reads in saved classification model
load_reg = pickle.load(open('https://github.com/adityarc19/IPL-player-value-prediction/blob/main/model.pkl?raw=true', 'rb'))

# Apply model to make predictions
prediction = load_reg.predict(input_df)
prediction_proba = load_reg.predict_proba(input_df)


