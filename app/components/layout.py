from config import Config
import streamlit as st


def update_page_layout(layout):
    # Set up the Streamlit page configuration
    st.set_page_config(
        page_title=Config.get('streamlit_ui.page_title'),
        page_icon=Config.get('streamlit_ui.page_icon'),
        layout=layout,
        initial_sidebar_state=Config.get('streamlit_ui.initial_sidebar_state')
    )

def reset_page_layout():
    # Set up the Streamlit page configuration
    st.set_page_config(
        page_title=Config.get('streamlit_ui.page_title'),
        page_icon=Config.get('streamlit_ui.page_icon'),
        layout=Config.get('streamlit_ui.layout'),
        initial_sidebar_state=Config.get('streamlit_ui.initial_sidebar_state')
    )
