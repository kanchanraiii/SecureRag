import faiss
import numpy as np
import json
from sentence_transformers import SentenceTransformer


model = SentenceTransformer('all-MiniLM-L6-v2')


docs = []
with open("Data/healthcare_dataset.jsonl", "r") as f:
    for line in f:
        obj = json.loads(line)
        docs.append(obj["text"])   


embeddings = model.encode(docs)
embeddings = np.array(embeddings).astype("float32")


d = embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(embeddings)

print(f"Indexed {len(docs)} documents")


def search(query, k=3):
    q_vec = model.encode([query]).astype("float32")
    distances, indices = index.search(q_vec, k)
    results = [docs[i] for i in indices[0]]
    return results


query = "What medicine is used for infection?"
retrieved = search(query, k=2)

print("Query:", query)
print("Retrieved docs:")
for doc in retrieved:
    print("-", doc)
