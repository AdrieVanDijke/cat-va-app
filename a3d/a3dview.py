from a3d.a3dmodel import A3DModel
from a3d.a3dcontroler import A3DControler
import streamlit as st
#import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Maar een keer uitvoeren om data te downloaden:
#nltk.download('punkt')
#nltk.download('stopwords')

class A3DGUI:
    def __init__(self):
        self.a3dmod = A3DModel()
        self.a3dcon = A3DControler(self.a3dmod)

    def start(self):    
        self.build_gui()

    # Bouw GUI op ========================================================
    def build_gui(self):
        st.subheader("Vraag & Antwoord")
        with st.expander("ℹ️ **Lees mij:** Gebruiksaanwijzingen & Achtergrondinformatie"):
            st.write(self.expander_text())
        user_question = st.text_input("Stel hier je vraag *en klik op Enter om de vraag te versturen:*")       
        if user_question:
            if len(user_question) > 0:
                self.send_question(user_question)
        #if st.button('Versturen'):
            #self.send_question(user_question)

    # Workers =============================================================
    # Callbacks ====================================
    def send_question(self, user_question):
        st.info(f"❔ **Je vraag:** {user_question}")
        antwoord = self.a3dcon.ask_the_database(user_question)
        if antwoord == 'NOPE':
            keywords = self.extract_keywords(user_question) 
            st.write("Een moment geduld nog a.u.b...") 
            antwoord2 = self.a3dcon.ask_the_database(keywords)
            if antwoord2 == 'NOPE':
                st.warning( self.antwoord_nope(user_question) )                      
            else:
                st.success(f"💡**Antwoord:** {antwoord2}")            
        else:
            st.success(f"💡**Antwoord:** {antwoord}")

    # Expander tekst ================================
    def expander_text(self):        
        extekst = """
                Dit is een Vraag en Antwoord module die gebruik maakt van AI *(kunstmatige intelegentie)* om antwoorden op je vragen te geven.
                Dit is geen Chat-bot en je kunt geen uitgebreide gesprekken voeren met deze AI simpelweg omdat als je een nieuwe vraag stelt de vorige vraag en het antwoord daarop niet in het geheugen worden opgeslagen.
                - Type in het tekst veld hieronder je vraag in gewoon Nederalands en druk op **Enter** om de vraag te versturen.
                - Probeer je vraag zo goed *(en duidelijk)* mogelijk te formuleren om de AI zo veel mogelijk bruikbare informatie te geven om een goed antwoord te kunnen geven. 
                *Vermeld b.v. of je een vergoedbare of niet vergoedbare therapeut bent als je vraag betrekking heeft op je beroepsorganisatie.*
                - Als je je vraag hebt verstuurd gaat er rechtsboven een animatie draaien om aan te geven dat de AI aan het werk is.
                """       
        return extekst
    
    # Antwoord: geen resultaat ====================
    def antwoord_nope(self, user_question):
        antwoord = f"""
            🤷‍♀️ Het spijt me maar ik kan het antwoord op je vraag "**{user_question}**" niet vinden. 
            *Misschien kun je de vraag nog een keer in andere woorden stellen?* Of stel een nieuwe vraag en neem later contact met ons op:
            - Je kunt *(indien gewenst)* op de "Service + Contact" pagina een belafspraak maken of *(onder werktijden)* live chatten met een van onze medewerkers.\n
            💡Hier nog een paar links die je misschien verder kunnen helpen:
            - [Onze kennisbank](https://kwaliteitsysteem.nl/kennisbank/) *Alles waar je als CAT-therapeut mee te maken hebt of kunt krijgen*
            - [GRO: vind een geschikte opleiding](https://gatregisteropleidingen.nl) *Alternatieve zorg opleidingen, scholingen, module opleidingen en bij- en nascholingen*
            - [Catcollectief.nl](https://catcollectief.nl/): [Profiel CAT-therapeut](https://catcollectief.nl/profiel/) 
            - [Catvergoedbaar.nl](https://catvergoedbaar.nl/): [Profiel Vergoedbare CAT-therapeut](https://catvergoedbaar.nl/profiel/)
            """
        return antwoord

    # Extract keywords ==============================
    def extract_keywords(self, query):
        stop_words = set(stopwords.words('dutch'))
        word_tokens = word_tokenize(query)
        keywords = [word for word in word_tokens if word not in stop_words]
        # Vervang dubbele woorden door 1 woord
        keywords = list(dict.fromkeys(keywords))
        # vervang "kost" door "kosten"
        keywords = [word.replace('kost', 'kosten') for word in keywords]    
        # haal alle leestekens uit de lijst
        keywords = [word for word in keywords if word.isalnum()]
        # haal alle woorden als de, het, een, etc. uit de lijst
        keywords = [word for word in keywords if len(word) > 2]
        # haal alle woorden als wat, wie, waar, etc. uit de lijst
        keywords = [word for word in keywords if word not in ['wat', 'wie', 'waar', 'wanneer', 'hoe', 'waarom', 'weet', 'Wat', 'Wie', 'Waar', 'Wanneer', 'Hoe', 'Waarom']]    
        # maak een string van de lijst
        keywords = ' '.join(keywords)
        return keywords
    


