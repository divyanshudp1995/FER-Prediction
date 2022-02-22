import streamlit as st
import pickle
import numpy as np

st.set_option('deprecation.showfileUploaderEncoding',False) 
model = pickle.load(open('india.pkl','rb'))

st.title("Foreign Exchange Rate Prediction")

st.write("Please enter the following information")

page = st.sidebar.selectbox("Select your Country", ("India", "Australia", "Canada", "Switzerland", "UK", "Brazil", "Japan", "China"))
if page == "India":
    PPP = st.number_input('PPP')
    GDP = st.number_input('Gross Domestic Product')
    INV = st.number_input('Investment')
    GDPPER = st.number_input('GDP per Capita')
    EXP = st.number_input('Exports')
    Topic2 = st.number_input('Proportion of Articles in Topic 2')
    Topic3 = st.number_input('Proportion of Articles in Topic 3')
    Topic5 = st.number_input('Proportion of Articles in Topic 5')
    
    ok = st.button("Calculate Loan Status")
    if ok:
        x = np.array([[PPP, GDP, INV, GDPPER, EXP, Topic2, Topic3, Topic5]])
        #x = x.astype(float)

        fer_india = model.predict(x)
        st.subheader(f"The Foreign Exchange Rate is  - "  " " + fer_india)

elif page == "Australia":
    print(show_predict_page())
elif page == "Canada":
    print(show_predict_page())
elif page == "Switzerland":
    print(show_predict_page())
elif page == "UK":
    print(show_predict_page())
elif page == "Brazil":
    print(show_predict_page())
elif page == "Japan":
    print(show_predict_page())
elif page == "China":
    print(show_predict_page())
    
