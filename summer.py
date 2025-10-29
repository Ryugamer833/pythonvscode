import streamlit as st



student_name = st.text_input('What is your name ')



col1,col2 = st.columns(2)

with col1:

 Web_development = st.number_input('Please enter your web development score',0,100)

 Robotics = st.number_input('Please enter your Robotics score',0,100)


with col2:
 Python = st.number_input('Please enter your Python score',0,100)

 Game_development = st.number_input('Please enter your game development score ',0,100)


totalstudent_weekly_score =  Python+ Web_development + Robotics + Game_development



avg_score = totalstudent_weekly_score/4

if avg_score >= 90:
 rank = ('Platinum')


elif avg_score >= 80:
 rank = ('Gold')


elif avg_score>= 70 :
 rank = ('Silver')


elif avg_score >= 60:
 rank =('Bronze')


elif avg_score <60:
 rank =('Participant')




if st.button('Submit Scores'):
    st.write('Your weekly avg score was',avg_score,'so your rank is',rank,'Congratulations') 