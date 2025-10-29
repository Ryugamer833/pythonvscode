import streamlit as st
#classwork: create a simple church form with 3 columns
#1 ask for the name (text), type their age and choose their gender (st.radio) on 3 columns]

#HINT1 gender = st.radio('Please choose your gender',['Male','Female'])
#put a message box incase user has a message for the pastor
#HINT2 message = st.text_area('Send a message to the pastor',height=200)

# decide member class with these categories: (Kids(3-12), Teens(13-19), Youth(20-35), Adult(36-64), Elders(65+) --== if block
#HINT3 if age >= 3 and age <=12:
#     churchclass = 'Kids

# when you click on submit button:
#Make sure you group members in different category based on their age
#write this welcome [name], you will be in the [churchclass] class

#your message has been received and will be sent to the pastor
#show the user message here


membersdict = col1,col2,col3 = st.columns (3)


with col1:
    name = st.text_input('What is your name')



with col2:
    gender = st.selectbox('What is your gender',['Female','Male'])


with col3:
    age = st.number_input('What is your age',0) 


if age>= 3 and age<= 12:
    churchclass = 'kid'


elif age>= 13 and age<= 19:
    churchclass = 'Teen' 



elif age>=20 and age<=35:
    churchclass = 'Youth'     



elif age>=36 and age<=64:
    churchclass = 'Adult'         



elif age >= 65:
    churchclass = 'Elders'




message = st.text_area('Send message to pastor')

if st.button('submit'):
    st.write ('Hello',name,'You will be in the',churchclass,'church class')
    st.info(message)
    