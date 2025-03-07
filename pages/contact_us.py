import streamlit as st
import send_email

st.set_page_config(layout='wide')

st.header("Contact us")

with st.form(key='contact form'):
    user_email = st.text_input(key='user email address', label='Enter your email')
    user_message = st.text_area(key='user message', label='Enter your message')
    submit_btn = st.form_submit_button(label='Submit')
    if button:

        message = f"""
        Subject: New email from {user_email}
        
        From: {user_email}
        {user_message}
        """

        send_email(message)

        st.info('Message sent succcessfully')