import os
import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
from datetime import datetime

from config import Config

_authenticator = None

# Get the authenticator instance
def get_authenticator():
    global _authenticator
    if _authenticator is None:
        _authenticator = setup_authenticator()
    return _authenticator

# Set up the authenticator
def setup_authenticator():

    # Load cookie key from environment
    cookie_key = os.getenv('COOKIE_KEY', 'secret_default_key')  # Use a default key if not set in the environment

    return stauth.Authenticate(
        credentials=Config.get('credentials'),
        cookie_name=Config.get('cookie.name'),
        cookie_key=cookie_key,
        cookie_expiry_days=Config.get('cookie.expiry_days'),
        auto_hash=False,
    )

# Function to handle login flow
def render_login_form():
    authenticator = get_authenticator()

    # Pre-hash passwords if needed
    # stauth.Hasher.hash_passwords(config['credentials'])

    # Initialize session state if not already initialized
    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_status'] = None

    enable_login_captcha = os.getenv('LOGIN_CAPTCHA', None)  # Use a default key if not set in the environment

    try:
        # Display the login widget and handle authentication
        authenticator.login(
            location="main",
            key="app_login_form",
            clear_on_submit=True,
            captcha=True if enable_login_captcha else False,
            callback=redirect_after_login,
        )
    except Exception as e:
        st.error(f"Error: {e}")

    if st.session_state['authentication_status'] is None:
        st.warning('Please enter your username and password', icon="⚠️")
    elif st.session_state['authentication_status'] is False:
        st.error('Username/password is incorrect', icon="🚨")

    if st.session_state.get('last_login') is None:
        st.session_state['last_login'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def render_logout_button():
    authenticator = get_authenticator()

    # Check if the user is logged in
    if st.session_state.get('authentication_status'):
        # Logout the user
        authenticator.logout(
            key="app_logout_button",
            callback=redirect_after_logout,
        )

def redirect_after_logout(*args, **kwargs):
    # Reset some sessions custom session variables
    st.session_state['last_login'] = None
    # Finally redirect to the main page where user will be asked to login
    switch_page('main')

def redirect_after_login(*args, **kwargs):
    # Finally redirect to the main page where user will be asked to login
    switch_page('home')
