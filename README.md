# LangGraph AI Chatbot

A simple AI chatbot built using LangGraph, LangChain, Groq LLM, and Streamlit.
This project demonstrates how to build a conversational AI system where LangGraph manages the conversation workflow and memory, while a Large Language Model generates responses.
The chatbot provides a web-based chat interface and streams responses in real time.

---
# Live Demo

Demo: https://langgraphchatbot-8pmyndeomjhbygjtepqmvt.streamlit.app/

---
# What This Project Does

* Provides a simple chat interface using Streamlit
* Sends user messages to a LangGraph workflow
* Uses Groq's LLM (Llama model) to generate responses
* Streams responses in real time to the user
* Maintains conversation state using LangGraph memory

# Tech Stack

* Python
* Streamlit – Web interface
* LangGraph – Conversation workflow management
* LangChain – Message handling and LLM integration
* Groq API – Language model inference

---

# Project Structure
    ChatBot_using_langgraph
    │
    ├── langgraph_backend.py        # LangGraph workflow and chatbot logic
    ├── streamlit_frontend.py       # Basic Streamlit chat interface
    ├── streamlit_with_streaming.py # Streamlit UI with streaming responses
    ├── requirements.txt

---

# How It Works

* The user types a message in the Streamlit chat interface.
* The message is sent to the LangGraph chatbot workflow.
* The chatbot node sends the message to the Groq LLM.
* The LLM generates a response.
* The response is streamed back to the UI and displayed to the user in real time.

---

# Running the Project Locally
  * 1️⃣ Clone the repository
      git clone https://github.com/your-username/langgraph-chatbot.git
      cd langgraph-chatbot
  * 2️⃣ Install dependencies
      pip install -r requirements.txt
  * 3️⃣ Add your API key
  
---

Create a .env file in the root directory and add your Groq API key:

* GROQ_API_KEY=your_api_key_here
  4️⃣ Run the Streamlit app
  * streamlit run streamlit_with_streaming.py

After running the command, open the link shown in the terminal (usually):

http://localhost:8501
