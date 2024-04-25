import streamlit as st
from langchain_community.llms import CTransformers
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

def generate_response(uploaded_file, query_text):
    # Load document if file is uploaded
    if uploaded_file is not None:
        documents = [uploaded_file.read().decode()]
        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        texts = text_splitter.create_documents(documents)
        # Select embeddings
        embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        # Create a vectorstore from documents
        db = Chroma.from_documents(texts, embeddings)        
        # Create retriever interface
        retriever = db.as_retriever()
        # Create llm for response
        llm=CTransformers(model='models/llama-2-7b-chat.Q8_0.gguf',
                  model_type='llama',
                  config={'max_new_tokens':1000,
                         'temperature':0.01,
                         'context_length': 1000})

        # Create QA chain
        qa = RetrievalQA.from_chain_type(llm, chain_type='stuff', retriever=retriever)
        return qa.invoke(query_text)

# Page title
st.set_page_config(page_title='🦜🔗 Ask the Doc App')
st.title('🦜🔗 Ask the Doc App')

# File upload
uploaded_file = st.file_uploader('Upload an article', type='txt')
# Query text
query_text = st.text_input('Enter your question:', placeholder = 'Please provide a short summary.', disabled=not uploaded_file)

# Form input and query
result = []
with st.form('myform', clear_on_submit=True):
    submitted = st.form_submit_button('Submit')
    if submitted:
        with st.spinner('Calculating...'):
            response = generate_response(uploaded_file, query_text)
            result.append(response)
            

if len(result):
    st.info(response)