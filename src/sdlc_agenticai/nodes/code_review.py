from src.sdlc_agenticai.state.state import State
import streamlit as st

class CodeReview:
    def __init__(self, llm):
        self.llm = llm
    def generate_code_review(self, state: State)->dict:
        code_review =  self.llm.invoke(f"You are a coding expert. Perform a code review on the following code: {state['generated_code']}. Refer User requirement: {state['user_requirement']}, User Story: {state['user_story']}. If the code document is approved, only return 'Approved' and NOTHING ELSE, DO NOT give any suggestions or Feedback. Else, return 'Failed' with feedback as to how to improve.")
        st.session_state["state"]["code_review"] = code_review.content
        return {"code_review": code_review.content}
    
    def decide_next(self, state: State):
        if state["code_review"] == "Approved":
            return "generate_security_review"
        else:
            return "generate_code"