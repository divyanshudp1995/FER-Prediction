import streamlit as st
import pickle

st.set_option('deprecation.showfileUploaderEncoding',False) 
model = pickle.load(open('india.pkl','rb'))

page = st.sidebar.selectbox("Select your Country", ("India", "Australia", "Canada", "Switzerland", "UK", "Brazil", "Japan", "China"))
if page == "India":
    #show_predict_page()
elif page == "Australia":
    #show_predict_page_2()
elif page == "Canada":
    #show_predict_page_3()
elif page == "Switzerland":
    #show_predict_page_4()
elif page == "UK":
    #show_predict_page_5()
elif page == "Brazil":
    #show_predict_page_6()
elif page == "Japan":
    #show_predict_page_7()
elif page == "China":
    #show_predict_page_8()
    
st.title("Loan Predicition")

st.write("""### We need some information to predict the loan predicition""")

st.write(""" ### Model - Linear Regression""")



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
