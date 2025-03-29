from src.sdlc_agenticai.state.state import State
import streamlit as st

class GenerateCode:
    def __init__(self, llm):
        self.llm = llm
    def generate_code(self, state: State)->dict:
        st.sidebar.write("generating code...")
        generated_code =  self.llm.invoke(f"Generate really good top notch code considering security as well for the following use case-User Requirement: {state['user_requirement']} \n\n User Story: {state['user_story']} \n\n. Refer the following design document, give it the highest importance: {state['design_documents']}.\n\n Take feedback from the following- Code Feedback: {state['code_review']},\n\n Security Feedback: {state['security_review']}.\n\n QA Testing feedback: {state['qa_test_review']}.")
        st.session_state["state"]["generated_code"] = generated_code.content
        return {"generated_code": generated_code.content}