import streamlit as st
player_name = st.text_input('What is your minecraft name',0)
emeralds = st.number_input('How many emeralds do you have',0)
weapons = st.number_input('How many emeralds did you spend on weapons',0)
armor = st.number_input('How many emeralds did you spend on armor',0)
food = st.number_input('How many emeralds did you spend on food',0)
blocks = st.number_input('How many emeralds did you on building blocks ',0)
total_spent = weapons + armor + food + blocks
remaining_emeralds = total_spent - emeralds
if remaining_emeralds > 20:
    st.write('Nice shopping',player_name,' You still have',remaining_emeralds,' emeralds left.Save some for some rare trades')
elif remaining_emeralds > 1 and remaining_emeralds< 20:
    st.write('Careful',player_name, 'You only have' ,remaining_emeralds,'emeralds left. Spend wisely!')
elif remaining_emeralds <= 0:
    st.write('Oh no', player_name,'! You’re out of emeralds (or overspent). Better find some villagers to trade with!"')