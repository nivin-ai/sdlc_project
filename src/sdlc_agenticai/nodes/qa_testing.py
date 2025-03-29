from src.sdlc_agenticai.state.state import State
import streamlit as st

class QATesting:
    def __init__(self, llm):
        self.llm = llm
    def qa_testing(self, state: State)->dict:
        st.sidebar.write("performing qa testing...")
        qa_test_review =  self.llm.invoke(f"You are a software engineer. Perform QA testing by applying the following test cases: {state['test_cases']}\n\n on the following code: {state['generated_code']}. \n\nRefer User requirement: {state['user_requirement']},\n\n User Story: {state['user_story']}.\n\n If the test cases pass, only return 'Approved' and NOTHING ELSE, DO NOT give any suggestions or Feedback. Else, return 'Failed' with feedback on what went wrong and how to improve the code.")
        st.session_state["state"]["qa_test_review"] = qa_test_review.content
        return {"qa_test_review": qa_test_review.content}
    
    def decide_next(self, state: State):
        if "Approved" in state["qa_test_review"]:
            st.sidebar.write("qa test passed")
            return ""
        else:
            st.sidebar.write("qa test failed")
            return "generate_code"