import streamlit as st

from forms.contact import contact_form
from st_social_media_links import SocialMediaIcons

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

# ''' SOCIAL MEDIA LINKS '''
links = [" https://www.linkedin.com/in/calvin-yang-7baa9427b/",]
icons = SocialMediaIcons(links)

# ''' PROFILE TITLE AND DESCRIPTION '''
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col2:
    st.image("./assets/profile_placeholder.png", width=230)
with col1:
    st.title("Calvin Y", anchor=False)
    info = st.container()
    info.write("ckyang02@gmail.com")
    with info:
        icons.render(sidebar=False, justify_content="left")
    st.write(
        "Computer Science Major with a background in IT, Machine Learning and Object Oriented Programming. \nI've enjoyed completing and adding \
            on to these fun web projects on the side. Check them out in the Projects section!"
    )
    if st.button("✉ Contact Me"):
        show_contact_form()


# """ EXPERIENCE AND QUALIFICATIONS """
st.write("\n")
st.subheader("Experience and Skill-sets", anchor=False)

description="""
    - <u>Java</u>: 
        - Understanding of Object Oriented Design and workflow with UML and Sequence Diagrams.
        - Experience with team programming projects using agile methedologies
    - <u>Machine Learning: Python</u>
        - Created Machine Learning models from datasets to classify and group user data
        -  (Pandas, Numpy, Sci-kit Learn)
    - <u>Web Design</u>: 
        - Studying through responsive web design with Python, HTML, CSS, and JavaScript projects
    - <u>MySQL Database: Database Management Systems</u>:
        - Developed and managed a small SQL based database with a group member
        - Created schemas and relational diagrams to aid with development
    - <u>Computer Management</u>:
        - Comptia A+ Certified - June 2023
    """
st.markdown(description, unsafe_allow_html=True)

# """ SKILLS """
st.write("\n")
st.subheader("Technical Skills", anchor=False)
st.write(
    """
    - __Languages__: Python, Java, C++, HTML, CSS, MySQL
    - __Computer Science__: Data structures and Algorithms, Agile Workflow, Object Oriented
    Programming, Machine learning
    - __Information Technology__: Networking, Cloud Computing, Troubleshooting, Customer Support
    """
)
st.write("\n")
st.subheader("Key Skills", anchor=False)
st.write(
    """
    - Problem Solving 
    - Adaptable 
    - Learner
    - Collaborative
    """
    )
    
