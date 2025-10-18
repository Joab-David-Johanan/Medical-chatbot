from flask import Flask, render_template,jsonify,request
from src.helper import download_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

load_dotenv()

PINECONE_API_KEY=os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

embedding_model=download_embeddings()

index_name= "medical-chatbot"
# Embed each chunk and upsert the embeddings into your Pinecone index.
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embedding_model
)

retriever=docsearch.as_retriever(search_type="similarity",search_kwargs={"k":3})

ChatModel=ChatOpenAI(model="gpt-4o")
prompt=ChatPromptTemplate.from_messages(
    [
        ("system",system_prompt),
        ("human","{input}"),
    ]
)

question_answer_chain=create_stuff_documents_chain(ChatModel,prompt)
rag_chain=create_retrieval_chain(retriever,question_answer_chain)


app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=["GET","POST"])
def chat():
    msg = request.form["msg"]
    input=msg
    print(input)
    response=rag_chain.invoke({"input":msg})
    print("Response :", response["answer"])
    return str(response["answer"])

if __name__=='__main__':
    app.run(host="0.0.0.0",port=8080,debug=True)
