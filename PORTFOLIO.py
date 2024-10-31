import streamlit as st

# Page Configurations
st.set_page_config(page_title="Joe Daniel's Portfolio", page_icon=":wave:", layout="wide")

# Styling
st.markdown("""
    <style>
        /* Main Title Style */
        .main-title {color: #2C3E50; font-size: 50px; text-align: center; font-weight: bold; animation: fadeIn 2s ease-in-out;}
        /* Section and Subsection Headers */
        .section-header {color: #2980B9; font-size: 28px; font-weight: bold; margin-top: 20px; text-decoration: underline;}
        .subsection-header {color: #34495E; font-size: 22px; font-weight: bold; padding-top: 10px;}
        /* Info and Contact Styles */
        .info {font-size: 16px; line-height: 1.6; padding-bottom: 15px; color: #34495E;}
        .contact-links a {text-decoration: none; color: #27AE60; font-weight: bold;}
        .container {background-color: #ECF0F1; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); margin-bottom: 20px;}
        /* Social Icons */
        .social-icons {text-align: center; margin-top: 20px;}
        .social-icons a {margin: 0 10px; text-decoration: none; font-size: 24px; color: #34495E; transition: color 0.3s;}
        .social-icons a:hover {color: #27AE60;}
        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>
""", unsafe_allow_html=True)

# Main Title
st.markdown("<div class='main-title'>Joe Daniel's Portfolio</div>", unsafe_allow_html=True)

# Introduction Section with Animation and Image
st.write("## :wave: Hello, I am Joe Daniel")
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    st.image("myself.jpg", width=200, caption="BTech Student | AI & Data Science Enthusiast")

st.write("""
    Welcome! I am a BTech student specializing in Artificial Intelligence and Data Science, currently in my first year. 
    I have successfully completed a comprehensive Full Stack development course, equipping me with a robust foundation 
    in both frontend and backend technologies.

    My journey in tech has provided me with a strong base in frontend development, where I have gained proficiency in 
    HTML, CSS, and JavaScript, enabling me to create visually appealing and user-friendly interfaces. I enjoy crafting 
    responsive designs that enhance user experience and engagement.

    In addition to my frontend skills, I have a solid understanding of backend development, working with frameworks 
    such as Django and Express.js, and databases like MongoDB and SQLite. This holistic approach allows me to understand 
    the complete development lifecycle and contribute effectively to projects.

    I am passionate about leveraging technology to tackle real-world challenges. I actively seek opportunities to apply 
    my skills in innovative projects and collaborations within the tech community. My goal is to combine my knowledge of 
    AI and Data Science with my development skills to create impactful solutions that drive efficiency and improve user experiences.
""")

# Tabs for Content Organization
tab1, tab2, tab3 = st.tabs(["Education", "Skills", "Contact"])

# Education Section
with tab1:
    st.markdown("<div class='section-header'>Education Qualification</div>", unsafe_allow_html=True)
    st.write("**B.Tech in Artificial Intelligence and Data Science** - 1st Year")
    st.write('''
        - **College**: [KGISL Institute of Technology](https://www.kgkite.ac.in/)
        - **Location**: Saravanampatti, Coimbatore
    ''')

# Skills Section with Progress Bars
with tab2:
    st.markdown("<div class='section-header'>Skills</div>", unsafe_allow_html=True)
    st.write('**Programming Languages**')
    st.progress(0.8)
    st.write('Python, C++, Full Stack, MERN Stack')
    st.write('**Frameworks & Libraries**')
    st.progress(0.6)
    st.write('Django, Streamlit, Pandas, Tkinter')
    st.write('**Databases**')
    st.progress(0.5)
    st.write('SQLite, MongoDB')
    st.write('**Tools & Technologies**')
    st.progress(0.7)
    st.write('Git, Visual Studio Code, Pycharm, Xampp, Jupyter Notebook')
    st.write('**Soft Skills**')
    st.progress(0.9)
    st.write('Leadership, Problem Solving, Communication')

# Contact Section with Interactive Feedback Form
with tab3:
    st.markdown("<div class='section-header'>Contact Me</div>", unsafe_allow_html=True)
    st.write("Feel free to connect with me on my social profiles or reach out directly:")
    st.markdown("""
        <div class='social-icons'>
            <a href="https://github.com/joedanields" target="_blank"><i class="fab fa-github"></i></a>
            <a href="mailto:joedanielajd@gmail.com" target="_blank"><i class="fas fa-envelope"></i></a>
            <a href="https://www.linkedin.com/in/joe-daniel-ba3300308/" target="_blank"><i class="fab fa-linkedin"></i></a>
            <a href="https://www.instagram.com/night_shades_1920/" target="_blank"><i class="fab fa-instagram"></i></a>
        </div>
    """, unsafe_allow_html=True)

    # Feedback Form
    st.subheader("Leave a Message")
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    if st.button("Send Message"):
        if name and email and message:
            st.success("Thank you for your message! I'll get back to you soon.")
        else:
            st.error("Please fill out all fields before submitting.")

# Font Awesome Icons Link
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
""", unsafe_allow_html=True)
