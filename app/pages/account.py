import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from components import auth

# Display user details if they exist in session state
if st.session_state.get('authentication_status'):
    # Safely retrieve user details from session state
    user_details = {
        'username': st.session_state.get('username', 'N/A'),
        'email': st.session_state.get('email', 'N/A'),
        'full_name': st.session_state.get('name', 'N/A'),
        # Placeholder for last login if available
        'last_login': st.session_state.get('last_login', 'N/A')
    }

    st.title("My Account")

    # Additional buttons or features
    if st.button("Back to Main", key='go_back_main_app'):
        switch_page('home')

    # Display user details in text inputs (disabled for read-only view)
    st.text_input("Username", value=user_details['username'], disabled=True, key='username_input')
    st.text_input("Email", value=user_details['email'], disabled=True, key='email_input')
    st.text_input("Full Name", value=user_details['full_name'], disabled=True, key='fullname_input')
    st.text_input("Last Login", value=user_details['last_login'], disabled=True, key='last_login_input')

    col1, col2, _, _, _, _ = st.columns(6, gap="small")
    # Flag to track if the button was clicked
    show_warning = False
    with col1:
        # Additional buttons or features
        if st.button("Edit Profile", key='edit_profile_button'):
            show_warning = True
    with col2:
        auth.render_logout_button()

    if show_warning:
        st.warning("Profile editing feature is under construction! 🚧")

else:
    # Button to navigate back to the main page if not authenticated
    if st.button("Back to Main Page", key='back_to_main_button'):
        # Redirect to the main page (use query parameters to control navigation)
        switch_page('home')

    st.warning("No user details found. Please log in to view your account.")
