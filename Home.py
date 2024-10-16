import streamlit as st

st.set_page_config(page_title="Laryssa Ferreira", page_icon="star", layout="centered", initial_sidebar_state="auto")

# Custom CSS to change background color and add hover effects
background_color = """
<style>
    .stApp {
        background: linear-gradient(135deg, #ffcdb2 0%, #e5989b 100%);
    }
    .sidebar-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .sidebar-button {
        padding: 10px;
        cursor: pointer; /* Default cursor */
        background-color: #f0f0f0; /* Light gray background */
        border-radius: 5px; /* Rounded corners */
        font-size: 18px; /* Larger font size */
        font-weight: bold; /* Bold text */
        color: #333; /* Dark text color */
        transition: background-color 0.3s ease, transform 0.3s ease; /* Smooth transition */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }
    .sidebar-button:hover {
        background-color: #ffb3c1; /* Light pink on hover */
        transform: translateY(-2px); /* Move up slightly on hover */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* Stronger shadow on hover */
    }
</style>
"""
st.markdown(background_color, unsafe_allow_html=True)

# --- PAGE SETUP --- #

# Sidebar for navigation
st.sidebar.markdown("<div class='sidebar-title'>Navigation</div>", unsafe_allow_html=True)

# Initialize a session state variable to track the current page
if 'current_page' not in st.session_state:
    st.session_state.current_page = "About Me"  # Default page

# Create buttons for navigation
if st.sidebar.button("About Me", key="about_button"):
    st.session_state.current_page = "About Me"

if st.sidebar.button("Highlights", key="highlights_button"):
    st.session_state.current_page = "Highlights"

# Load the appropriate page based on the selected item
if st.session_state.current_page == "About Me":
    with open("views/about.py") as f:
        exec(f.read())
elif st.session_state.current_page == "Highlights":
    with open("views/extracurriculars.py") as f:
        exec(f.read())
