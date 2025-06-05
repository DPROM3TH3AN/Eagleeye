# backend/utils/supabase_client.py
from supabase import create_client, Client
import os

# Replace with your actual Supabase URL and API key
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def insert_tracking_data(data: dict):
    response = supabase.table("tracking").insert([data]).execute()
    return response
