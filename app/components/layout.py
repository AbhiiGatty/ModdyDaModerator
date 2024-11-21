from config import Config
import streamlit as st


def update_page_layout(layout):
    """
    Updates the Streamlit page layout configuration.

    Args:
        layout (str): Layout type. Must be one of "centered" or "wide"

    Raises:
        ValueError: If an invalid layout type is provided.
    """
    # Allowed layout values
    allowed_layouts = {"centered", "wide"}

    # Validate the layout input
    if layout not in allowed_layouts:
        raise ValueError(f"Invalid layout '{layout}'. Allowed values are: {', '.join(allowed_layouts)}")

    # Set up the Streamlit page configuration
    st.set_page_config(
        page_title=Config.get('streamlit_ui.page_title'),
        page_icon=Config.get('streamlit_ui.page_icon'),
        layout=layout,
        initial_sidebar_state=Config.get('streamlit_ui.initial_sidebar_state')
    )

def reset_page_layout():
    """
    Resets the Streamlit page layout to the default configuration
    defined in the Config object.
    """
    # Set up the Streamlit page configuration with default values
    st.set_page_config(
        page_title=Config.get('streamlit_ui.page_title'),  # Retrieve and set the default page title
        page_icon=Config.get('streamlit_ui.page_icon'),    # Retrieve and set the default page icon
        layout=Config.get('streamlit_ui.layout'),          # Retrieve and set the default layout type
        initial_sidebar_state=Config.get('streamlit_ui.initial_sidebar_state')  # Retrieve and set the default sidebar state
    )
