import json, numpy as np, faiss, sys
from client import client, CHAT_DEPLOYMENT, EMBED_DEPLOYMENT

docs = json.load(open("chunks.json"))
index = faiss.read_index("kb.faiss")

SYSTEM = """You are a policy assistant. Answer ONLY using the provided context.
Rules:
- If the context does not contain the answer, say exactly: "I don't have that in the provided documents."
- Never use outside knowledge. Never guess.
- Cite the source id in brackets after each claim, e.g. [policy.pdf#3].
- Be concise.
- When you refuse, do not cite any sources."""

def retrieve(question, k=4):
    q = client.embeddings.create(model=EMBED_DEPLOYMENT, input=[question]).data[0].embedding
    qv = np.array([q], dtype="float32"); faiss.normalize_L2(qv)
    scores, idxs = index.search(qv, k)
    return [docs[i] for i in idxs[0]]

def ask(question):
    hits = retrieve(question)
    context = "\n\n".join(f"[{h['id']}]\n{h['text']}" for h in hits)
    resp = client.chat.completions.create(
        model=CHAT_DEPLOYMENT,
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"},
        ],
    )
    return resp.choices[0].message.content

if __name__ == "__main__":
    print(ask(" ".join(sys.argv[1:])))