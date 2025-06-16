import streamlit as st
from components.sidebar import sidebar
from pages import chat, tracking, numbers

# Set up the main layout of the app
st.set_page_config(page_title="Eagle Eye Dashboard", layout="wide")

# Render the sidebar for navigation
sidebar()

# Main content area
st.title("Eagle Eye Tracking System")

# Create a navigation menu
page = st.sidebar.selectbox("Select a page:", ["Chat", "Tracking", "Numbers"])

# Render the selected page
if page == "Chat":
    chat.show_chat()
elif page == "Tracking":
    tracking.show_tracking()
elif page == "Numbers":
    numbers.show_numbers()