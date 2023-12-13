from a3d.a3dmodel import A3DModel
from a3d.a3dcontroler import A3DControler
from a3d.a3d_teksten import A3DTeksten
import streamlit as st
import time

class A3DGUI:
    def __init__(self):
        self.a3dmod = A3DModel()
        self.a3dcon = A3DControler(self.a3dmod)
        self.a3dtekst = A3DTeksten()
        if 'var' not in st.session_state:
            st.session_state['var'] = 0
        if 'naam' not in st.session_state:
            st.session_state['naam'] = ''

    def start(self): 
        # haal data uit de url
        url = st.experimental_get_query_params()
        if url != {}:
            if 'var' in url:
                var = url['var'][0]
                st.session_state['var'] = var                   
            if 'naam' in url:
                naam = url['naam'][0]
                st.session_state['naam'] = naam                       
        self.build_gui()

    # Bouw GUI op ========================================================
    def build_gui(self):
        st.subheader("☯️ Vraag & Antwoord 🛠️ Training ⚙️")
        with st.form('my_form'):
            with st.expander("🪁: **Lees mij:** Gebruiksaanwijzingen & Achtergrondinformatie"):
                st.write(self.a3dtekst.get_intro_tekst())
            text = st.text_area('Stel hier zo gedetailleerd mogelijk je vraag:', '')
            submitted = st.form_submit_button('Versturen')
            if submitted:               
                self.send_question(text)

    # Workers =============================================================
    # Callbacks ====================================
    def send_question(self, user_question):
        # placeholder voor de loader 
        preloader = st.empty()   
        preloader.text("🕵️ Een moment geduld a.u.b...")  
        antwoord = self.a3dcon.ask_the_database(user_question)       
        if antwoord == 'NOPE':
            st.write("ℹ️: Geen antwoord gevonden in de database 🕵️ ...")  
            antwoord2 = self.a3dcon.ask_model(user_question)
            if antwoord2 == 'NOPE':                  
                st.warning( self.a3dtekst.get_geen_ai_antwoord(user_question) )  
                preloader.empty()
            else:
                st.info(f"💡**Antwoord Fine-tuned Model:** {antwoord2}")  
                preloader.empty()        
        else:
            st.info(f"💡**Antwoord Database:** {antwoord}")
            preloader.empty()





    
    


