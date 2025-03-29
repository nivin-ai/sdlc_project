from src.sdlc_agenticai.state.state import State
import streamlit as st

class SecurityReview:
    def __init__(self, llm):
        self.llm = llm
    def generate_security_review(self, state: State)->dict:
        st.sidebar.write("performing security review on code...")
        security_review =  self.llm.invoke(f"You are a computer security expert. Perform a security review on the following code: {state['generated_code']}. Refer User requirement: {state['user_requirement']}, User Story: {state['user_story']}. If the code document is approved, only return 'Approved' and NOTHING ELSE, DO NOT give any suggestions or Feedback. Else, return 'Failed' with feedback as to how to improve.")
        st.session_state["state"]["security_review"] = security_review.content
        return {"security_review": security_review.content}
    
    def decide_next(self, state: State):
        if state["security_review"] == "Approved":
            st.sidebar.write("security review passed")
            return "generate_test_cases"
        else:
            st.sidebar.write("security review failed")
            return "generate_code"