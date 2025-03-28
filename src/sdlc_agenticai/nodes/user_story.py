from src.sdlc_agenticai.state.state import State
import streamlit as st

class UserStory:
    def __init__(self, llm):
        self.llm = llm
    def create_user_story(self, state: State)->dict:
        st.write(f"node: user story,  graph state: {state}")
        user_story =  self.llm.invoke(f"Create a user story for the following requirement: {state['user_requirement']}")
        #st.write(user_story.content)
        st.session_state["state"]["user_story"] = user_story.content
        #state["user_story"] = user_story.content
        #st.write(st.session_state["state"])
        return {"user_story": user_story.content}