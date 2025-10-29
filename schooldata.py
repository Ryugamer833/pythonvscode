import streamlit as st
elementary_fee = 5000
college_fee = 15000
parents_name = st.text_input('What is your name')
elementary_kids = st.number_input('How many of your kids are in elementary',0)
college_kids = st.number_input('How many of your kids are in college',0)
Collegekidsfee = college_kids * college_fee 
elementarykidsfee = elementary_kids * elementary_fee
total_fee = Collegekidsfee + elementarykidsfee
school_dict = {'Parents Name':[parents_name],'Elemantary Kids':[elementary_kids],'College kids':[college_kids],'College fee':[college_fee],'Elemantary Fee':[elementary_fee],'Total fee':[total_fee]}
st.write(school_dict)
st.table(school_dict)