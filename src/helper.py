from langchain.document_loaders import PyPDFLoader
from typing import List
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings


def extract_text_from_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    return documents


def clean_metadata(docs:List[Document])->List[Document]:
    """
    Given a list of Document objects, return a new list of Document objects containing
    only 'source' in metadata and the original page_content
    :param docs: Original list of Documents with a lot of unwanted metadata information
    :return: Cleaned list of Documents with only necessary metadata and the original page_content
    """
    cleaned_doc: List[Document]=[]
    for doc in docs:
        src=doc.metadata.get("source")
        cleaned_doc.append(
            Document(
                page_content=doc.page_content,
                metadata={"source":src}
            )
        )
    return cleaned_doc


def document_into_chunks(cleaned_documents):
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20,
    )
    texts=text_splitter.split_documents(cleaned_documents)
    return texts


def download_embeddings():
    """
    Download and return the HuggingFace Embedding model
    :return: HuggingFace embedding model
    """
    model='sentence-transformers/all-MiniLM-L6-v2'
    embeddings=HuggingFaceEmbeddings(
        model_name=model
    )
    return embeddings
