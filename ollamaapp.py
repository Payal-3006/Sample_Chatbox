from langchain_community.llms import Ollama
import streamlit as st 
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser

#create my prompt

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are helpful assistant. please respond to the questionasked"),
        ("user","Question:{question}")
    ]
)

#sreamlit framework
st.title('Langchain demo Chat App With gemma2:2b')
input_text = st.text_input('What question do you in mind')

#ollama LLM Model
llm=Ollama(model="gemma2:2b")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
