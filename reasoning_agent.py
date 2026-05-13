from tools.groq_tool import query_groq


def reasoning_agent(query, context):

    prompt = f"""
    You are an engineering AI assistant.

    Context:
    {context}

    Question:
    {query}
    """

    return query_groq(prompt)