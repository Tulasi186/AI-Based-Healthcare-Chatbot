import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure API keys
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set page configuration with a custom theme
st.set_page_config(
    page_title="HealthBuddy AI Assistant",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary: #3498db;
        --secondary: #2ecc71;
        --accent: #9b59b6;
        --background: #f0f8ff;
        --text: #2c3e50;
        --light-accent: #e3f2fd;
    }
    
    /* Overall page styling */
    .stApp {
        background-color: var(--background);
        color: var(--text);
    }
    
    /* Header styling */
    .main-header {
        color: var(--primary);
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
        padding: 1.5rem 0 0.5rem;
        text-align: center;
        border-bottom: 2px solid var(--primary);
        margin-bottom: 1.5rem;
    }
    
    /* Cards styling */
    .stCard {
        border-radius: 15px;
        border-left: 5px solid var(--primary);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin-bottom: 1rem;
        background-color: white;
    }
    
    /* Topic buttons */
    .stButton>button {
        border-radius: 20px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: 500;
        transition: all 0.3s ease;
        width: 100%;
        margin-bottom: 0.5rem;
        text-align: center;
    }
    
    /* Different colored buttons */
    .primary-btn > button {
        background-color: #3498db;
        color: white;
    }
    .secondary-btn > button {
        background-color: #2ecc71;
        color: white;
    }
    .accent-btn > button {
        background-color: #9b59b6;
        color: white;
    }
    .warning-btn > button {
        background-color: #e74c3c;
        color: white;
    }
    
    /* Button hover effects */
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* Chat message styling */
    .user-message {
        background-color: #e3f2fd;
        border-radius: 15px;
        padding: 0.8rem;
        margin-bottom: 0.8rem;
        border-left: 5px solid #3498db;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .assistant-message {
        background-color: #f1f8e9;
        border-radius: 15px;
        padding: 0.8rem;
        margin-bottom: 0.8rem;
        border-left: 5px solid #2ecc71;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* Features section */
    .features-section {
        background-color: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        border-top: 4px solid #9b59b6;
    }
    
    /* Disclaimer section */
    .disclaimer {
        background-color: #fff8e1;
        border-left: 4px solid #ffb74d;
        padding: 1rem;
        border-radius: 5px;
        font-size: 0.9rem;
        margin: 1.5rem 0;
    }
    
    /* Health tip box */
    .health-tip {
        background-color: #e8f5e9;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        border-left: 4px solid #4caf50;
        font-style: italic;
    }
    
    /* Chat input */
    .stTextInput>div>div>input {
        border-radius: 20px;
        border: 2px solid #e0e0e0;
        padding: 0.5rem 1rem;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    }
    
    .stTextInput>div>div>input:focus {
        border: 2px solid var(--primary);
        box-shadow: 0 0 0 2px rgba(52, 152, 219, 0.2);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 1rem;
        font-size: 0.8rem;
        color: #78909c;
        border-top: 1px solid #e0e0e0;
        margin-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# App header with icon and title
st.markdown('<div class="main-header"><h1>🩺 HealthBuddy AI Assistant</h1></div>', unsafe_allow_html=True)

# App description with styled box
st.markdown("""
<div class="stCard">
    <h3>Your Personal Health Companion</h3>
    <p>This AI-powered healthcare assistant can help answer general medical questions, 
    provide wellness advice, and assist with understanding medical concepts.</p>
    <div class="disclaimer">
        <strong>Important:</strong> This is not a substitute for professional medical advice, diagnosis, or treatment.
        Always consult with qualified healthcare providers for medical concerns.
    </div>
</div>
""", unsafe_allow_html=True)

# Daily health tip (random tip that changes on refresh)
import random
health_tips = [
    "Staying hydrated improves energy levels and brain function. Aim for 8 glasses of water daily.",
    "Just 30 minutes of walking each day can significantly improve your cardiovascular health.",
    "A diet rich in colorful fruits and vegetables provides essential antioxidants and nutrients.",
    "Regular sleep patterns help regulate your body's internal clock and improve sleep quality.",
    "Taking short breaks to stand and stretch during long periods of sitting improves circulation.",
    "Mindful breathing for just 5 minutes daily can help reduce stress and improve focus."
]

st.markdown(f"""
<div class="health-tip">
    <strong>💡 Daily Health Tip:</strong> {random.choice(health_tips)}
</div>
""", unsafe_allow_html=True)

# Features section with colored styling
st.markdown('<div class="features-section">', unsafe_allow_html=True)
st.markdown("### 🔍 Explore Health Topics")
st.markdown("Click on any topic to get started with your health journey:")

# Topic buttons with different colors using custom HTML/CSS
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="primary-btn">', unsafe_allow_html=True)
    button1 = st.button("💪 Fitness & Exercise")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="secondary-btn">', unsafe_allow_html=True)
    button2 = st.button("🥗 Nutrition & Diet")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="accent-btn">', unsafe_allow_html=True)
    button3 = st.button("😌 Mental Wellness")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="primary-btn">', unsafe_allow_html=True)
    button4 = st.button("😴 Sleep Health")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="secondary-btn">', unsafe_allow_html=True)
    button5 = st.button("🩺 Common Symptoms")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="accent-btn">', unsafe_allow_html=True)
    button6 = st.button("🧠 Preventive Care")
    st.markdown('</div>', unsafe_allow_html=True)

# Clear chat button in warning color
st.markdown('<div class="warning-btn" style="margin-top: 1rem;">', unsafe_allow_html=True)
clear_button = st.button("🗑️ Clear Conversation")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close features section

# Guidelines and disclaimers
with st.expander("📋 Important Healthcare Disclaimers"):
    st.markdown("""
    - This chatbot provides general health information and is not a substitute for professional medical advice.
    - Do not disregard professional medical advice or delay seeking it because of information provided here.
    - In case of emergency, call your local emergency number immediately.
    - The information provided is for educational purposes only.
    - Your conversation is not stored permanently and is used only to provide contextual responses.
    - Always consult qualified healthcare professionals for specific medical concerns.
    """)

# Initialize chat model
def initialize_chat_model():
    # Healthcare-specific system prompt
    system_prompt = """
    You are HealthBuddy, a friendly and knowledgeable healthcare assistant designed to provide general health information and guidance.
    
    Guidelines:
    - Provide accurate and evidence-based health information
    - Use a warm, supportive tone while maintaining professionalism
    - Include specific, actionable advice when appropriate
    - Explain medical concepts in simple, clear language
    - Acknowledge the emotional aspects of health concerns
    - Always encourage consulting healthcare professionals for specific concerns
    - Provide balanced information about treatment options when relevant
    - Focus on preventive care and healthy lifestyle choices
    - Include brief explanations of why certain recommendations are beneficial
    - Be respectful of diverse health perspectives and cultural practices
    
    Important: Always include appropriate disclaimers when discussing specific health concerns.
    """
    
    # Initialize Gemini model with system prompt
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config={
            "temperature": 0.7,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 800,
        }
    )
    
    # Create a chat session
    chat = model.start_chat(history=[])
    
    # Add system prompt as first message
    try:
        response = chat.send_message(system_prompt)
        return chat
    except Exception as e:
        st.error(f"Failed to initialize chat model: {str(e)}")
        return None

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "model", "content": "👋 Hello! I'm HealthBuddy, your AI health assistant. How can I help with your health and wellness questions today?"}
    ]

