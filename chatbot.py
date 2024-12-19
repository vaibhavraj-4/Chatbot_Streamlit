import streamlit as st
import google.generativeai as genai


genai.configure(api_key="GEMINI_KEY")  # Replace with your actual API key


if "history" not in st.session_state:
    st.session_state["history"] = []


predefined_answers = {
    "Who is Sonu": "Sonu, Bihar ka rehne wala hai or ye Chandiwala institute of information technology se BCA kar raha hai or uski girl dost Radhika hai.",
    "What is the age of Sonu": "Bhai me 20 saal ka hu.",
    "Explain the Love life.": "Bhai aaj tk mera love life nahi bn paya."
    
}


def get_response(user_input):

    if user_input in predefined_answers:
        return predefined_answers[user_input]
    else:
        prompt = f"""
        You are a knowledgeable assistant designed to help users with their study notes and academic concepts.
        Provide clear, concise, and informative answers relevant to study material or general educational topics.

        Question from user:
        {user_input}

        Your response should be:
        - Informative and straightforward.
        - Relevant to typical study notes or academic subjects.
        - Concise, with examples or key points if applicable.
        """
        
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text


st.title("Note Provider Chatbot")
st.write("Ask any question, and the chatbot will provide relevant information related to your notes!")


user_input = st.text_input("Ask a question:")

if user_input:
    bot_response = get_response(user_input)
    st.session_state["history"].append({"user": user_input, "bot": bot_response})

for chat in st.session_state["history"]:
    st.write(f"**You:** {chat['user']}")
    st.write(f"**Bot:** {chat['bot']}")
