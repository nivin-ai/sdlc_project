from src.sdlc_agenticai.ui.streamlitui.load_ui import LoadUI
from src.sdlc_agenticai.llm.groqllm import GroqLLM
import streamlit as st

def initialize_session():
        return {
            "current_step": "requirements",
            "user_requirement": "",
            "user_story": "",
            "po_review": "",
            "design_doc": "",
            "design_review": "",
            "generated_code": "",
            "code_review": "",
            "security_review": "",
            "test_cases": "",
            "test_cases_review": "",
        }

def load_sldc_agent():
    if "user_controls" not in st.session_state:
        st.session_state["user_controls"] = {}
    if "state" not in st.session_state:
        st.session_state["state"] = initialize_session()

    ui = LoadUI()
    ui.load_ui()
    if st.session_state["user_controls"]["GROQ_API_KEY"] != "":
        groq_llm = GroqLLM(st.session_state["user_controls"])
        llm = groq_llm.get_llm_model()
        st.sidebar.write(f"LLM has been fetched: {llm}")
    