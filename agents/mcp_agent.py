from tools.groq_tool import query_groq


def mcp_agent(query, context):

    prompt = f"""
    You are an MCP-enabled engineering assistant.

    Context:
    {context}

    Query:
    {query}
    """

    return query_groq(prompt)