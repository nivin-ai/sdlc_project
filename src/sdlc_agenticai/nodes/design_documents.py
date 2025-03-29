from src.sdlc_agenticai.state.state import State
import streamlit as st

class DesignDocuments:
    def __init__(self, llm):
        self.llm = llm
    def generate_design_documents(self, state: State)->dict:
        st.sidebar.write("generating design documents...")
        design_documents =  self.llm.invoke(f"Create really good, top notch, both functional and technical design documents based on the following. Requirement: {state['user_requirement']}. User story: {state['user_story']}.")
        st.session_state["state"]["design_documents"] = design_documents.content
        return {"design_documents": design_documents.content}