
from urllib.request import urlopen
import streamlit as st
import pandas as pd
import numpy as np
#import shap
import xgboost
from xgboost import XGBRegressor

st.write("""
# IPL Player Value Prediction App
This app predicts the **player value** in IPL!""")
st.write("""Data is obtained from [Cricmetric](http://www.cricmetric.com/ipl/ranks/).""")

st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/adityarc19/IPL-analysis/main/data/2020.csv)
""")

# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
    input_df = input_df.drop(['Rank','Player','Team'], axis=1)
    input_df['Salary'] = input_df['Salary'].str.replace(',', '').str.replace('$', '').astype(float)
    input_df = input_df.fillna('0')
else:
    def user_input_features():
        RAA = st.sidebar.slider('RAA', -292.00, 410.00, -21.00)
        Wins = st.sidebar.slider('Wins', -0.98, 1.41, -0.07)
        EFscore = st.sidebar.slider('EFscore', 0.00, 0.24, 0.04)
        Salary = st.sidebar.slider('Salary', 15000.00, 2656250.00, 581584.48)
        data = {'RAA': RAA,
                'Wins': Wins,
                'EFscore': EFscore,
                'Salary': Salary
                }
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()


# Displays the user input features
st.subheader('User Input features')

if uploaded_file is not None:
    st.write(input_df)
else:
    st.write('Awaiting CSV file to be uploaded. Currently using sidebar input parameters (shown below).')
    st.write(input_df)

train_df = pd.read_csv('https://github.com/adityarc19/IPL-player-value-prediction/raw/main/data/full-data.csv')
values = {'Salary': 0}
train_df = train_df.fillna(value=values)

X = train_df[['RAA', 'Wins', 'EFscore', 'Salary']]
y = train_df[['Value']]

xgb_model = XGBRegressor().fit(X, y)

# Apply model to make predictions
prediction = xgb_model.predict(input_df)

st.header('Prediction of Value (in currency)')
st.write(prediction)
st.write('---')

# Explaining the model's predictions using SHAP values
# https://github.com/slundberg/shap
# explainer = shap.TreeExplainer(xgb_model)
# shap_values = explainer.shap_values(X)

# st.header('Feature Importance')
# plt.title('Feature importance based on SHAP values')
# shap.summary_plot(shap_values, X)
# st.pyplot(bbox_inches='tight')
# st.write('---')

# plt.title('Feature importance based on SHAP values (Bar)')
# shap.summary_plot(shap_values, X, plot_type="bar")
# st.pyplot(bbox_inches='tight')


st.write("""For understanding more on how 'player value' is calculated and the other details of the implementation, check out --> [Github repo](https://github.com/adityarc19/IPL-player-value-prediction)""")
