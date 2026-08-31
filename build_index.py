import json, numpy as np, faiss
from client import client, EMBED_DEPLOYMENT

docs = json.load(open("chunks.json"))
texts = [d["text"] for d in docs]

# batch embed
resp = client.embeddings.create(model=EMBED_DEPLOYMENT, input=texts)
vecs = np.array([d.embedding for d in resp.data], dtype="float32")
faiss.normalize_L2(vecs)

index = faiss.IndexFlatIP(vecs.shape[1])   # 1536 dims for 3-small
index.add(vecs)
faiss.write_index(index, "kb.faiss")
print(f"indexed {index.ntotal} vectors")