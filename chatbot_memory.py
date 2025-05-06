from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

llm= HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-alpha" ,
    task="text-generation"
)

model = ChatHuggingFace(llm = llm )

st.title("🗣️ Open-Source AI Chatbot")

user_input = st.text_input("You: ")
if st.button("Send"):
    if user_input.strip():
        response = model.invoke(user_input)
        st.write("🤖 AI:", response.content)  
    else:
        st.warning("⚠️ Please enter a message!")