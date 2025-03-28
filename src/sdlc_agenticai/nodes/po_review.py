from src.sdlc_agenticai.state.state import State
import streamlit as st

class POReview:
    def __init__(self, llm):
        self.llm = llm
    def po_review(self, state: State)->dict:
        #st.write(f"node: po review,  graph state: {state}")
        po_review =  self.llm.invoke(f"As a product owner, give a review for the following user story for the requirement {state["user_requirement"]}: {state["user_story"]}. If the user story is approved, simply return 'Approved' and NOTHING ELSE, do not give any suggestions. Else, return 'Failed' with feedback as to how to improve.")
        #st.write(user_story.content)
        st.session_state["state"]["po_review"] = po_review.content
        #state["user_story"] = user_story.content
        #st.write(st.session_state["state"])
        return {"po_review": po_review.content}
    
    def decide_next(self, state: State):
        if state["po_review"] == "Approved":
            return "create_design_documents"
        else:
            return "create_user_story"