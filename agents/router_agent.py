def router_agent(query):

    query = query.lower()

    if "dependency" in query:
        return "dependency"

    elif "code" in query:
        return "code"

    return "retrieval"