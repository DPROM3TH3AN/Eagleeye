import streamlit as st
from utils.supabase import get_numbers_data

def display_numbers():
    st.title("Number Analysis")
    
    # Fetch number-related data from Supabase
    numbers_data = get_numbers_data()
    
    if numbers_data:
        st.write("### Number Data")
        for number in numbers_data:
            st.write(f"- {number}")
    else:
        st.write("No data available.")

if __name__ == "__main__":
    display_numbers()