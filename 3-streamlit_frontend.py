import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

# st.session_state -> dict -> 
CONFIG = {'configurable': {'thread_id': 'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# loading the conversation history-->displaying the previous messages history in the chat interface . 
for message in st.session_state['message_history']:  #load all the previous messages from the message_history list in session_state and display them in the chat interface. Each message is displayed using st.chat_message, which creates a new message bubble for each message.
    with st.chat_message(message['role']):
        st.text(message['content'])

#{'role': 'user', 'content': 'Hi'}
#{'role': 'assistant', 'content': 'Hi=Hello'}

user_input = st.chat_input('Type here')

if user_input:

    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config=CONFIG)
    
    ai_message = response['messages'][-1].content  #last message is ai_message.

    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)



#with st.chat_message('assistant'):  -->message from the assistant
# with st.chat_message('user'): --> message from the user
# st.chat_input() --> input box for the user to type in


# if user_input:
#       with st.chat_message('user'):
#             st.text(user_input)       -->these means whatever the user types in the input box will be displayed as a message from the user on the screen. The st.chat_message('user') creates a new message bubble for the user, and st.text(user_input) displays the content of the user's message inside that bubble.


# session_state-->it is a dictionary-like object provided by Streamlit that allows you to store and manage state across different interactions with the app. In this code, we are using session_state to keep track of the message history of the chat. Whenever a user sends a message, it is added to the message_history list in session_state, and whenever the assistant responds, that response is also added to the message_history. This way, we can maintain a record of the entire conversation history and display it in the chat interface.