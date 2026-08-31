import os, glob, json
from pypdf import PdfReader

def load_text(path):
    if path.lower().endswith(".pdf"):
        return "\n".join(page.extract_text() or "" for page in PdfReader(path).pages)
    with open(path, encoding="utf-8") as f:
        return f.read()

def chunk(text, size=800, overlap=150):
    words = text.split()
    step = size - overlap
    return [" ".join(words[i:i+size]) for i in range(0, len(words), step) if words[i:i+size]]

docs = []
for path in glob.glob("knowledge/*"):
    for i, c in enumerate(chunk(load_text(path))):
        docs.append({"id": f"{os.path.basename(path)}#{i}", "source": os.path.basename(path), "text": c})

json.dump(docs, open("chunks.json", "w"))
print(f"{len(docs)} chunks from {len(set(d['source'] for d in docs))} docs")