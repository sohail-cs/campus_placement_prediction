from http.client import responses
import requests
import streamlit as st

#Create title
st.title("WELCOME TO CAMPUS PLACEMENT PREDICTION MODEL")
st.text('''
         The Model aims to predict where a given candiate will be able to secure campus placement using the candidate details provided
''')

#Get user details
candidate_details = {
    "gender":st.radio("What is the gender of the candidate",("M","F")),
    "ssc_p" :float(st.number_input("What is the percentage acquired in secondary education?")),
    "ssc_b" :st.radio("What is the Secondary education board",("Central","Others")),
    "hsc_p" : float(st.number_input("What is percentage acquired in higher secondary?")),
    "hsc_b" : st.radio("What is the higher secondary education board",("Central","Others")),
    "hsc_s" : st.radio("What is the academic stream pursued?",("Commerce","Science","Arts")),
    "degree_p": float(st.number_input("What is the degree percentage acquired?")),
    "degree_t":st.radio("What is your undergraduate degree type",("Sci&Tech","Comm&Mgmt","Others")),
    "workex": st.radio("Do you have any work experience?",("Yes","No")),
    "etest_p": float(st.number_input("What is the employbility test results obtained:")),
    "specialisation":st.radio("What is your specialisation?",("Mkt&HR","Mkt&Fin")),
    "mba_p": float(st.number_input("What is the mba percentage obtained?"))
}

#Check if submit button is pressed
if st.button("Submit"):
    if all(values !="" for values in candidate_details.values()):
        #Server url
        url = 'http://127.0.0.1:8081'

        try:
            responses = requests.post(url,json=candidate_details)
            if responses.status_code ==200:
                st.text("CONNECTED TO SERVER")
                st.write("RESPONSE FROM SERVER")
                st.write(responses.json())
            else:
                st.text("NOT CONNECTED")
        except :
            st.error("Failed to connect")


    else:
        st.text("PLEASE ENTER ALL DETAILS")



