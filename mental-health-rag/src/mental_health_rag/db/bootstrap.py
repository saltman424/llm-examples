import os
from pathlib import Path
from PyPDF2 import PdfReader
from .client import collection

data_dir = Path(__file__).parent.parent.parent.parent / 'data'

def extract_text_from_pdf(pdf_path: str) -> list[str]:
  """Extract text content from a PDF file."""
  try:
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
      text += page.extract_text() + "\n"
    return text.strip()
  except Exception as e:
    print(f"Error reading {pdf_path}: {e}")
    return None

def bootstrap():
  """
  Iterate through all PDF files in the 'data' directory and add them to ChromaDB
  """
  pdf_files = list(data_dir.glob("*.pdf"))
  
  if not pdf_files:
    print(f"No PDF files found in {data_dir}")
    return
  
  print(f"Found {len(pdf_files)} PDF files")
  
  # Process each PDF
  documents = []
  metadatas = []
  ids = []
  
  for idx, pdf_path in enumerate(pdf_files):
    print(f"Processing {idx + 1}/{len(pdf_files)}: {pdf_path.name}")
    
    # Extract text from PDF
    text = extract_text_from_pdf(pdf_path)
    
    if text:
      documents.append(text)
      metadatas.append({
        "filename": pdf_path.name,
        "path": str(pdf_path.absolute()),
        "file_size": os.path.getsize(pdf_path)
      })
      ids.append(pdf_path.name)
    else:
      print(f"Skipping {pdf_path.name} - no text extracted")
  
  # Add documents to collection
  if documents:
    collection.add(
      documents=documents,
      metadatas=metadatas,
      ids=ids
    )
    print(f"\nSuccessfully added {len(documents)} PDFs to the collection")
  else:
    print("No documents were added to the collection")
  
  return collection