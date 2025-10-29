import streamlit as st
st.header('Student database')
name = st.text_input('Please enter student name')

cola,colb = st.columns(2)

with cola:
    math = st.number_input('Please enter your Math Score',0,100)
   
    english = st.number_input('Please enter your English Score',0,100)

with colb:
    science = st.number_input('Please enter your Science Score',0,100)    
    history = st.number_input('Please enter your History Score',0,100)    

if st.button('Submit'):
    total = math + english + science + history
    average = total/4
