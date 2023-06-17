import streamlit as st
import pickle
import numpy as np

file=open('credits_predict_model.pkl','rb')
classifier=pickle.load(file)
def show_predict_page():
    st.title("Credit Score Classifier")
    st.write("### Kindly enter your Details:")
    annual_income=st.number_input("Enter Annual Income: ")
    num_ccard=st.slider("Number of Credit Cards:",0,15,1)
    num_loans = st.number_input("Enter Number of Loans taken: ")
    interest_rate = st.number_input("Enter Interest Rate: ")
    mix_choice = ['Good', 'Bad', 'Standard']
    Credit_Mix = st.selectbox("Credit Mix", mix_choice)
    if Credit_Mix=="Good":
        Credit_Mix=1.0
    elif Credit_Mix=="Standard":
        Credit_Mix=2.0
    else:
        Credit_Mix=0.0
    credit_history_age = st.number_input("Enter Credit History Age:")
    debt=st.number_input("Enter total debt:")
    monthly_balnce=st.number_input("Enter Monthly Balance")

    ok=st.button("Predict Credit Score")
    if ok:
        X=np.array([[annual_income,num_ccard,interest_rate,num_loans,Credit_Mix,debt,credit_history_age,monthly_balnce]])
        score=classifier.predict(X)
        if score[0]==0:
            st.subheader("The predicted credit score is: GOOD")
        elif score[0]==1:
            st.subheader("The predicted credit score is: STANDARD")
        else:
            st.subheader("The predicted credit score is: POOR")









