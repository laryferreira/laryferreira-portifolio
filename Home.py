import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Laryssa Ferreira",page_icon="star", layout="centered", initial_sidebar_state="auto")
# Custom CSS to change background color
background_color = """
<style>
    .stApp {
        background: linear-gradient(135deg, #ffcdb2 0%, #e5989b 100%);
    }
</style>
"""

# --- PAGE SETUP --- #

about_page = st.Page(
    page = "views/about.py",
    title = "About Me",
    default = True
)

timeline_page = st.Page(
    page = "views/extracurriculars.py",
    title = "Highlights",
)

page = st.navigation(pages=[about_page, timeline_page])

page.run()