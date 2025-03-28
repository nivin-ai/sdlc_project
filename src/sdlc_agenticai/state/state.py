from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages


class State(TypedDict):
    current_step: str
    user_requirement: str
    user_story: str
    po_review: str
    design_doc: str
    design_review: str
    generated_code: str
    code_review: str
    security_review: str
    test_cases: str
    test_cases_review: str