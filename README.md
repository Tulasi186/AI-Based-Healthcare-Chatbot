# AI-Based-Healthcare-Chatbot

# HealthBuddy AI Assistant


## Overview

HealthBuddy AI Assistant is a Streamlit-based web application that leverages Google's Gemini AI model to provide general health information, wellness advice, and assistance with understanding medical concepts. With a user-friendly, colorful interface, HealthBuddy makes accessing health information intuitive and engaging.

## Features

- **AI-Powered Health Information**: Utilizes Google's Gemini 1.5 Pro model to provide evidence-based health information
- **Interactive Topic Exploration**: Quick access buttons for common health topics 
- **Conversational Interface**: Natural dialogue experience for health-related questions
- **Daily Health Tips**: Random wellness tips that refresh with each session
- **Responsive Design**: Clean, colorful UI with visual feedback and professional styling
- **Clear Health Disclaimers**: Transparent communication about the app's limitations

## Installation

### Prerequisites
- Python 
- Streamlit
- Google Generative AI Python SDK
- A Gemini API key

### Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/healthbuddy-ai.git
   cd healthbuddy-ai
   ```

2. Create a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root directory with your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

5. Run the application:
   ```
   streamlit run app.py
   ```

## Usage

1. **Topic Exploration**: Click on any of the colored topic buttons to get information about specific health areas.
2. **Ask Questions**: Use the chat input at the bottom to ask health-related questions.
3. **View Responses**: Read the AI-generated responses in the chat area.
4. **Clear Conversation**: Reset the conversation using the "Clear Conversation" button.

## Screenshots

![image](https://github.com/user-attachments/assets/9e0776de-ef6c-4e43-9a7f-1a668b5f2303)


## Important Disclaimers

- This application provides general health information and is **not a substitute for professional medical advice**.
- Always consult qualified healthcare providers for specific medical concerns.
- In case of emergency, call your local emergency services immediately.
- Information provided is for educational purposes only.
- Conversations are not stored permanently and are used only to provide contextual responses.

## Technical Details

### Key Components

- **Streamlit**: Powers the web interface and interactive elements
- **Google Generative AI (Gemini)**: Provides the AI capabilities for health information
- **Custom CSS**: Creates the colorful, professional look and feel
- **System Prompting**: Specialized healthcare guidance system for the AI model

### Code Structure

- **App Initialization**: Sets up environment variables and configures the Gemini API
- **UI Definition**: Custom CSS and Streamlit components for the interface
- **Model Initialization**: Healthcare-specific system prompt for the Gemini model
- **Conversation Handling**: Logic for processing user input and generating responses
- **Health Features**: Topic suggestions, health tips, and disclaimers

## Customization

You can customize the application by:

1. Modifying the CSS in the `st.markdown()` section at the beginning of the script
2. Adding or changing health topics in the `topic_map` dictionary
3. Updating the health tips in the `health_tips` list
4. Adjusting the system prompt in the `initialize_chat_model()` function
5. Changing the Gemini model parameters in the `generation_config` section

## Requirements

```
streamlit>=1.31.0
google-generativeai>=0.3.0
python-dotenv>=1.0.0
```



## Acknowledgements

- Google Generative AI for the Gemini model
- Streamlit for the web application framework

---

Created with ❤️ for better health information access.
