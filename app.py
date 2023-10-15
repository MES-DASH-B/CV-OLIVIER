from pathlib import Path

import streamlit as st

from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

PAGE_TITLE = "Digital CV  YOUMBI OLIVIER"
PAGE_ICON = ":wave"
NAME = "OLIVIER YOUMBI"
TELEPHONE = "+33 7 68 96 44 18"
ADRESSE = "LYON, FRANCE"
DESCRIPTION = """ 
ASPIRANT MANAGER DE PROJET D'INNOVATION, INDUSTRIE 4.0/RECHERCHE D'ALTERNANCE (CONTRAT D'APPRENTISSAGE)/FORMATION EN COURS(MASTERE SPECIALISE)
"""
EMAIL = "youmbio@yahoo.com"
LinkedIn = "https://www.linkedin.com/in/ornello-olivier-youmbi-1a66b1184/"
Projet_1 = "https://ibs-cocacola-lytics-03.streamlit.app/"
Projet_2 = "https://maintibs-cocacola.streamlit.app/"

#PROJETS = {
    #"Projet 1 - description du projet": "https://ibs-cocacola-lytics-03.streamlit.app/",
    #"Projet 2 - description du projet": "https://maintibs-cocacola.streamlit.app/"
#}
st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=320)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📞", TELEPHONE)
    st.write("📍", ADRESSE)
    st.write("📧", EMAIL)
    
    
    st.download_button(
        label=" Dowload Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

#st.write("#")
#cols = st.columns(len(PROJETS))
#for index, (platform, link) in enumerate(PROJETS.items()):
    #cols  [index].write(f"[{platform}]({link})")

#st.write("#")
st.subheader("EXPERIENCES PROFESSIONNELLES")
st.write (
    """
- ✅  ( Jan.2022 - Oct.2023 ) PILOTE DU PROCESSUS RESSOURCES MATERIELLES : COCA COLA SENEGAL ( IBS ) 
- ✅  jhdhsuur jshjofoz ishiueropopuop soijofjoi oshjoe jsojoei seffdsgrgdvdrgrgsrherge
- ✅  kjoijec ioujoejocfj ihuisgryehu copedky ihzoioe ojdcpoeoppopqoiosdbfgdf fbthshdst sthsrthtsdf
- ✅  kjoijec ioujoejocfj ihuisgryehu copedky ihzoioe ojdcpoeoppopqoiosdcs erhryoyigfdser rgser
"""
)
st.write("🔗 Projet_1", Projet_1 )
st.write("🔗 Projet_2", Projet_2 )
st.write("🔗 LinkedIn", LinkedIn )

st.write("#")
st.subheader("Developed Skills")
st.write (
    """
- ✅  7 years of eperience exteacting actionable insights from datac hdqqzdko
- ✅  jhdhsuur jshjofoz ishiueropopuop soijofjoi oshjoe jsojoei seffzdnkkzjoid
- ✅  kjoijec ioujoejocfj ihuisgryehu copedky ihzoioe ojdcpoeoppopqoiozdkzojodjzdozijd
- ✅  kjoijec ioujoejocfj ihuisgryehu copedky ihzoioe ojdcpoeoppopqoiozkzoiudoi
"""
)

st.write("#")
st.subheader("Experience & Qualifications")
st.write ("---")

st.write ("Pilote processus ressurse materiel")
st.write ("05/01/2022 -- 30/09/2023")
st.write (
    """
- ✅  7 years of eperience exteacting actionable insights from datac hdqqsckuzs
- ✅  jhdhsuur jshjofoz ishiueropopuop soijofjoi oshjoe jsojoei seffsnkcjiouzcjgiuyu
- ✅  kjoijec ioujoejocfj ihuisgryehu copedky ihzoioe ojdcpoeoppopqoiozdjsoiuzoi
- ✅  kjoijec ioujoejocfj ihuisgryehu copedky ihzoioe ojdcpoeoppopqoioscnsoiucozudsuzsycihiyis
"""
)



