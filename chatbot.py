from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai;

# Set up API key using environment variable (recommended)
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# initialise model
model = genai.GenerativeModel('gemini-pro')
# 
chat = model.start_chat(history=[])
def getGeminResponse(question):
    response=chat.send_message(question,stream=True)
    return response
# initialise streamlit
st.set_page_config(page_title='Gemin')
st.header("GenAi Chatbot")

# initialize session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
# inputs
input= st.text_input("Input",key="input")
submit=st.button("Ask Me")

if submit and input:
    response=getGeminResponse(input)
    # add user query and response to session state
    st.session_state['chat_history'].append(("You",input))
    for chunk in response:
        st.session_state["chat_history"].append(("Bot",chunk.text))
    st.subheader("The chat history is")
    for role,text in st.session_state['chat_history']:
        st.write(f"{role}: {text}")







