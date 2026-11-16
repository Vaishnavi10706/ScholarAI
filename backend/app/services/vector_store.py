import chromadb
from pathlib import Path
from uuid import uuid4

BASE_DIR = Path(__file__).resolve().parents[2]
CHROMA_PATH = BASE_DIR/"chroma_data"
client = chromadb.PersistentClient(path=str(CHROMA_PATH))
collection = client.get_or_create_collection(name="research_papers",metadata={"hnsw:space":"cosine"})
def store_chunks(paper_id: str,filename: str, chunks: list[str]) -> int:
    if not chunks:
        return 0
    ids = []
    documents = []
    metadatas = []
    for chunk in chunks:
        ids.append(str(uuid4))
        documents.append(chunks["text"])
        metadatas.append({
            "paper_id":paper_id,
            "filename":filename,
            "page_number": chunk["page_number"],
            "chunk_index": chunk["chunk_index"]
        })
    collection.add(ids=ids,documents=documents,metadatas=metadatas)
    return len(ids)