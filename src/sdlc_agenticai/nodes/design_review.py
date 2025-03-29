from src.sdlc_agenticai.state.state import State
import streamlit as st

class DesignReview:
    def __init__(self, llm):
        self.llm = llm
    def generate_design_review(self, state: State)->dict:
        st.sidebar.write("performing design review...")
        design_review =  self.llm.invoke(f"Generate a review for the following design documents for the requirement {state['user_requirement']}: {state['design_documents']}. If the design document is approved, only return 'Approved' and NOTHING ELSE, DO NOT give any suggestions or Feedback. Else, return 'Failed' with feedback as to how to improve. Fail only if it is really bad.")
        st.session_state["state"]["design_review"] = design_review.content
        return {"design_review": design_review.content}
    
    def decide_next(self, state: State):
        if "Approved" in state["design_review"]:
            st.sidebar.write("design review passed")
            return "generate_code"
        else:
            st.sidebar.write("design review failed")
            return "create_design_documents"