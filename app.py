import streamlit as st
import joblib
model = joblib.load('spam-ham')
st.title('SPAM-HAMCLASSIFIER')
IP = st.text_input('enter your message')
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
