# frontend matrai basxa
import streamlit as st
from models import gemini

st.header('Gemini LLM Application')
st.subheader('Prompt Engineering')


data = st.text_area('Prompt',placeholder='Ask Gemini')

if st.button('Send Prompt'):
    if data.strip() == '':
        # Sucess, Error, Warning
        st.warning('Enter content')
    else:
        with st.spinner('Thinking🤔'):
            try:
                answer = gemini(data)
                st.toast('Content Generated')
                st.write(answer)
            except Exception as e:
                st.toast(e)