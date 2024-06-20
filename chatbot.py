from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai;
# set up api key in genai
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# function to load gemini pro model and get response
model=genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])
def getGeminiResponse(question):
    response.chat.send_message(question,stream=True)
    return response
# initialize our streamlit app
st.set_page_config(page_title="Last's Chatbot demo")
st.header("Chatbot")
input=st.text_input("Input",key="input")
submit=st.button("Ask Message")


