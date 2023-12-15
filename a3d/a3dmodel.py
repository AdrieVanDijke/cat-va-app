import os
import streamlit as st

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

class A3DModel:
    def __init__(self):
        self.api_openai_key = st.secrets["OPENAI_API_KEY"]
        self.pinecone_api_key = st.secrets["PINECONE_API_KEY"]
        self.pinecone_environment = st.secrets["PINECONE_ENVIRONMENT"]
        self.pinecone_index_name = st.secrets["PINECONE_INDEX_NAME"]
        self.aimodel = "gpt-3.5-turbo"
        self.finemodel = st.secrets["FINETUNED_MODEL"]
        self.temperature = 0.1 
        self.max_tokens = 2000 
        self.fine_temperature = 0.0 
        self.fine_max_tokens = 1000

        
        