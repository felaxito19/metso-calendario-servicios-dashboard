# mod_auth.py
import streamlit as st
from supabase import create_client, Client

def init_supabase():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

def login_user(email: str, password: str):
    supabase = init_supabase()
    try:
        user = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })
        return user
    except Exception as e:
        st.error(f"Error: {e}")
        return None

def signup_user(email: str, password: str):
    supabase = init_supabase()
    try:
        user = supabase.auth.sign_up({
            "email": email,
            "password": password
        })
        return user
    except Exception as e:
        st.error(f"Error: {e}")
        return None

def require_login():
    """Bloquea acceso si el usuario no está logueado."""
    if "user" not in st.session_state or st.session_state.user is None:
        st.error("Inicia sesión para continuar")
        st.stop()

