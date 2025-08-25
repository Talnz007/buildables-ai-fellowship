"""
Streamlit Chatbot with OpenAI Integration
Week 2 - Conversational LLMs and Prompt Fundamentals
"""

import streamlit as st
import openai
from typing import List, Dict
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="🤖",
    layout="wide"
)

class ChatBot:
    def __init__(self):
        self.client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
        
    def get_response(self, messages: List[Dict], model: str = "gpt-3.5-turbo") -> str:
        """Get response from OpenAI API"""
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"

def initialize_session_state():
    """Initialize session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "system_prompt" not in st.session_state:
        st.session_state.system_prompt = "You are a helpful AI assistant."

def get_system_prompts():
    """Predefined system prompts for different personas"""
    return {
        "General Assistant": "You are a helpful, friendly, and knowledgeable AI assistant. Provide clear and accurate information.",
        "Code Tutor": "You are an expert programming tutor. Explain coding concepts clearly with examples. Ask follow-up questions to ensure understanding.",
        "Creative Writer": "You are a creative writing assistant. Help with brainstorming, storytelling, and creative projects. Be imaginative and inspiring.",
        "Data Analyst": "You are a data analysis expert. Help interpret data, suggest analysis methods, and explain statistical concepts clearly.",
        "Business Consultant": "You are a professional business consultant. Provide strategic advice, market insights, and practical business solutions.",
    }

def export_chat_history():
    """Export chat history as JSON"""
    if st.session_state.chat_history:
        export_data = {
            "export_date": datetime.now().isoformat(),
            "system_prompt": st.session_state.system_prompt,
            "conversation": st.session_state.chat_history
        }
        return json.dumps(export_data, indent=2)
    return None

def main():
    st.title("🤖 AI Chat Assistant")
    st.subtitle("Week 2: Exploring Conversational LLMs and System Prompts")
    
    # Initialize
    initialize_session_state()
    chatbot = ChatBot()
    
    # Sidebar configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # System prompt selection
        system_prompts = get_system_prompts()
        selected_persona = st.selectbox(
            "Choose AI Persona:",
            list(system_prompts.keys()),
            key="persona_select"
        )
        
        # Update system prompt when persona changes
        if st.session_state.system_prompt != system_prompts[selected_persona]:
            st.session_state.system_prompt = system_prompts[selected_persona]
            # Clear messages when changing system prompt
            st.session_state.messages = []
            st.session_state.chat_history = []
            st.rerun()
        
        # Display current system prompt
        with st.expander("View System Prompt"):
            st.text_area(
                "Current System Prompt:",
                value=st.session_state.system_prompt,
                height=100,
                disabled=True
            )
        
        # Chat controls
        st.header("💬 Chat Controls")
        
        if st.button("Clear Conversation", type="secondary"):
            st.session_state.messages = []
            st.session_state.chat_history = []
            st.rerun()
        
        # Export functionality
        if st.session_state.chat_history:
            if st.button("Export Chat History"):
                export_data = export_chat_history()
                if export_data:
                    st.download_button(
                        "Download JSON",
                        export_data,
                        f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                        "application/json"
                    )
        
        # Statistics
        st.header("📊 Statistics")
        st.metric("Messages Sent", len([m for m in st.session_state.chat_history if m["role"] == "user"]))
        st.metric("AI Responses", len([m for m in st.session_state.chat_history if m["role"] == "assistant"]))
    
    # Main chat interface
    st.header("💬 Conversation")
    
    # Display chat history
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.write(message["content"])
                if message["role"] == "assistant":
                    st.caption(f"Generated at {message.get('timestamp', 'Unknown time')}")
    
    # Chat input
    if user_input := st.chat_input("Type your message here..."):
        # Add user message to history
        user_message = {
            "role": "user",
            "content": user_input,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }
        st.session_state.chat_history.append(user_message)
        
        # Display user message
        with st.chat_message("user"):
            st.write(user_input)
        
        # Prepare messages for API call
        api_messages = [
            {"role": "system", "content": st.session_state.system_prompt}
        ]
        
        # Add conversation history (last 10 messages to manage token limit)
        recent_messages = st.session_state.chat_history[-10:]
        for msg in recent_messages:
            api_messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })
        
        # Get AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = chatbot.get_response(api_messages)
                st.write(response)
                st.caption(f"Generated at {datetime.now().strftime('%H:%M:%S')}")
        
        # Add assistant response to history
        assistant_message = {
            "role": "assistant",
            "content": response,
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }
        st.session_state.chat_history.append(assistant_message)
        
        # Rerun to update the interface
        st.rerun()
    
    # Instructions and tips
    with st.expander("💡 Usage Tips"):
        st.markdown("""
        **How to get the best responses:**
        1. **Be specific** - Clear questions get better answers
        2. **Provide context** - Help the AI understand your situation
        3. **Try different personas** - Each has different strengths
        4. **Iterate** - Refine your questions based on responses
        
        **Experiment with system prompts:**
        - Notice how different personas respond differently to the same question
        - Try asking the same question with different personas
        - Observe changes in tone, detail level, and approach
        """)

if __name__ == "__main__":
    main()
