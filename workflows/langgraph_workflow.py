from langgraph.graph import StateGraph

from workflows.state import AgentState

from agents.retrieval_agent import retrieval_agent
from agents.dependency_agent import dependency_agent
from agents.code_agent import code_agent
from agents.summarizer_agent import summarizer_agent
from agents.reasoning_agent import reasoning_agent

workflow = StateGraph(AgentState)



def retrieval_node(state):

    docs = retrieval_agent(
        state["query"]
    )

    return {
        "retrieved_docs": docs
    }



def dependency_node(state):

    dependencies = dependency_agent(
        "data/repos"
    )

    return {
        "dependencies": dependencies
    }



def code_node(state):

    code_context = code_agent(
        "data/repos"
    )

    return {
        "code_context": code_context
    }



def summary_node(state):

    combined_context = f"""
    Documents:
    {state['retrieved_docs']}

    Dependencies:
    {state['dependencies']}

    Code:
    {state['code_context']}
    """

    summary = summarizer_agent(
        combined_context
    )

    return {
        "summary": summary
    }



def reasoning_node(state):

    response = reasoning_agent(
        state["query"],
        state["summary"]
    )

    return {
        "response": response
    }


workflow.add_node(
    "retrieval",
    retrieval_node
)

workflow.add_node(
    "dependency",
    dependency_node
)

workflow.add_node(
    "code",
    code_node
)

workflow.add_node(
    "summary",
    summary_node
)

workflow.add_node(
    "reasoning",
    reasoning_node
)

workflow.set_entry_point(
    "retrieval"
)

workflow.add_edge(
    "retrieval",
    "dependency"
)

workflow.add_edge(
    "dependency",
    "code"
)

workflow.add_edge(
    "code",
    "summary"
)

workflow.add_edge(
    "summary",
    "reasoning"
)

workflow.set_finish_point(
    "reasoning"
)

graph = workflow.compile()