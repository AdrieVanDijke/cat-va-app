
class A3DTeksten:
    def __init__(self):
        pass

    # tekst voor de introductie van de GUI    
    def get_intro_tekst(self):
        intro_tekst = """
        Dit is een Vraag en Antwoord module die gebruik maakt van AI *(kunstmatige intelegentie)* om antwoorden op je vragen te geven.
        *Dit is geen Chat-bot en je kunt geen uitgebreide gesprekken voeren met deze AI simpelweg omdat als je een nieuwe vraag stelt de vorige vraag en het antwoord daarop niet in het geheugen worden opgeslagen.*
        - Type in het tekst veld hieronder je vraag in gewoon Nederalands.
          - *Probeer je vraag zo goed, uitgebreid en duidelijk mogelijk te formuleren.* 
        - Druk op **Ctrl + Enter** *(of klik op de **Versturen knop)*** om de vraag te versturen.
        """
        return intro_tekst
    
    # template voor de prompt die naar de OpenAI API wordt gestuurd met Pinecone als retriever   
    def get_db_prompt_template(self):
        prompt_template = """Gebruik de onderstaande context om de vraag aan het einde zo gedetailleerd mogelijk te beantwoorden. Vermijd het vermelden van de context zoals b.v. in: 'In de context staat...'. 
        Als je het antwoord niet weet, of twijfeld aan de juistheid van het antwoord, antwoord dan met alleen het woord: 'NOPE'. Verzin geen antwoord, URL's, namen of andere informatie die niet direct uit de context gehaald kan worden. 
        Concentreer je op de vraag en het beantwoorden daarvan zonder overbodige informatie te geven die niets met de vraag te maken heeft. Neem de tijd om een goed antwoord te vinden.
        Wanneer er gevraagd wordt naar geschikte opleidingen, geef dan de volgende link: https://gatregisteropleidingen.nl/opleiding-scholing-zoeken/

        {context}

        Vraag: {question}

        Antwoord in het Nederlands.
        
        Antwoord:
        """
        return prompt_template
    
    # template voor de prompt die naar de OpenAI API wordt gestuurd met een fine-tuned model
    def get_qa_system_prompt(self):
        system_prompt = """Je naam is CATja. je bent een vriendelijke AI assistent in dienst van beroepsorganisatie CAT die vragen van therapeuten gedetaileerd beantwoord.
        Geef nauwkeurige, feitelijke antwoorden op de vragen van de therapeuten. Verzin geen informatie. Als je het antwoord niet weet (of als je twijfeld) antwoord dan met alleen het woord: 'NOPE'.
        Verzin nooit zo maar een url, namen of andere informatie die niet direct uit de trainingsdata gehaald kunnen worden. Antwoord nooit met een vraag.
        Alle therapeuten die aangesloten zijn bij CAT maken gebruik van het accountsysteem op kwaleitsysteem.nl. Informatie over het accountsysteem en alle bijkomende zaken is te vinden in onze kennisbank: https://kwaliteitsysteem.nl/kennisbank/.       
        Als er gevraangd wordt naar opleidingen antwoorde dan met de volgende link: https://gatregisteropleidingen.nl/opleiding-scholing-zoeken/"""
        return system_prompt

    # tekst voor als er geen antwoord gevonden is in de database
    def get_geen_ai_antwoord(self, user_question):
        geen_antwoord = f"""
            🤷‍♀️ Het spijt me maar ik kan het antwoord op je vraag "**{user_question}**" niet vinden. 
            *Misschien kun je de vraag nog een keer in andere woorden stellen?* Of stel een nieuwe vraag en neem later contact met ons op:
            - Je kunt *(indien gewenst)* op de "**[Service + Contact](https://kwaliteitsysteem.nl/contact-center/)**" pagina een belafspraak maken of *(onder werktijden)* live chatten met een van onze medewerkers.\n
            💡Hier nog een paar links die je misschien verder kunnen helpen:
            - [Onze kennisbank](https://kwaliteitsysteem.nl/kennisbank/) *Alles waar je als CAT-therapeut mee te maken hebt of kunt krijgen*
            - [GRO: vind een geschikte opleiding](https://gatregisteropleidingen.nl) *Alternatieve zorg opleidingen, scholingen, module opleidingen en bij- en nascholingen*
            - [Catcollectief.nl](https://catcollectief.nl/): **[Profiel CAT-therapeut](https://catcollectief.nl/profiel/)** 
            - [Catvergoedbaar.nl](https://catvergoedbaar.nl/): **[Profiel Vergoedbare CAT-therapeut](https://catvergoedbaar.nl/profiel/)**
            """
        return geen_antwoord
