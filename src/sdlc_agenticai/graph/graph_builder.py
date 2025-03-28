from langgraph.graph import StateGraph, START, END, MessagesState
from src.sdlc_agenticai.state.state import State
from src.sdlc_agenticai.nodes.user_story import UserStory
from src.sdlc_agenticai.nodes.po_review import POReview

class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        self.graph_builder = StateGraph(State)

    def build_graph(self):
        self.user_story_node = UserStory(llm=self.llm)
        self.po_review_node = POReview(llm=self.llm)
        self.graph_builder.add_node("create_user_story", self.user_story_node.create_user_story)
        self.graph_builder.add_node("generate_po_review", self.po_review_node.po_review)
        
        self.graph_builder.add_edge(START, "create_user_story"),
        self.graph_builder.add_edge("create_user_story", "generate_po_review")
        self.graph_builder.add_edge("generate_po_review", END)
        
        return self.graph_builder.compile()
