from supabase import create_client, Client
import os
from dotenv import load_dotenv
from typing import Optional

# Load environment variables
load_dotenv()

class SupabaseClient:
    def __init__(self):
        self.url = os.getenv("SUPABASE_URL")
        self.key = os.getenv("SUPABASE_KEY")
        
        if not self.url or not self.key:
            raise ValueError(
                "Missing Supabase credentials. "
                "Please set SUPABASE_URL and SUPABASE_KEY environment variables."
            )
        
        self.client = create_client(self.url, self.key)

    def get_client(self) -> Client:
        """Returns the Supabase client instance"""
        return self.client

    def get_user(self):
        """Get current authenticated user"""
        return self.client.auth.get_user()

    def sign_in_with_email(self, email: str, password: str):
        """Sign in user with email and password"""
        return self.client.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

    def sign_out(self):
        """Sign out current user"""
        return self.client.auth.sign_out()

    def get_session(self):
        """Get current session"""
        return self.client.auth.get_session()

# Singleton instance
_supabase_client: Optional[SupabaseClient] = None

def get_supabase_client() -> SupabaseClient:
    """Get or create Supabase client instance"""
    global _supabase_client
    if _supabase_client is None:
        _supabase_client = SupabaseClient()
    return _supabase_client.get_client()