# Initialize chat in session state if it doesn't exist
if "chat" not in st.session_state:
    try:
        st.session_state.chat = initialize_chat_model()
    except Exception as e:
        st.error(f"Failed to initialize chat model: {str(e)}")
        st.session_state.chat = None

# Function to get AI response
def get_ai_response(prompt):
    try:
        # Send user prompt to Gemini model
        response = st.session_state.chat.send_message(prompt)
        return response.text
    except Exception as e:
        return f"I apologize, but I encountered an error: {str(e)}. Please try again later."

# Process button clicks for suggested topics
topic_map = {
    button1: "Tell me about effective fitness and exercise routines for overall health",
    button2: "Provide information about balanced nutrition and healthy eating habits",
    button3: "Share strategies for maintaining good mental health and reducing stress",
    button4: "Explain the importance of sleep and tips for better sleep quality",
    button5: "Describe how to understand common symptoms and when to see a doctor",
    button6: "What are important preventive healthcare measures everyone should know about?"
}

for button, prompt in topic_map.items():
    if button:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.spinner("🤔 Thinking..."):
            response = get_ai_response(prompt)
        st.session_state.messages.append({"role": "model", "content": response})
        st.experimental_rerun()

# Process clear conversation button
if clear_button:
    st.session_state.messages = [
        {"role": "model", "content": "👋 Hello! I'm HealthBuddy, your AI health assistant. How can I help with your health and wellness questions today?"}
    ]
    # Re-initialize chat session
    st.session_state.chat = initialize_chat_model()
    st.experimental_rerun()

# Chat interface with styled messages
st.markdown("### 💬 Your Health Conversation")

# Display chat messages
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f'<div class="user-message"><strong>You:</strong> {message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="assistant-message"><strong>🩺 HealthBuddy:</strong> {message["content"]}</div>', unsafe_allow_html=True)

# Chat input with custom styling
st.markdown("<br>", unsafe_allow_html=True)
user_input = st.chat_input("Ask me about your health concerns...")

# Process user input
if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message (this will be shown instantly)
    st.markdown(f'<div class="user-message"><strong>You:</strong> {user_input}</div>', unsafe_allow_html=True)
    
    # Get and display assistant response with a spinner
    with st.spinner("🤔 Thinking..."):
        response = get_ai_response(user_input)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "model", "content": response})
    
    # Display assistant response
    st.markdown(f'<div class="assistant-message"><strong>🩺 HealthBuddy:</strong> {response}</div>', unsafe_allow_html=True)
    
    # Force a rerun to update the UI
    st.experimental_rerun()

# Footer with disclaimer
st.markdown("""
<div class="footer">
    <p>HealthBuddy AI Assistant © 2025 | For informational purposes only</p>
    <p>Not a substitute for professional medical advice, diagnosis, or treatment</p>
</div>
""", unsafe_allow_html=True)