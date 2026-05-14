from typing import TypedDict
from typing import List


class AgentState(TypedDict):

    query: str
    retrieved_docs: List[str]
    dependencies: List[str]
    code_context: List[str]
    summary: str
    response: str