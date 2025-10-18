import os
from dotenv import load_dotenv
from src.helper import extract_text_from_pdf,clean_metadata,document_into_chunks,download_embeddings
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore

load_dotenv()

PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

extracted_data=extract_text_from_pdf(r"C:\Coding\Projects\Medical-chatbot\data\Medical_book.pdf")
cleaned_document=clean_metadata(extracted_data)
chunks=document_into_chunks(cleaned_document)

embedding_model=download_embeddings()

pc=Pinecone(api_key=PINECONE_API_KEY)

index_name="medical-chatbot"
if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384, # Dimensionality of the embedding
        metric="cosine", # Cosine Similarity metric
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index=pc.Index(index_name)

docsearch=PineconeVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    index_name=index_name
)