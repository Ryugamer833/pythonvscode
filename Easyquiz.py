import streamlit as st

st.title('First Aid quiz')

score = 0


st.info('Question 1 - Nosebleed')


q1 = st.selectbox('Your friend’s nose suddenly starts bleeding 😮What should you do first?',['Choose an answer','tilt their head back and pinch the nose','Tilt their head forward and pinch the nose','Make them lie flat on the ground'])

if q1 == 'tilt their head back and pinch the nose':
    st.write('That is the correct answer')
    score += 1


st.info('Question 2 - Choking')

q2 = st.selectbox('Someone is eating and suddenly starts coughing hard, can’t speak, and looks panicked 😨',['Choose an answer','Give them water to drink','Perform the Heimlich maneuver','Tell them to lie down and rest'])


if q2 == 'Perform the Heimlich maneuver':
    st.write('That is the correct answer')
    score += 1



st.info('Question 3 - Fainting')

q3 = st.selectbox('You see your friend faint while standing in the sun ☀️,What should you do first',['Choose an answer','Lay them on their back and lift their legs','Give them food immediately','Shake them to wake them up'])

if q3 == 'Lay them on their back and lift their legs':
    st.write('That is the correct answer')
    score += 1


if st.button('Check my score'):
    st.write('Your score is',score)    
