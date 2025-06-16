import streamlit as st
from utils.supabase import get_tracking_data

def display_tracking_info():
    st.title("Device Tracking Information")
    
    tracking_data = get_tracking_data()
    
    if tracking_data:
        for device in tracking_data:
            st.subheader(f"Device ID: {device['id']}")
            st.write(f"IMEI: {device['imei']}")
            st.write(f"Location: {device['location']}")
            st.write(f"Status: {device['status']}")
            st.write("---")
    else:
        st.write("No tracking information available.")

if __name__ == "__main__":
    display_tracking_info()