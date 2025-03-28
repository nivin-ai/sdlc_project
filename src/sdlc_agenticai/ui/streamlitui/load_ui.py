import streamlit as st
from src.sdlc_agenticai.ui.streamlitui.uiconfig import Config


class LoadUI:
    def __init__(self):
        self.config = Config()


    def load_ui(self):
        # Sidebar for API key and model selection
        st.sidebar.header("Settings")
        groq_api_key = st.sidebar.text_input("Groq API Key", type="password")
        model_options = self.config.get_llm_options()
        groq_model = st.sidebar.selectbox("Groq Model", model_options)

        # Main interface
        st.title("what do you want to make?")

        # Text area for app description
        app_description = st.text_area("describe what you want to create")

        # button
        if st.button("create"):
            st.write("on it!")