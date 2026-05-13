from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb
import json
import mlflow

from utils.config import EMBEDDING_MODEL
from utils.config import CHROMA_PATH
from utils.config import COLLECTION_NAME

model = SentenceTransformer(
    EMBEDDING_MODEL
)

client = chromadb.PersistentClient(
    path=CHROMA_PATH
)

collection = client.get_or_create_collection(
    COLLECTION_NAME
)

with open("data/documents.json", "r", encoding="utf-8") as f:
    docs = json.load(f)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=50
)

mlflow.set_experiment(
    "Embedding Pipeline"
)

with mlflow.start_run():

    mlflow.log_param(
        "embedding_model",
        EMBEDDING_MODEL
    )

    mlflow.log_param(
        "chunk_size",
        400
    )

    mlflow.log_param(
        "chunk_overlap",
        50
    )

    doc_id = 0
    total_chunks = 0

    for doc in docs:

        chunks = text_splitter.split_text(
            doc["content"]
        )

        total_chunks += len(chunks)

        for chunk in chunks:

            embedding = model.encode(
                chunk
            ).tolist()

            collection.add(
                ids=[str(doc_id)],
                documents=[chunk],
                embeddings=[embedding]
            )

            doc_id += 1

    mlflow.log_metric(
        "documents_processed",
        len(docs)
    )

    mlflow.log_metric(
        "chunks_created",
        total_chunks
    )

print("Embeddings stored successfully")