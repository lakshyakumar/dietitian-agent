# streamlit_app.py
import streamlit as st
import requests

# Initialize session state for chat_id and conversation history
if "chat_id" not in st.session_state:
    st.session_state.chat_id = None
if "conversation" not in st.session_state:
    st.session_state.conversation = []
    
# Streamlit app title
st.title("Chat API Frontend")

# Input box for user message
user_message = st.text_input("Enter your message:", "")
# Button to send the message
if st.button("Send"):
    if user_message.strip():
        # Prepare the payload
        payload = {
            "query": user_message,
            "chat_id": st.session_state.chat_id
        }

        # Send the request to the /chat API
        try:
            response = requests.get("http://localhost:8000/chat", params=payload)
            response_data = response.json()

            # Update chat_id and conversation history
            st.session_state.chat_id = response_data.get("chat_id", st.session_state.chat_id)
            bot_reply = response_data.get("message", "No reply received.")
            st.session_state.conversation.append(("You", user_message))
            st.session_state.conversation.append(("Bot", bot_reply))
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a message before sending.")

# Display the conversation history
st.subheader("Conversation History")
st.markdown("---")  # Separator for clarity
for sender, message in reversed(st.session_state.conversation):  # Reverse the conversation
    st.write(f"**{sender}:** {message}")