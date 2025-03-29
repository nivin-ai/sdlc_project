from src.sdlc_agenticai.state.state import State
import streamlit as st

class DeployCode:
    def __init__(self, llm):
        self.llm = llm
    def deploy_code(self, state: State)->dict:
        #for the time being, we are just printing the code
        st.sidebar.write("deploying code...")
        deployable_code =  self.llm.invoke(f"Return ONLY the code part from the following: {state['generated_code']}. At the end, give simple instructions as to how to deploy and run this code.")
        st.session_state["state"]["deployable_code"] = deployable_code.content
        st.write(deployable_code.content)
        return {"deployable_code": deployable_code.content}