from tools.groq_tool import query_groq


def summarizer_agent(context):

    short_context = context[:800]

    prompt = f"""
    Summarize the following engineering context.

    {short_context}
    """

    return query_groq(prompt)