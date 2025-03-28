import streamlit as st
from src.sdlc_agenticai.ui.streamlitui.uiconfig import Config


class LoadUI:
    def __init__(self):
        self.config = Config()


    def load_centrepage(self):
        # Main interface
        st.title("what do you want to make?")

        # Text area for app description
        app_description = st.text_area("describe what you want to create")
        st.session_state["state"]["user_requirement"] = app_description

        # button
        if st.button("create"):
            with st.spinner("working on it..."):
                st.write("model will respond here")

    def load_sidebar(self):
        # Sidebar for API key and model selection
        st.sidebar.header("Settings")
        groq_api_key = st.sidebar.text_input("Groq API Key", type="password")
        st.session_state["user_controls"]["GROQ_API_KEY"] = groq_api_key
        model_options = self.config.get_llm_options()
        groq_model = st.sidebar.selectbox("Groq Model", model_options)
        st.session_state["user_controls"]["GROQ_MODEL"] = groq_model
        st.sidebar.write(st.session_state)



    def load_ui(self):

        self.load_sidebar()

        self.load_centrepage()