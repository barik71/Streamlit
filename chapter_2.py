import streamlit as st
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

st.title("Hello, Streamlit!")

if st.button("Click me"):
    st.success("Button clicked!")

checked = st.checkbox("Check me out")

if checked:
    st.info("Checkbox is checked!")

type = st.radio("Pick one:", ["Choice A", "Choice B", "Choice C"])
st.write(f"You picked: {type}")

selected = st.selectbox("Select an item:", ["Item 1", "Item 2", "Item 3"])
st.write(f"You selected: {selected}")

st.slider("Slide me:", 0, 100, 50)

ans = st.number_input("Enter a number:", min_value=0, max_value=100, value=10)
st.write(f"You entered: {ans}")

name = st.text_input("Enter your name:")
st.write(f"Hello, {name}!")

# dob = st.date_input("Select your birth date:")
# st.write(f"Your birth date is: {dob}")

# date of birth calculator 

st.title("Date of Birth Calculator")
dob = st.date_input(
    "Select your birth date:",
    min_value=date(1900, 1, 1),
    max_value=date.today()
)
st.write(f"Your birth date is: {dob}")

today = date.today()
age = relativedelta(today, dob)
st.write(f"You are {age} years old.")