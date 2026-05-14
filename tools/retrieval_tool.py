import chromadb

from utils.config import CHROMA_PATH
from utils.config import COLLECTION_NAME

client = chromadb.PersistentClient(
    path=CHROMA_PATH
)

collection = client.get_or_create_collection(
    COLLECTION_NAME
)

def retrieve_context(query):

    results = collection.query(
        query_texts=[query],
        n_results=1
    )

    documents = results["documents"][0]

    shortened_docs = []

    for doc in documents:
        shortened_docs.append(doc[:800])

    return "\n".join(documents)