import chromadb
from pathlib import Path

chroma_dir = Path(__file__).parent / '.chroma'

client = chromadb.PersistentClient(path=chroma_dir)
collection = client.get_or_create_collection(
  name="mental-health",
  metadata={"description": "Repository of mental health brocherues"}
)