from langchain_groq import ChatGroq
import streamlit as st

class GroqLLM:
    def __init__(self, user_controls):
        self.user_controls = user_controls

    def get_llm_model(self):
        try:
            groq_api_key = st.session_state["user_controls"]["GROQ_API_KEY"]
            selected_groq_model = st.session_state["user_controls"]["GROQ_MODEL"]
            if groq_api_key == ''  and st.session_state["GROQ_API_KEY"]=='':
                st.error("Please enter your Groq API key.")
            
            llm = ChatGroq(model=selected_groq_model, api_key=groq_api_key)

        except Exception as e:
            raise ValueError(f"Error occured with exception {e}")
        
        return llm