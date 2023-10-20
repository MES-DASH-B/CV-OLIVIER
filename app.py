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
ADRESSE = "4ème Rue du sauveur, 69007 LYON, FRANCE"
DESCRIPTION = """ 
ASPIRANT MANAGER DE PROJET D'INNOVATION, INDUSTRIE 4.0/RECHERCHE D'ALTERNANCE (CONTRAT D'APPRENTISSAGE)/FORMATION EN COURS(MASTÈRE SPÉCIALISÉ)
"""
EMAIL = "youmbio@yahoo.com"
LinkedIn = "https://www.linkedin.com/in/ornello-olivier-youmbi-1a66b1184/"
Projet_1 = "https://abc-cocacola-lytics-03.streamlit.app/"
Projet_2 = "https://maint-cocacola.streamlit.app/"

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
        label="📥 Mon CV détaillé ",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

#st.write("#")
#cols = st.columns(len(PROJETS))
#for index, (platform, link) in enumerate(PROJETS.items()):
    #cols  [index].write(f"[{platform}]({link})")

#st.write("#")
st.subheader("🦺 EXPERIENCES PROFESSIONNELLES")
st.write (
    """
- ✅  (Jan.2022 - Oct.2023) PILOTE DU PROCESSUS RESSOURCES MATERIELLES : CocaCola Sénégal (IBS) 
- ✅  (Jan.2021 - Jan.2022) TECHNICIEN AUTOMATISME INDUSTRIEL : Groupe Castel Cameroun (SABC)
- ✅  (Mars.2020 - Août.2020) TECHNICIEN AUTOMATISME INDUSTRIEL : Groupe Castel Cameroun 
- ✅  (Août.2019 - Déc.2019) STAGIAIRE MAINTENANCES INDUSTRIELLE : Groupe Castel Cameroun
- ✅  (Mai.2017 - Sept.2017) STAGIAIRE AUTOMATISME INDUSTRIEL : Groupe Castel Cameroun
"""
)
st.write("🔴 Projet_1", Projet_1 )
st.write("🔴 Projet_2", Projet_2 )
st.write("🔗 LinkedIn", LinkedIn )

st.write("#")
st.subheader("👨🏾‍🎓 PARCOURS ACADÉMIQUE")
st.write (
    """
- ✅  (2023 - 2024) MASTÈRE SPÉCIALISÉ MANAGER DE PROJET D'INNOVATION, I4.0 : Lyon, France🇫🇷
- ✅  (2018 - 2020) MASTER EN GENIE INDUSTRIEL ET MAINTENANCE : Douala, Cameroun🇨🇲
- ✅  (2016 - 2017) LICENCE GENIE ELECTRIQUE / INFORMATIQUE INDUSTRIELLE : Douala, Cameroun🇨🇲
- ✅  (2014 - 2016) BTS INFORMATIQUE INDUSTRIELLE Douala, Cameroun🇨🇲
"""
)

st.write("#")
st.subheader("💯 COMPÉTENCES")
#st.write ("---")

#st.write ("Pilote processus ressurse materiel")
#st.write ("05/01/2022 -- 30/09/2023")
st.write (
    """
- ✅  Automatisme Industriel (Programmation des API)
- ✅  Maintenance industrielle (TPM Management)
- ✅  Analyse de données et reporting (Excel, Python, Streamlit...)
"""
)



