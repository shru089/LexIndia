from supabase import create_client, Client
from config import settings

if settings.SUPABASE_URL and settings.SUPABASE_ANON_KEY:
    supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_ANON_KEY)
else:
    supabase = None
    print("⚠️ Warning: Supabase credentials not found in config.")
