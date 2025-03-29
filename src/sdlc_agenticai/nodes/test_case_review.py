from src.sdlc_agenticai.state.state import State
import streamlit as st

class TestCaseReview:
    def __init__(self, llm):
        self.llm = llm
    def test_case_review(self, state: State)->dict:
        st.sidebar.write("performing test case review...")
        test_case_review =  self.llm.invoke(f"You are a software engineer. Perform a review on the following test cases: {state['test_cases']}. If the review is approved, ONLY RETURN 'Approved', and NOTHING ELSE, NO FEEDBACK OR SUGGESTIONS. Else, return 'Failed' with feedback on how to improve the test cases.")
        st.session_state["state"]["test_cases_review"] = test_case_review.content
        return {"test_cases_review": test_case_review.content}
    
    def decide_next(self, state: State):
        if state["test_cases_review"] == "Approved":
            st.sidebar.write("test case review passed")
            return "deploy_code"
        else:
            st.sidebar.write("test case review failed")
            return "generate_test_cases"