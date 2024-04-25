## End-to-end LLM AI app using Streamlit and Langchain.
![alt text](https://github.com/sharath7879/streamlit-ask-thedoc-app/blob/main/AsktheDocApp.png)
To create this ask the doc app, using Streamlit and Langchain, need below pre-requisites and libraries. This repo has all the necessary files to create the end-to-end app, including the DockerFile to build the Docker container.

First, we need the LLM model, in this case, I am using, the llama2 model, but you can replace it with any model of your choice. 
For the Llam2 model I am using here, you can download it from, huggingface, https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/tree/main, and copy this model to folder, 'models'. You can use any model and change the name of the model in the 'app.py' script.

The libraries used to develop this app are listed in the requirements.txt file:
         langchain,
         langchain_community,
         transformers,
         streamlit,
         chromadb,
         watchdog,
         sentence-transformers
