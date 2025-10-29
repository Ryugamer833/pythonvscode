import streamlit as st

import pandas as pd 

try:
 churchlink = pd.read_csv('churchform.csv')
except: 
 churchlink = pd.DataFrame

name = st.text_input('Waht is your name')

age = st.number_input('What is your age',0)

Gender = st.radio('What is your gender',{'Male','Female'})

Volunteer_unit = st.selectbox('What is your volunteer unit',['None','Cleaning','Ushering','Security'])

if age >= 3 and age <= 12:
    agegroup = ('kid')

elif age >= 13 and age <=19:
    agegroup = ('teen')

elif age >= 20 and age<= 35:
    agegroup = ('Youth')

elif age >= 36 and age <= 64:
    agegroup = ('Adult')

elif age >= 65:
    agegroup = ('Elderly')

if st.button('Submit Information'):
 
 membersdict = {'Name ':[name],'Age':[age],'Volunteer Unit':[Volunteer_unit],'Agegroup':[agegroup]}
 st.write(membersdict)
 st.table(membersdict)