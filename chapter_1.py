import streamlit as st

st.title("Hello, Streamlit!")
st.subheader("This is a subheader")
st.text("This is a simple text element.")
st.write("This is a write element that can display various data types.")

selected = st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])

st.write(f"You selected: {selected}. excellent choice!")
st.success("This is a success message!")