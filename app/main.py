from config import Config
from components import auth
import streamlit as st

if __name__ == "__main__":
    # Load configuration
    Config.load_config("app/config.yaml")

    # Set up the Streamlit page configuration
    st.set_page_config(
        page_title=Config.get('streamlit_ui.page_title'),
        page_icon=Config.get('streamlit_ui.page_icon'),
        layout=Config.get('streamlit_ui.layout'),
        initial_sidebar_state=Config.get('streamlit_ui.initial_sidebar_state')
    )

    # Render the login form
    auth.render_login_form()
