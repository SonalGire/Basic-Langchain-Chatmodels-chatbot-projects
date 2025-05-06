from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st 
import os

load_dotenv()

token = os.getenv("HUGGINGFACEHUB_API_TOKEN")  
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-alpha",
    task="text-generation",
    token=token  
)

st.header("Welcome to Persona world !!")

user_input = st.text_input("What can I help with?")
model = ChatHuggingFace(llm=llm)

if st.button("Execute"):
    result = model.invoke(user_input)
    st.write(result.content)  
