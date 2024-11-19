import os
import streamlit as st
from config import Config
from components import auth
from components import layout


if __name__ == "__main__":
    # Load configuration
    Config.load_config("app/config.yaml")

    # Reset page layout to default settings
    layout.reset_page_layout()

    # Initialize session state for logout functionality
    st.session_state['logout'] = None

    if os.getenv("LOGIN_ENABLED", None):
        # Render the login form
        auth.render_login_form()
    else:
        auth.redirect_after_login()
