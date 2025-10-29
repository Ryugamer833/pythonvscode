import streamlit as st
numbers1 = st.number_input('Please enter the first number',0)
numbers2 = st.number_input('Please enter the second number',0)
multiplication = numbers1 * numbers2
addition = numbers1 + numbers2
numbersdict = {'First Number':[numbers1],'Numbers2':[numbers2],'Multiplication': [multiplication],'Addition':[addition]}
st.write(numbersdict)
st.table(numbersdict)