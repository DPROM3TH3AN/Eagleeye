import streamlit as st
from datetime import datetime
import sys
import os

# Add parent directory to path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.supabase import get_supabase_client

def render_sidebar():
    """Renders the sidebar with navigation and user controls"""
    
    with st.sidebar:
        st.title("Eagle Eye")
        
        # User Authentication Section
        if 'user' not in st.session_state:
            st.session_state.user = None
            
        if st.session_state.user is None:
            with st.expander("Login", expanded=True):
                email = st.text_input("Email")
                password = st.text_input("Password", type="password")
                if st.button("Sign In"):
                    try:
                        supabase = get_supabase_client()
                        response = supabase.auth.sign_in_with_password({
                            "email": email,
                            "password": password
                        })
                        st.session_state.user = response.user
                        st.success("Successfully logged in!")
                        st.experimental_rerun()
                    except Exception as e:
                        st.error(f"Login failed: {str(e)}")
        else:
            st.write(f"Welcome, {st.session_state.user.email}")
            if st.button("Logout"):
                st.session_state.user = None
                st.experimental_rerun()
        
        # Navigation Menu
        st.sidebar.header("Navigation")
        pages = {
            "Dashboard": "🏠",
             "Chat": "💬",
            "Tracking": "📍",
            "Numbers": "📊"
        }
        
        selected_page = st.sidebar.radio(
            "Go to",
            pages.keys(),
            format_func=lambda x: f"{pages[x]} {x}"
        )
        
        # System Status
        st.sidebar.header("System Status")
        status_container = st.sidebar.container()
        with status_container:
            st.write("Last Update:", datetime.now().strftime("%H:%M:%S"))
            st.progress(0.8, "System Health")
            
            # Quick Stats
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Active Users", "42", "+5")
            with col2:
                st.metric("Messages", "128", "+12")
        
        # Settings
        with st.sidebar.expander("Settings ⚙️"):
            st.checkbox("Dark Mode")
            st.checkbox("Notifications")
            st.select_slider(
                "Update Frequency",
                options=["1m", "5m", "15m", "30m", "1h"],
                value="5m"
            )
        
        # Footer
        st.sidebar.markdown("---")
        st.sidebar.caption("Eagle Eye v1.0.0")
        st.sidebar.caption("© 2025 Eagle Eye Systems")

if __name__ == "__main__":
    render_sidebar()
