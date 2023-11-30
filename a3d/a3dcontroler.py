import pinecone 
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
#import logging

#logging.basicConfig(level=logging.DEBUG)

class A3DControler:
    def __init__( self, a3dmod ):
        self.a3dmod = a3dmod

    # vraag het de Pinecone database ======================================
    def ask_the_database(self, query):
        pinecone.init(api_key=self.a3dmod.pinecone_api_key, environment=self.a3dmod.pinecone_environment)
        index = pinecone.Index(self.a3dmod.pinecone_index_name)
        embeddings = OpenAIEmbeddings() 
        vectorstore = Pinecone(index, embeddings, "text")            
        prompt_template = """Gebruik de volgende context om de vraag aan het einde te beantwoorden. 
        Als je het antwoord niet weet, antwoord dan met alleen het woord:'NOPE'
        Verzin geen antwoord, url's, namen of andere informatie die je niet kunt halen uit de context. 
        Als er gevraagd wordt waar geschikte opleidingen te vinden zijn geef dan altijd de volgende link: https://gatregisteropleidingen.nl/opleiding-scholing-zoeken/

        {context}
        
        Vraag: {question}
        Geef een vriendelijk en zo gedetailleerd mogelijk antwoord in het Nederlands."""
        PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

        chain_type_kwargs = {"prompt": PROMPT}
        llm = ChatOpenAI(model_name=self.a3dmod.aimodel, temperature=self.a3dmod.temperature, max_tokens=self.a3dmod.max_tokens)
        qa = RetrievalQA.from_chain_type(
            llm=llm, 
            chain_type='stuff', 
            retriever=vectorstore.as_retriever(),
            chain_type_kwargs=chain_type_kwargs
        )
        result = qa.run(query)               
        return result





        