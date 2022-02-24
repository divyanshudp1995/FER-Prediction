import streamlit as st
import pickle
import numpy as np

st.set_option('deprecation.showfileUploaderEncoding',False) 
model_india1 = pickle.load(open('india.pkl','rb'))
model_uk1 = pickle.load(open('uk.pkl','rb'))
model_canada1 = pickle.load(open('canada.pkl','rb'))
model_brazil1 = pickle.load(open('brazil.pkl','rb'))
model_australia1 = pickle.load(open('australia.pkl','rb'))
model_switzerland1 = pickle.load(open('switzerland.pkl','rb'))
model_japan1 = pickle.load(open('japan.pkl','rb'))
model_china1 = pickle.load(open('china.pkl','rb'))

st.title("Foreign Exchange Rate Prediction")
st.write("***Please select the country from the side bar***")
st.write("Please enter the following information")

page = st.sidebar.selectbox("Select your Country", ("India", "Australia", "Canada", "Switzerland", "UK", "Brazil", "Japan", "China"))
if page == "India":
    PPP = st.number_input('PPP')
    GDP = st.number_input('Gross Domestic Product')
    INV = st.number_input('Investment')
    GDPPER = st.number_input('GDP per Capita')
    EXP = st.number_input('Exports')
    Topic2 = st.number_input('Proportion of Articles in Topic 2 (Social Media)')
    Topic3 = st.number_input('Proportion of Articles in Topic 3 (Finance)')
    Topic5 = st.number_input('Proportion of Articles in Topic 5 (Business)')
    
    ok = st.button("Calculate Foreign Exchange Rate")
    if ok:
        x = np.array([[PPP, Topic5, GDP, Topic2, INV, Topic3, GDPPER, EXP]])
        #x = x.astype(float)

        fer_india = model_india1.predict(x)
        st.subheader(f"The Foreign Exchange Rate is {fer_india}")

elif page == "Australia":
    INF = st.number_input('Inflation')
    GDP = st.number_input('Gross Domestic Product')
    INV = st.number_input('Investment')
    GDPPER = st.number_input('GDP per Capita')
    Topic3 = st.number_input('Proportion of Articles in Topic 3 (Finance)')
    
    ok = st.button("Calculate Foreign Exchange Rate")
    if ok:
        x = np.array([[INV, GDP, INF, Topic3, GDPPER]])
        #x = x.astype(float)

        fer_australia = model_australia1.predict(x)
        st.subheader(f"The Foreign Exchange Rate is {fer_australia}")
        
elif page == "Canada":
    GDP = st.number_input('Gross Domestic Product')
    INV = st.number_input('Investment')
    GDPPER = st.number_input('GDP per Capita')
    Topic3 = st.number_input('Proportion of Articles in Topic 3 (Finance)')
    
    ok = st.button("Calculate Foreign Exchange Rate")
    if ok:
        x = np.array([[INV, GDP, Topic3, GDPPER]])
        #x = x.astype(float)

        fer_canada = model_canada1.predict(x)
        st.subheader(f"The Foreign Exchange Rate is {fer_canada}")
        
elif page == "Switzerland":
    PPP = st.number_input('PPP')
    GDP = st.number_input('Gross Domestic Product')
    INV = st.number_input('Investment')
    INF = st.number_input('Inflation')
    Topic2 = st.number_input('Proportion of Articles in Topic 2 (Social Media)')
    Topic3 = st.number_input('Proportion of Articles in Topic 3 (Finance)')
    Topic5 = st.number_input('Proportion of Articles in Topic 5 (Business)')
    
    ok = st.button("Calculate Foreign Exchange Rate")
    if ok:
        x = [[GDP, PPP, Topic5, Topic2, INF,  INV, Topic3]]
        #x = x.astype(float)

        fer_switzerland = model_switzerland1.predict(x)
        st.subheader(f"The Foreign Exchange Rate is {fer_switzerland}")
        
elif page == "UK":
    Topic1 = st.number_input('Proportion of Articles in Topic 1 (Market)')
    Topic4 = st.number_input('Proportion of Articles in Topic 4 (Politics)')
    
    ok = st.button("Calculate Foreign Exchange Rate")
    if ok:
        x = np.array([[Topic1, Topic4]])
        #x = x.astype(float)

        fer_uk = model_uk1.predict(x)
        st.subheader(f"The Foreign Exchange Rate is {fer_uk}")
        
elif page == "Brazil":
    PPP = st.number_input('PPP')
    GDP = st.number_input('Gross Domestic Product')
    Topic2 = st.number_input('Proportion of Articles in Topic 2 (Social Media)')
    Topic3 = st.number_input('Proportion of Articles in Topic 3 (Finance)')
    Topic5 = st.number_input('Proportion of Articles in Topic 5 (Business)')
    
    ok = st.button("Calculate Foreign Exchange Rate")
    if ok:
        x = np.array([[PPP, Topic2, Topic5, Topic3, GDP]])
        #x = x.astype(float)

        fer_brazil = model_brazil1.predict(x)
        st.subheader(f"The Foreign Exchange Rate is {fer_brazil}")
        
elif page == "Japan":
    PPP = st.number_input('PPP')
    GDP = st.number_input('Gross Domestic Product')
    INV = st.number_input('Investment')
    GDPPER = st.number_input('GDP per Capita')
    INF = st.number_input('Inflation')
    Topic2 = st.number_input('Proportion of Articles in Topic 2 (Social Media)')
    Topic5 = st.number_input('Proportion of Articles in Topic 5 (Business)')
    
    ok = st.button("Calculate Foreign Exchange Rate")
    if ok:
        x = np.array([[GDP, PPP, Topic5, INF, Topic2, INV, GDPPER]])
        #x = x.astype(float)

        fer_japan = model_japan1.predict(x)
        st.subheader(f"The Foreign Exchange Rate is {fer_japan}")
        
elif page == "China":
    PPP = st.number_input('PPP')
    INV = st.number_input('Investment')
    Topic1 = st.number_input('Proportion of Articles in Topic 1 (Market)')
    Topic2 = st.number_input('Proportion of Articles in Topic 2 (Social Media)')
    Topic3 = st.number_input('Proportion of Articles in Topic 3 (Finance)')
    Topic5 = st.number_input('Proportion of Articles in Topic 5 (Business)')
    
    ok = st.button("Calculate Foreign Exchange Rate")
    if ok:
        x = np.array([[Topic2, PPP, Topic5, Topic1, INV, Topic3]])
        #x = x.astype(float)

        fer_china = model_china1.predict(x)
        st.subheader(f"The Foreign Exchange Rate is {fer_china}")
    
