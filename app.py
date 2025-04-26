import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import streamlit as st
load_dotenv()



api_key = os.getenv("GROQ_API_KEY")

st.title("langchain first UI project")
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=api_key,
)


input=st.text_input("Search any topic here")
if input:
    response = llm.invoke(input+"Please give me consize answer in short form in just lines")
    st.write(response.content)



