from src.sdlc_agenticai.state.state import State
import streamlit as st

class UserStory:
    def __init__(self, llm):
        self.llm = llm
    def create_user_story(self, state: State)->dict:
        st.sidebar.write("generating user story...")
        user_story =  self.llm.invoke(f"Create a user story for the following requirement: {state['user_requirement']}. Consider the following feedback to create better user stories: {state["po_review"]}.")
        st.session_state["state"]["user_story"] = user_story.content
        return {"user_story": user_story.content}