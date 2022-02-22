import streamlit as st
import pickle

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
    

gender_1 = {
"Male",
"Female",
}

marital_status = {
"Yes",
"No",
}

education = {
"Graduate",
"Not Graduate",
}

credit_history = {
"1",
"0",
}



gender = st.selectbox("Gender",gender_1)
marital_status = st.selectbox("Marital Status",marital_status)
education = st.selectbox("Education",education)
credit = st.selectbox("Credit Score",credit_history)
income = st.slider("Income (in $)", 0, 100000, 1000,100)
loan_amount = st.slider("Loan Amount (in $)", 0, 1000, 100,10)
loan_amount_term = st.slider("Loan Amount Term (in months)", 0, 480, 40,20)

ok = st.button("Calculate Loan Status")
if ok:
  st.subheader(f"The Loan Approval Status  - " + " ")
