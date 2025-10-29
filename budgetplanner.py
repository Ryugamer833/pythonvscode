import streamlit as st
name = st.text_input('What is your name')
monthly_income = st.number_input('What is your total monthly income')
rent = st.number_input('What is your monthly rent')
groceries = st.number_input('What is your monthly groceries expense')
transportation = st.number_input('What is your monthly tansportation cost')
other_expenses = st.number_input('What are your other ')