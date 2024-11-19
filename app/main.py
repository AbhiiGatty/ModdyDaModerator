from config import Config
from components import auth
from components import layout
import streamlit as st

if __name__ == "__main__":
    # Load configuration
    Config.load_config("app/config.yaml")

    # Reset page layout to default settings
    layout.reset_page_layout()

    # Render the login form
    auth.render_login_form()
