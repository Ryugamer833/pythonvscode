import streamlit as st

st.header('Toy Store')
bill = 0


monstertruck1,monstertruck2,monstertruck3 = st.columns(3)

 

with monstertruck1:
    st.image('https://m.media-amazon.com/images/I/81I0RYKEI0L._AC_UL480_FMwebp_QL65_.jpg')

with monstertruck2:
    st.write('')
    st.write('')
    st.subheader('Monster Truck:$20')

with monstertruck3:
 monstertruck =  st.number_input('How many monstertrucks do you want',0,100)

st.divider()

robotdog1,robotdog2,robotdog3 = st.columns(3)

with robotdog1:
   st.image('https://m.media-amazon.com/images/I/51lHONBtW3L._AC_UL480_FMwebp_QL65_.jpg')


with robotdog2:
   st.write('')
   st.write('')
   st.subheader('Robot Dog:$50')


with robotdog3:
 robotdog =  st.number_input('How many robot dogs do you want',0,100)



st.divider()

bowarrow1,bowarrow2,bowarrow3 = st.columns(3)

with bowarrow1:
   st.image('https://m.media-amazon.com/images/I/81LXbld-uSL._AC_UL480_FMwebp_QL65_.jpg')


with bowarrow2:
   st.write('')
   st.write('')
   st.subheader('JOYIN kids bow and arrow:$30')


with bowarrow3:
 bowarrow =   st.number_input('How many bows and arrows do you want',0,100)

st.divider()



soccerball1,soccerball2,soccerball3= st.columns(3)

with soccerball1:
   st.image('https://m.media-amazon.com/images/I/41gbtCymmOL._AC_SR250,250_QL65_.jpg')


with soccerball2:
   st.write('')
   st.write('')
   st.subheader('Playbolt Soccer Ball:$20')


with soccerball3:
 soccerball =   st.number_input('How many of these soccer balls do you want',0,100)

st.divider()



glowingfootball1,glowingfootball2,glowingfootball3= st.columns(3)

with glowingfootball1:
   st.image('https://m.media-amazon.com/images/I/51Vr3PxMttL._AC_SR250,250_QL65_.jpg')


with glowingfootball2:
   st.write('')
   st.write('')
   st.subheader('Startrail Glow in the Dark Football:$20')


with glowingfootball3:
 glowingfootball =  st.number_input('How many footballs do you want',0,100)

st.divider()


monstertruckprice = monstertruck * 20

glowingfootballprice = glowingfootball * 20
soccerballprice = soccerball * 20
bowandarrowprice = bowarrow * 30
robot_dogprice = robotdog * 50


bill = glowingfootballprice + soccerballprice + bowandarrowprice + robot_dogprice + monstertruckprice


if st.button('Done'):
  st.write('Hello your final bill is',bill)


