import streamlit as st
import requests
import json
# from streamlit_lottie import st_lottie
import time

st.set_page_config(page_title="BA Group LLM", page_icon="🧠", layout="wide")

st.title("BA Group LLM Assistant")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

result = {}
# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    result = call_api(user_question)

    response = result.get('generated_response', 'No response body available')
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
        with st.expander("See details"):
                    st.json({
                        "Reference": result.get('referenced_document', 'N/A'),
                        "Status Code": result.get('statusCode', 'N/A'),
                        "Source": result.get('file_location', 'N/A')
                    })
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
