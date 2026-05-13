from tools.retrieval_tool import retrieve_context

query = input("Enter query: ")

results = retrieve_context(query)

print(results)