import streamlit as st
import pickle
import numpy as np

st.set_option('deprecation.showfileUploaderEncoding',False) 
model_india = pickle.load(open('india1.pkl','rb'))
model_uk = pickle.load(open('uk1.pkl','rb'))
model_canada = pickle.load(open('canada1.pkl','rb'))
model_brazil = pickle.load(open('brazil1.pkl','rb'))
model_australia = pickle.load(open('australia1.pkl','rb'))
model_switzerland = pickle.load(open('switzerland1.pkl','rb'))
model_japan = pickle.load(open('japan1.pkl','rb'))
model_china = pickle.load(open('china1.pkl','rb'))

st.title("Foreign Exchange Rate Prediction")
st.write("*Please select the country from the side bar*")
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
    
    ok = st.button("Calculate Foreign Exchange Rate")
    if ok:
        x = np.array([[PPP, GDP, INV, GDPPER, EXP, Topic2, Topic3, Topic5]])
        #x = x.astype(float)

        fer_india = model_india.predict(x)
        st.subheader(f"The Foreign Exchange Rate is {fer_india}")

elif page == "Australia":
    INF = st.number_input('Inflation')
    GDP = st.number_input('Gross Domestic Product')
    INV = st.number_input('Investment')
    GDPPER = st.number_input('GDP per Capita')
    Topic3 = st.number_input('Proportion of Articles in Topic 3')
    
    ok = st.button("Calculate Foreign Exchange Rate")
    if ok:
        x = np.array([[INF, GDP, INV, GDPPER, Topic3]])
        #x = x.astype(float)

        fer_australia = model_australia.predict(x)
        st.subheader(f"The Foreign Exchange Rate is {fer_australia}")
        
elif page == "Canada":
    GDP = st.number_input('Gross Domestic Product')
    INV = st.number_input('Investment')
    GDPPER = st.number_input('GDP per Capita')
    Topic3 = st.number_input('Proportion of Articles in Topic 3')
    
    ok = st.button("Calculate Foreign Exchange Rate")
    if ok:
        x = np.array([[GDP, INV, GDPPER, Topic3]])
        #x = x.astype(float)

        fer_canada = model_canada.predict(x)
        st.subheader(f"The Foreign Exchange Rate is {fer_canada}")
        
elif page == "Switzerland":
    PPP = st.number_input('PPP')
    GDP = st.number_input('Gross Domestic Product')
    INV = st.number_input('Investment')
    INF = st.number_input('Inflation')
    Topic2 = st.number_input('Proportion of Articles in Topic 2')
    Topic3 = st.number_input('Proportion of Articles in Topic 3')
    Topic5 = st.number_input('Proportion of Articles in Topic 5')
    
    ok = st.button("Calculate Foreign Exchange Rate")
    if ok:
        x = np.array([[PPP, GDP, INV, INF, Topic2, Topic3, Topic5]])
        #x = x.astype(float)

        fer_switzerland = model_switzerland.predict(x)
        st.subheader(f"The Foreign Exchange Rate is {fer_switzerland}")
        
elif page == "UK":
    Topic1 = st.number_input('Proportion of Articles in Topic 1')
    Topic4 = st.number_input('Proportion of Articles in Topic 4')
    
    ok = st.button("Calculate Foreign Exchange Rate")
    if ok:
        x = np.array([[Topic1, Topic4]])
        #x = x.astype(float)

        fer_uk = model_uk.predict(x)
        st.subheader(f"The Foreign Exchange Rate is {fer_uk}")
        
elif page == "Brazil":
    PPP = st.number_input('PPP')
    GDP = st.number_input('Gross Domestic Product')
    Topic2 = st.number_input('Proportion of Articles in Topic 2')
    Topic3 = st.number_input('Proportion of Articles in Topic 3')
    Topic5 = st.number_input('Proportion of Articles in Topic 5')
    
    ok = st.button("Calculate Foreign Exchange Rate")
    if ok:
        x = np.array([[PPP, GDP, Topic2, Topic3, Topic5]])
        #x = x.astype(float)

        fer_brazil = model_brazil.predict(x)
        st.subheader(f"The Foreign Exchange Rate is {fer_brazil}")
        
elif page == "Japan":
    PPP = st.number_input('PPP')
    GDP = st.number_input('Gross Domestic Product')
    INV = st.number_input('Investment')
    GDPPER = st.number_input('GDP per Capita')
    INF = st.number_input('Inflation')
    Topic2 = st.number_input('Proportion of Articles in Topic 2')
    Topic5 = st.number_input('Proportion of Articles in Topic 5')
    
    ok = st.button("Calculate Foreign Exchange Rate")
    if ok:
        x = np.array([[PPP, GDP, INV, GDPPER, INF, Topic2, Topic5]])
        #x = x.astype(float)

        fer_japan = model_japan.predict(x)
        st.subheader(f"The Foreign Exchange Rate is {fer_japan}")
        
elif page == "China":
    PPP = st.number_input('PPP')
    INV = st.number_input('Investment')
    Topic1 = st.number_input('Proportion of Articles in Topic 1')
    Topic2 = st.number_input('Proportion of Articles in Topic 2')
    Topic3 = st.number_input('Proportion of Articles in Topic 3')
    Topic5 = st.number_input('Proportion of Articles in Topic 5')
    
    ok = st.button("Calculate Foreign Exchange Rate")
    if ok:
        x = np.array([[PPP, INV, Topic1, Topic2, Topic3, Topic5]])
        #x = x.astype(float)

        fer_china = model_china.predict(x)
        st.subheader(f"The Foreign Exchange Rate is {fer_china}")
    
