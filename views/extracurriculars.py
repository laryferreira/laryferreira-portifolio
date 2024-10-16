import streamlit as st
from streamlit_option_menu import option_menu

# Color palette
colors = {
    'lightest_blue': '#f7d1cd',
    'light_blue': '#e8c2ca',
    'medium_blue': '#d1b3c4',
    'dark_blue': '#b392ac', 
    'darkest_blue': '#615483',
    'white': '#f4ece8',
}
st.markdown(f"""
<style>
    .stApp {{
        background: linear-gradient(180deg, #08090C 0%, #212531 50%, #313749 100%) !important;
    }}
</style>
""", unsafe_allow_html=True)


# HTML and CSS for the centered baby blue interactive timeline with polaroid-style photos
timeline_html = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Covered+By+Your+Grace&family=Homemade+Apple&display=swap');
:root {{
    --lightest-blue: {colors['lightest_blue']};
    --light-blue: {colors['light_blue']};
    --medium-blue: {colors['medium_blue']};
    --dark-blue: {colors['dark_blue']};
    --darkest-blue: {colors['darkest_blue']};
    --white: {colors['white']};
}}
.timeline-container {{
    display: flex;
    justify-content: center;
    width: 100%;
    padding: 10px;
}}
.timeline {{
    position: relative;
    max-width: 1200px;
    width: 100%;
}}
.timeline::after {{
    content: '';
    position: absolute;
    width: 6px;
    background-color: var(--dark-blue);
    top: 0;
    bottom: 0;
    left: 50%;
    margin-left: -3px;
}}
.timeline-item {{
    padding: 10px 40px;
    position: relative;
    background-color: inherit;
    width: 50%;
    box-sizing: border-box;
}}
.timeline-item::after {{
    content: '';
    position: absolute;
    width: 25px;
    height: 25px;
    right: -17px;
    background-color: var(--darkest-blue);
    border: 4px solid var(--darkest-blue);
    top: 15px;
    border-radius: 50%;
    z-index: 1;
}}
.left {{
    left: 0;
}}
.right {{
    left: 50%;
}}
.right::after {{
    left: -16px;
}}
.timeline-content {{
    padding: 20px 30px;
    position: relative;
}}
.timeline-year {{
    font-weight: bold;
    font-family: 'Montserrat', sans-serif;
    font-size: 1.8em;
    color: var(--dark-blue);
    margin-bottom: 10px;
    transition: all 0.3s ease;
}}
.timeline-text {{
    color: var(--medium-blue);
    margin-bottom: 10px;
    font-family: 'Montserrat', sans-serif;
}}
.timeline-photo {{
    background-color: var(--white);
    border: 1px solid var(--light-blue);
    padding: 2px 3px 10px 3px;
    transform: rotate(-2deg);
    width: 200px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    margin-bottom: 15px;
    transition: all 0.3s ease;
}}
.timeline-photo img, .timeline-photo iframe {{
    width: 100%;
    height: 150px;
    object-fit: cover;
    display: block;
}}
.timeline-photo p {{
    text-align: center;
    margin-top: 10px;
    font-size: 1.3em;
    font-family: "Covered By Your Grace", cursive;
    color: var(--darkest-blue);
}}
.timeline-item:hover .timeline-year {{
    font-size: 1.5em;
    color: var(--darkest-blue);
}}

.timeline-item:hover .timeline-photo {{
    transform: rotate(0deg) scale(1.05);
    box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
}}
.timeline-text-list {{
    list-style-type: none;
    padding-left: 0;
    margin-bottom: 15px;
}}

.timeline-text-list li {{
    position: relative;
    padding-left: 20px;
    margin-bottom: 5px;
    font-size: 0.9em;
    color: var(--white);
    font-family: 'Montserrat', sans-serif;
}}

.timeline-text-list li a:hover,
.timeline-text-list li a:active {{
    color: var(--lightest-blue);
    border-bottom-color: var(--lightest-blue);
}}


.timeline-text-list li a {{
    color: var(--light-blue);
    text-decoration: none;
    transition: all 0.3s ease;
    border-bottom: 1px solid transparent;
}}

.timeline-text-list li a:hover,
.timeline-text-list li a:active {{
    color: var(--lightest-blue);
    border-bottom-color: var(--lightest-blue);
}}

@media (hover: hover) {{
    .timeline-text-list li a:hover {{
        color: var(--lightest-blue);
        border-bottom-color: var(--lightest-blue);
    }}
     .timeline-text-list li:hover {{
        transform: scale(1.03); 
    }}

}}


.timeline-text-list li::before {{
    content: '•';
    position: absolute;
    left: 0;
    color: var(--dark-blue);
}}


@media screen and (max-width: 600px) {{
    .timeline::after {{
        left: 31px;
    }}
    .timeline-item {{
        width: 100%;
        padding-left: 70px;
        padding-right: 25px;
    }}
    .left::after, .right::after {{
        left: 15px;
    }}
    .right {{
        left: 0%;
    }}
}}
</style>

