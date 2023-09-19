from pathlib import Path

import streamlit as st
from PIL import Image
from streamlit_disqus import st_disqus

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.jpg"
github_icon = current_dir / "assets" / "github_icon.png"


#--- GENERAL SETTINGS ---#
PAGE_TITLE = "Mark Vincent Estrada - CV"
PAGE_ICON = "📄"
NAME = "Mark Vincent Estrada"
CONTACT_NO = "09457194445 / 09474261330"
ADDRESS = "Kapasigan, Pasig City"
DESCRIPTION = """
Graduate of BS Computer Science
"""
EMAIL = "estrada.markvincent.ccs@gmail.com"
SOCIAL_MEDIA = {
     "Youtube": "https://www.youtube.com/channel/UCJP9o9iLVN-mZrO3SgzYfNw",
    "Linkedin": "https://www.linkedin.com/in/mark-vincent-estrada/",
      "Github": "https://github.com/MarkEstrada-CS",
     "Twitter": "",
}

PROJECTS = {
    "📝 **Digital CV**": "https://markestradacv.streamlit.app/",
    "🩸 **Blood eDonate** - A simple blood donation mobile app developed in Kodular": "https://github.com/MarkEstrada-CS/Blood-eDonate",
    "👾 **Space Invader** - An alien shooting game developed in Kodular": "https://github.com/MarkEstrada-CS/CS111-BSCS3A-G2",
    "🗒️ **TTD** - Note-keeping mobile app developed in Kodular": "https://github.com/MarkEstrada-CS/TTD",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

#--st.title("Hello there!")--#

#--- LOAD CSS, PDF, PROFILE PIC ---#

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)
    github_icon = Image.open(github_icon)

    #-- HERO SECTION ---#
    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.title(NAME)
        st.write("**CONTACT**", )
        st.write("📞", CONTACT_NO)
        #--st.write(DESCRIPTION)--
        st.write("🏠", ADDRESS)
        st.write("📧", EMAIL)
        st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
        )

    with col2:
        st.image(profile_pic, width=320)

#--SOCIAL MEDIA LINKS--#
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

#--EXPERINCE & QUALIFICATION--#
st.write("---")
st.write("#")
st.subheader("Objectives")
st.write(
"""
Taking Bachelor of Science in Computer Science at Pamantasan
ng Lungsod ng Pasig (PLP), I aim to gather my knowledge and
experience to refine my current skills and acquire additional set
of skills. This will not only benefit me and university but your company
as well by being a good role model

"""
)

#---EDUCATION---#
st.write("#")
st.subheader("Education")
st.write("**Bachelor of Science in Computer Science**")
st.write("*Pamantasan ng Lungsod ng Pasig | 2019 - July 2023*")
st.write("Achievements")
st.write(
"""
- ➤Second Year - Fourth Year Dean's Lister
- ➤Third Year - President's Lister

"""
)

#---SKILLS---#
st.write("#")
st.subheader("Skills")
st.write(
"""
- ➤MIT App Inventor / Kodular
- ➤HTML, CSS, JavaScript
- ➤WordPress
- ➤C++

"""
)

#-- WORK HISTORY --#
st.write("#")
st.subheader("Work Experience")
st.write("---")

#--JOB1--#
st.write("**SPES** | **Pasig City Hall**")
st.write("*March 2015 - April 2015 | San Nicolas, Pasig City*")
st.write(
"""
- ➤Assisting medical personnels in carrying medical equipments during visits on different barangays
- ➤Helping in encoding patient's information using microsoft excel

"""
)

#--JOB2--#
st.write("#")
st.write("**INTERN** | **Wellness PRO Inc.**")
st.write("*March 2023 - April 2023 | Kapitolyo, Pasig City*")
st.write(
"""
- ➤Digitalizing employee 201 files and Service Reports
- ➤RFID encoding
- ➤Designing company website using Wordpress

"""
)

#--PROJECTS--#
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
st.write("---")

st_disqus("markestradacv")
