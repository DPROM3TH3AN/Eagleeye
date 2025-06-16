import streamlit as st
from datetime import datetime
import sys
import os

# Add parent directory to path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.supabase import get_supabase_client
from utils.api import get_api_client

def init_chat_page():
    st.title("Chat System")
    
    # Initialize Supabase client
    supabase = get_supabase_client()
    
    # Chat interface
    st.sidebar.header("Chat Controls")
    selected_contact = st.sidebar.selectbox(
        "Select Contact",
        ["Contact 1", "Contact 2", "Contact 3"]  # Replace with actual contacts from database
    )

    # Chat history container
    chat_container = st.container()
    
    with chat_container:
        # Fetch chat history from Supabase
        try:
            messages = supabase.table('messages')\
                .select('*')\
                .eq('contact', selected_contact)\
                .order('timestamp')\
                .execute()
            
            # Display messages
            for msg in messages.data:
                with st.chat_message(msg['sender']):
                    st.write(f"{msg['content']}")
                    st.caption(f"Sent: {msg['timestamp']}")
        
        except Exception as e:
            st.error(f"Error loading chat history: {str(e)}")

    # Message input
    with st.form(key='message_form'):
        message = st.text_area("Type your message:", height=100)
        send_button = st.form_submit_button("Send")
        
        if send_button and message:
            try:
                # Save message to Supabase
                new_message = {
                    'content': message,
                    'sender': 'user',
                    'contact': selected_contact,
                    'timestamp': datetime.now().isoformat()
                }
                
                supabase.table('messages').insert(new_message).execute()
                st.success("Message sent successfully!")
                st.experimental_rerun()
                
            except Exception as e:
                st.error(f"Error sending message: {str(e)}")

    # Additional features
    with st.expander("Chat Settings"):
        st.checkbox("Enable notifications")
        st.selectbox("Chat theme", ["Light", "Dark", "System"])
        if st.button("Clear Chat History"):
            try:
                supabase.table('messages')\
                    .delete()\
                    .eq('contact', selected_contact)\
                    .execute()
                st.success("Chat history cleared!")
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Error clearing chat history: {str(e)}")

if __name__ == "__main__":
    init_chat_page()