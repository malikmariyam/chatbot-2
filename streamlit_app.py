 import streamlit as st
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyC86IqnS0vAzkijFfnDW2yOEtpWNiea1Vc")

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Define Gym-specific responses
def gym_faq(user_input):
    faq_responses = {
        "membership": "We offer different membership plans: Monthly, Quarterly, and Yearly. Visit our Membership page for detailed pricing.",
        "trainer": "Our certified trainers specialize in various fitness areas including strength training, cardio, and yoga.",
        "hours": "We are open every day from 6 AM to 10 PM.",
        "classes": "We offer classes such as Yoga, Zumba, and Crossfit. You can check the schedule on our Classes page.",
        "equipment": "We have a wide range of equipment, including cardio machines, free weights, and resistance training tools."
    }
    return faq_responses.get(user_input.lower(), None)

# Streamlit UI
st.title("GymBot - Your Virtual Gym Assistant")

# Instructions
st.markdown("""
    **Welcome to our Gym!**  
    How can I assist you today? Ask me about:
    - Membership plans
    - Trainers and their specialties
    - Gym hours
    - Available classes
    - Gym equipment
""")

# User input
user_input = st.text_input("You:", "")

# Display the chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if user_input:
    # Append user input to the chat history
    st.session_state.chat_history.append(f"You: {user_input}")

    # Check for gym-related FAQs
    response = gym_faq(user_input)
    
    if response:  # If we found a match in FAQs
        st.session_state.chat_history.append(f"GymBot: {response}")
    else:  # If no FAQ match, generate a dynamic response
        response = model.generate_content(user_input).text
        st.session_state.chat_history.append(f"GymBot: {response}")

# Show chat history
for message in st.session_state.chat_history:
    st.markdown(message)
