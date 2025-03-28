from src.sdlc_agenticai.state.state import State
import streamlit as st

class GenerateCode:
    def __init__(self, llm):
        self.llm = llm
    def generate_code(self, state: State)->dict:
        generated_code =  self.llm.invoke(f"Generate the code for the following use case-User Requirement: {state['user_requirement']} \n\n User Story: {state['user_story']} \n\n. Refer the following design document, give it the highest importance: {state['design_documents']}.")
        st.session_state["state"]["generated_code"] = generated_code.content
        return {"generated_code": generated_code.content}