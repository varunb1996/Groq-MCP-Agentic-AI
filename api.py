from fastapi import FastAPI
from workflows.langgraph_workflow import graph

app = FastAPI()


@app.get("/query")
async def query(q: str):

    result = graph.invoke({
        "query": q
    })

    return result