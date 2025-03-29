from src.sdlc_agenticai.state.state import State
import streamlit as st

class GenerateTestCases:
    def __init__(self, llm):
        self.llm = llm
    def generate_test_cases(self, state: State)->dict:
        test_cases =  self.llm.invoke(f"As a software engineer, create test cases for the following code: {state['generated_code']}. \n\n User requirement: {state['user_requirement']}")
        st.session_state["state"]["test_cases"] = test_cases.content
        return {"test_cases": test_cases.content}