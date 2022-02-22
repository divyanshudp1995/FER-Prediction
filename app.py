import streamlit as st
import pickle

st.set_option('deprecation.showfileUploaderEncoding',False) 
model = pickle.load(open('india.pkl','rb'))

gender = st.selectbox("Gender",gender_1)
marital_status = st.selectbox("Marital Status",marital_status)
education = st.selectbox("Education",education)
credit = st.selectbox("Credit Score",credit_history)
income = st.slider("Income (in $)", 0, 100000, 1000,100)
loan_amount = st.slider("Loan Amount (in $)", 0, 1000, 100,10)
loan_amount_term = st.slider("Loan Amount Term (in months)", 0, 480, 40,20)
