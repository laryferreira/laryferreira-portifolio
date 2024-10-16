import streamlit as st

# Define colors
colors = {
    'lightest_blue': '#f7d1cd',
    'light_blue': '#e8c2ca',
    'medium_blue': '#d1b3c4',
    'dark_blue': '#b392ac', 
    'darkest_blue': '#615483',
    'white': '#f4ece8',
}

# Add custom CSS for styling
st.markdown(f"""
<style>
    .stApp {{
        background: linear-gradient(180deg, #08090C 0%, #212531 50%, #313749 100%) !important;
    }}
    .container {{
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin: 20px 0;
    }}
    .column {{
        flex: 1;
        margin: 10px;
    }}
    .hover-effect {{
        transition: color 0.3s ease, transform 0.3s ease; 
        color: {colors['lightest_blue']};
    }}
    .hover-effect:hover {{
        color: {colors['darkest_blue']}; /* Color on hover */
        transform: translateY(-7px); /* Move up by 5 pixels on hover */
    }}
    h1 {{
        font-family: 'Montserrat', sans-serif;
        color: {colors['lightest_blue']}; /* Change title color */
        font-size: 2.5em;
    }}
    h2 {{
        font-family: 'Montserrat', sans-serif;
        color: {colors['dark_blue']}; /* Change header color */
        font-size: 1.5em;
    }}
    p {{
        font-family: 'Montserrat', sans-serif;
        color: {colors['white']}; /* Change paragraph color */
        font-size: 1em;
    }}
    .footer {{
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        color: grey;
        padding: 10px;
    }}
</style>
""", unsafe_allow_html=True)

class AboutMe:
    def __init__(self, title, about, img):
        self.title = title
        self.about = about
        self.img = img

    def display(self):
        col1, col2, col3 = st.columns([1.5, 0.1, 1.2])
        with col1:
            st.markdown(f"<h2 class='hover-effect' style='font-size: 36px;'>{self.title}</h2>", unsafe_allow_html=True)
            st.markdown(f"<div style='text-align: justify;'>{self.about}</div>", unsafe_allow_html=True)

            st.markdown("""
                <div style="margin-top: 20px;">
                    <p><a href="https://www.linkedin.com/in/laryssaoliferreira/" style="text-decoration: none;">🔗 LinkedIn</a></p>
                    <p><a href="mailto:laryssa.ferreira@aluno.unb.br" style="text-decoration: none;">📨 Email</a></p>
                    <p><a href="http://lattes.cnpq.br/3221759794696198" style="text-decoration: none;">📝 Lattes </a></p>
                    <p><a href="https://github.com/laryferreira" style="text-decoration: none;">💻 Github</a></p>
                </div>
            """, unsafe_allow_html=True)

        with col3:           
            st.image(self.img, use_column_width=True)

# Description
description = """
Curious girl who grew up and works in tech, creating web solutions, promoting female participation in IT and sharing knowledge through multiple projects.
<br>Currently, a Software Developer intern at the largest investment bank in Latin America (BTG), researcher and Computer Engineer on the making at University of Brasília, Brazil.
"""

# Display content
about = AboutMe("Laryssa Ferreira", description, "img/profile.png")  # Update the image path as needed
about.display()

st.divider()





# Technical Skills Section
st.subheader("Technical Skills")
st.write("""
- **Programming languages:** Python, Typescript, C++
- **Libraries and frameworks:** Pandas, Pytorch, Tensorflow, StreamLit, NodeJs, NestJs, VueJs
- **Service Deployment and Cloud:** AWS(EC2, SQS, SNS, S3), Azure, Kubernetes, Docker
- **Version control:** Git
- **Agile methodologies:** Scrum
- **Formatting tools:** LaTeX
""")
st.divider()

# Footer
st.markdown(
    """
    <div class="footer">
        <p>Developed by Laryssa Ferreira &copy; 2024</p>
    </div>
    """,
    unsafe_allow_html=True
)
