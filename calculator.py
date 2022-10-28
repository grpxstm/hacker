import streamlit as st
number = st.number_input('insert a number')
numberr = st.number_input('insert a number')
st.write('the current is,number')
st.write('the current is,numberr')
sum = number+numberr
st.write(sum)
