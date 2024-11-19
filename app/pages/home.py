import os
from config import Config
from utils import helper
from components import layout

import streamlit as st
from streamlit_ace import st_ace


# Set up the Streamlit page layout
layout.update_page_layout(layout="wide")

st.sidebar.page_link("pages/account.py", label="Account")

# Title
st.title(f'{Config.get("streamlit_ui.page_icon", "")} {Config.get("streamlit_ui.page_title")}')

# Layout setup for columns
col1, col2 = st.columns(2)

# Initialize session state for editor code and selected check
if 'editor_code' not in st.session_state:
    st.session_state.editor_code = ''
if 'selected_check' not in st.session_state:
    st.session_state.selected_check = Config.get("ai_operations.fact_check")

def generate_output(selected_check, editor_code, uploaded_file_names=None):
    """Generate the output based on the selected check."""
    with col2:
        st.subheader('AI Output')
        output = ""
        # current_check = constants.AI_CHECK_OPTIONS.get(selected_check, "unknown")

        # with st.status("AI Moderation in progress ", expanded=True) as status:
        #     st.write("Generating Subject Tags")
        #     content_tags = ai_operations.generate_upsc_tags(editor_code)
        #     extras.content_tags(tag_dict=content_tags, description="")

        #     st.write("Crafting the perfect response 📝")
        #     # Call the respective AI operation based on the selected check
        #     if current_check == constants.AI_CHECK_OPTIONS["Fact Check"]:
        #         output = ai_operations.check_factuality(editor_code)
        #     elif current_check == constants.AI_CHECK_OPTIONS["Tone Check"]:
        #         output = ai_operations.check_tone(editor_code)
        #     elif current_check == constants.AI_CHECK_OPTIONS["Accuracy Check"]:
        #         if uploaded_file_names:
        #             st.write("Processing Uploaded Files")
        #             # extractor.process_pdfs(pdf_dir="uploads", txt_dir="uploads / convert_to_text")
        #             # st.write("Running Indexing to create Vector DB")
        #             # indexer.main()
        #             output = ai_operations.query_relevancy_score(input_string=editor_code)  # Assuming a function exists to handle accuracy check on uploaded files
        #         else:
        #             output = "No files uploaded for Accuracy Check. Please upload files to proceed."
        #     else:
        #         output = "Unknown check option selected."

        #     st.code(json.dumps(output, indent=4), line_numbers=True, wrap_lines=True)

        #     status.update(
        #         label="Processing Complete!", state="complete", expanded=True
        # )


# Left column for code input
with col1:
    st.subheader('Code Input')

    subjects_folder = "app/content/subjects"
    # Dropdown for subject selection
    subjects = os.listdir(subjects_folder)
    selected_subject = st.selectbox('Select a subject', subjects, key="subject_selectbox")

    # # List files in the selected subject folder
    files_in_subject = os.listdir(os.path.join(subjects_folder, selected_subject))
    selected_file = st.selectbox('Select a file', files_in_subject, key="file_selectbox")

    # # Display the contents of the selected file
    st.caption(f'Contents of {selected_file}:')
    file_path = os.path.join(subjects_folder, selected_subject, selected_file)
    content = helper.load_code_content(file_path)
    st.session_state.editor_code = content  # Load file content into session state

    # # Display code editor
    st.session_state.editor_code = st_ace(st.session_state.editor_code, min_lines=8, wrap=True)

    # # Dropdown for check selection
    selected_check = st.selectbox('Select AI Operation', Config.get("ai_operations"))
    st.session_state.selected_check = selected_check

    # Submit button
    st.button('Submit Content', on_click=generate_output, args=(selected_check, st.session_state.editor_code), type='primary')
