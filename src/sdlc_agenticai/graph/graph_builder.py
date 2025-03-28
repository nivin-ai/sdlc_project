from langgraph.graph import StateGraph, START, END, MessagesState
from src.sdlc_agenticai.state.state import State
from src.sdlc_agenticai.nodes.user_story import UserStory

class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        self.graph_builder = StateGraph(State)

    def build_graph(self):
        self.user_story_node = UserStory(llm=self.llm)
        self.graph_builder.add_node("user_story", self.user_story_node.create_user_story)
        
        self.graph_builder.add_edge(START, "user_story"),
        self.graph_builder.add_edge("user_story", END)
        
        return self.graph_builder.compile()
