from langgraph.graph import StateGraph, START, END, MessagesState
from src.sdlc_agenticai.state.state import State
from src.sdlc_agenticai.nodes.user_story import UserStory
from src.sdlc_agenticai.nodes.po_review import POReview
from src.sdlc_agenticai.nodes.design_documents import DesignDocuments
from src.sdlc_agenticai.nodes.design_review import DesignReview
from src.sdlc_agenticai.nodes.generate_code import GenerateCode
from src.sdlc_agenticai.nodes.code_review import CodeReview
from src.sdlc_agenticai.nodes.security_review import SecurityReview
from src.sdlc_agenticai.nodes.test_cases import GenerateTestCases

class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        self.graph_builder = StateGraph(State)

    def build_graph(self):
        self.user_story_node = UserStory(llm=self.llm)
        self.po_review_node = POReview(llm=self.llm)
        self.design_documents_node = DesignDocuments(llm=self.llm)
        self.design_review_node = DesignReview(llm=self.llm)
        self.code_generation_node = GenerateCode(llm=self.llm)
        self.code_review_node = CodeReview(llm=self.llm)
        self.security_review_node = SecurityReview(llm=self.llm)
        self.test_cases_node = GenerateTestCases(llm=self.llm)
        self.graph_builder.add_node("create_user_story", self.user_story_node.create_user_story)
        self.graph_builder.add_node("generate_po_review", self.po_review_node.po_review)
        self.graph_builder.add_node("create_design_documents", self.design_documents_node.generate_design_documents)
        self.graph_builder.add_node("generate_design_review", self.design_review_node.generate_design_review)
        self.graph_builder.add_node("generate_code", self.code_generation_node.generate_code)
        self.graph_builder.add_node("generate_code_review", self.code_review_node.generate_code_review)
        self.graph_builder.add_node("generate_security_review", self.security_review_node.generate_security_review)
        self.graph_builder.add_node("generate_test_cases", self.test_cases_node.generate_test_cases)
        
        self.graph_builder.add_edge(START, "create_user_story")
        self.graph_builder.add_edge("create_user_story", "generate_po_review")
        self.graph_builder.add_conditional_edges("generate_po_review", self.po_review_node.decide_next)
        self.graph_builder.add_edge("create_design_documents", "generate_design_review")
        self.graph_builder.add_conditional_edges("generate_design_review", self.design_review_node.decide_next)
        self.graph_builder.add_edge("generate_code", "generate_code_review")
        self.graph_builder.add_conditional_edges("generate_code_review", self.code_review_node.decide_next)
        self.graph_builder.add_conditional_edges("generate_security_review", self.security_review_node.decide_next)
        
        return self.graph_builder.compile()
