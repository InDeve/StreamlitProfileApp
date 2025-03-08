import streamlit as st
import re

import requests

# Inform code when user hits submit
WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTY5MDYzNjA0M2M1MjZkNTUzNzUxMzUi_pc"

def is_valid_email(email):
    # regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-0-.]+$"
    return re.match(email_pattern, email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Enter Your Message")
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if not WEBHOOK_URL:
                st.error("Service error.", icon="📩")
                st.stop()
            
            if not name:
                st.error("Please enter your name.")
                st.stop()
            
            if not email:
                st.error("Please enter your email")
                st.stop()
            
            if not is_valid_email(email):
                st.error("Please provide a valid email address.")
                st.stop()
            
            if not message:
                st.error("Please enter a message.")
                st.stop()
            
            data = {"email": email, "name": name, "message": message}
            response = requests.post(WEBHOOK_URL, json=data)

            if response.status_code == 200:
                st.success("Your message has been sent!", icon="📤")
            else:
                st.error("An error occured while sending your message.")

