from src.sdlc_agenticai.state.state import State
import streamlit as st

class POReview:
    def __init__(self, llm):
        self.llm = llm
    def po_review(self, state: State)->dict:
        st.sidebar.write("performing po review on user story...")
        po_review =  self.llm.invoke(f"As a product owner, review the following user story for the requirement {state['user_requirement']}: {state['user_story']}. If the user story is approved, simply return 'Approved' and NOTHING ELSE, do not give any suggestions. Else, return 'Failed' with feedback as to how to improve.")
        st.session_state["state"]["po_review"] = po_review.content
        return {"po_review": po_review.content}
    
    def decide_next(self, state: State):
        if "Approved" in state["po_review"]:
            st.sidebar.write("po review passed")
            return "create_design_documents"
        else:
            st.sidebar.write("po review failed")
            return "create_user_story"