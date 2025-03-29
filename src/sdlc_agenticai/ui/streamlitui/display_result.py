import streamlit as st


class DisplayResult:
    def __init__(self, graph, user_requirement):
        self.graph = graph
        self.user_requirement = user_requirement

    def display_result(self):
        # for event in self.graph.invoke({"user_requirement": st.session_state["state"]["user_requirement"]}):
        #     st.write(event)
         for event in self.graph.stream(st.session_state["state"]):
             st.session_state["state"]["current_step"] = f"event: {event}"