<div class="timeline-container">
    <div class="timeline">
        <div class="timeline-item left">
            <div class="timeline-content">
                <div class="timeline-year">2024</div>
                <div class="timeline-text">Second Year of University (Current) </div>
                <ul class="timeline-text-list">
                    <li>Software Developer Intern at <a href="https://www.btgpactual.com/">BTG Pactual</a>, developing tools and a chatbot for the collections team</li>
                    <li>Co-organized and developed the Women's Programming Marathon website, a major event with 1000+ entries.</li>
                    <li>World Bank delegate at the 2024 Youth Summit and Grace Hopper fellow, receiving a 1-year scholarship from AnitaB.org.</li>
                    <li>Organized and spoke at the “RoME Summer School” 2024, uniting students and teachers from Argentina and Brazil.</li>
                    <li>Returned to my high school to share my journey in computer engineering, an inspiring and fulfilling experience.</li>
                </ul>
                <div class="timeline-photo">
                    <iframe src="https://drive.google.com/file/d/1DNO-ekdl4SZcRI8Gnq5-CA8YrGD3qbhT/preview" width="640" height="480" allow="autoplay"></iframe>
                        <p>MFP at Unicamp</p>
                </div>
            </div>
        </div>
        <div class="timeline-item right">
            <div class="timeline-content">
                <div class="timeline-year">2023</div>
                <div class="timeline-text">First Year of University</div>
                <ul class="timeline-text-list">
                    <li>In my first year at university, I explored a bit of everything!</li>
                    <li>As a <a href="https://www.instagram.com/p/CzJ4145OJXw/?img_index=1">Meninas.Comp</a> scholar, I conducted the first UnB women's programming competition with sponsorship and taught python at public schools in Federal District</li>
                    <li>As an undergraduate researcher at <a href="https://les.unb.br/">LES</a>, I assisted research on <a href="https://www.docdroid.net/PPXqE4g/bsn-report-pdf">Body Sensor Network (BSN)</a> applied in the field of medicine.</li>
                    <li>As a <a href="https://www.huawei.com/minisite/seeds-for-the-future/index.html">Huawei Seeds for the Future</a> alumni, I was one of 25 brazilian women selected to pitch in Latin American phase</li>
                    <li>Led teams through competitions and hackathons<li>
                </ul>
                <div class="timeline-photo">
                     <iframe src="https://drive.google.com/file/d/1oEXz8tP2cusjukUTTr2pGbO7D-lIfAIz/preview"  width="400" height="150" allow="autoplay"></iframe>
                    <p>Women programming competitions!</p>
                </div>
            </div>
        </div>
        <div class="timeline-item left">
            <div class="timeline-content">
                <div class="timeline-year">2022</div>
                <div class="timeline-text">Started Bachelor's degree in Computer Engineering</div>
                <ul class="timeline-text-list">
                    <li>I finished high school and entered <a href="https://www.topuniversities.com/universities/universidade-de-brasilia">UnB</a> through the <a href="https://www.cebraspe.org.br/pas-unb/">serial assessment program</a>, studying for 3 years straight.</li>
                    <li>I am very glad to be the first in my family to enter a <a href="https://en.wikipedia.org/wiki/Public_university">public university</a>!</li>
                </ul>
                <div class="timeline-photo">
                     <iframe src="https://drive.google.com/file/d/1bVYwQzS8ESrrgCjUmL_3y1xqSGWAzkAY/preview" width="400" height="150" allow="autoplay"></iframe>
                    <p>Class of 2027!</p>
                </div>
            </div>
        </div>
        <div class="timeline-item right">
            <div class="timeline-content">
                <div class="timeline-year">2021</div>
                <div class="timeline-text">High School</div>
                 <ul class="timeline-text-list">
                    <li>Selected for virtual high school research program (<a href="https://drive.google.com/file/d/1m_rq3oWBywyWD3jcQ_XJW7qkJVhBTNMr/preview" >+Science</a>)</li>
                    <li>Presented the final project at the DF's main science fair (<a href="https://febratecdf.com.br/">FEBRATEC - Brasilia Science and Technology Fair</a>, hosted by the University of Brasilia</a>)</li>
                    <li>My research group won <a href="https://drive.google.com/file/d/1owrQBSIjvoKrhdvjUybk0IMbpOJRKN7F/preview">2nd place for best engineering project</a>, which sparked my interest in the field!</li>
                </ul>
                <div class="timeline-photo">
                   <iframe src="https://drive.google.com/file/d/1PwxqnnXrlF3IEl2qSMnEe4CRf6-EQ7uE/preview" width="640" height="480" allow="autoplay"></iframe>
                    <p>First Research!</p>
                </div>
            </div>
        </div>
    </div>
</div>
"""

colors = {
    'lightest_blue': '#f7d1cd',
    'light_blue': '#e8c2ca',
    'medium_blue': '#d1b3c4',
    'dark_blue': '#b392ac', 
    'darkest_blue': '#615483',
    'white': '#f4ece8',
}
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

    .title {
        font-family: 'Montserrat', sans-serif;
        color: {colors['lightest_blue']}; /* Change title color */
        font-size: 2.2em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add custom CSS for styling (if not already present)
st.markdown(f"""
<style>
    .hover-effect {{
        transition: color 0.3s ease, transform 0.3s ease; /* Added transform transition */
        color: {colors['lightest_blue']}; /* Default color */
    }}
    .hover-effect:hover {{
        color: {colors['dark_blue']}; /* Color on hover */
        transform: translateY(-5px); /* Move up by 5 pixels on hover */
    }}
    ...
</style>
""", unsafe_allow_html=True)

# Create the timeline with hover effect on the title
st.markdown("<h1 class='title hover-effect'>Career Highlights</h1><h2 class='subtitle'></h2>", unsafe_allow_html=True)

def show():
    # Renderizar a timeline
    st.components.v1.html(timeline_html, height=1000, scrolling=True)

# Chamar a função show
show()
