from a3d.a3dmodel import A3DModel
from a3d.a3dcontroler import A3DControler
from a3d.a3d_teksten import A3DTeksten
import streamlit as st

class A3DGUI:
    def __init__(self):
        self.a3dmod = A3DModel()
        self.a3dcon = A3DControler(self.a3dmod)
        self.a3dtekst = A3DTeksten()
        if 'eerstelader' not in st.session_state:
            st.session_state['eerstelader'] = 'aan'

    def start(self):    
        self.build_gui()

    # Bouw GUI op ========================================================
    def build_gui(self):
        st.subheader("☯️ Vraag & Antwoord 🛠️ Training ⚙️")
        with st.form('my_form'):
            with st.expander("🪁: **Lees mij:** Gebruiksaanwijzingen & Achtergrondinformatie"):
                st.write(self.a3dtekst.get_intro_tekst())
            #st.write("**Jou vraag:**")
            text = st.text_area('Stel hier zo gedetailleerd mogelijk je vraag:', '')
            submitted = st.form_submit_button('Versturen')
            if submitted:
                self.send_question(text)

    # Workers =============================================================
    # Callbacks ====================================
    def send_question(self, user_question):
        #st.info(f"❔ **Je vraag:** {user_question}")
        if st.session_state['eerstelader'] == 'aan':
            st.session_state['eerstelader'] = 'uit'
            st.write("🕵️ Een moment geduld a.u.b...") 
        antwoord = self.a3dcon.ask_the_database(user_question)       
        if antwoord == 'NOPE':
            st.write("ℹ️: Geen antwoord gevonden in de database 🕵️ ...")  
            antwoord2 = self.a3dcon.ask_model(user_question)
            if antwoord2 == 'NOPE':                  
                st.warning( self.a3dtekst.get_geen_ai_antwoord(user_question) )  
            else:
                st.info(f"💡**Antwoord Fine-tuned Model:** {antwoord2}")          
        else:
            st.info(f"💡**Antwoord Database:** {antwoord}")

    
    


