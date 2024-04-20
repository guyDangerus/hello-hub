import streamlit as st

n1 = st.number_input("Enter the first number --", step = 0.0001, value = 0.0000, format = "%5.4f")
n2 = st.number_input("Enter the second number --", step = 0.0001, value = 0.0000, format = "%5.4f")
n3 = st.number_input("Enter the third number --", step = 0.0001, value = 0.0000, format = "%5.4f")

greatest = max(n1, n2, n3)
greatest = round(greatest, 4)

st.write("the largest number is ", greatest)
if st.button("Click me!"):
    st.balloons()
