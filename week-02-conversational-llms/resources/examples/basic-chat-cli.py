"""
Basic Command Line Chat Interface
Week 2 - Conversational LLMs and Prompt Fundamentals
"""

import openai
import os
from typing import List, Dict
import json
from datetime import datetime

class SimpleChatBot:
    def __init__(self, api_key: str):
        """Initialize the chatbot with OpenAI API key"""
        self.client = openai.OpenAI(api_key=api_key)
        self.conversation_history = []
        self.system_prompt = "You are a helpful AI assistant."
        
    def set_system_prompt(self, prompt: str):
        """Set or update the system prompt"""
        self.system_prompt = prompt
        print(f"✅ System prompt updated: {prompt[:50]}...")
    
    def get_response(self, user_input: str) -> str:
        """Get response from OpenAI API"""
        # Build messages list
        messages = [{"role": "system", "content": self.system_prompt}]
        
        # Add conversation history
        messages.extend(self.conversation_history)
        
        # Add current user input
        messages.append({"role": "user", "content": user_input})
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )
            
            ai_response = response.choices[0].message.content
            
            # Update conversation history
            self.conversation_history.append({"role": "user", "content": user_input})
            self.conversation_history.append({"role": "assistant", "content": ai_response})
            
            # Keep only last 10 exchanges to manage token limits
            if len(self.conversation_history) > 20:
                self.conversation_history = self.conversation_history[-20:]
            
            return ai_response
            
        except Exception as e:
            return f"❌ Error: {str(e)}"
    
    def save_conversation(self, filename: str = None):
        """Save conversation to JSON file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"conversation_{timestamp}.json"
        
        conversation_data = {
            "timestamp": datetime.now().isoformat(),
            "system_prompt": self.system_prompt,
            "conversation": self.conversation_history
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(conversation_data, f, indent=2)
            print(f"💾 Conversation saved to {filename}")
        except Exception as e:
            print(f"❌ Error saving conversation: {e}")
    
    def load_conversation(self, filename: str):
        """Load conversation from JSON file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            self.system_prompt = data.get("system_prompt", self.system_prompt)
            self.conversation_history = data.get("conversation", [])
            print(f"📂 Conversation loaded from {filename}")
            print(f"📝 System prompt: {self.system_prompt}")
            
        except Exception as e:
            print(f"❌ Error loading conversation: {e}")
    
    def show_history(self):
        """Display conversation history"""
        if not self.conversation_history:
            print("📭 No conversation history yet.")
            return
        
        print("\n" + "="*50)
        print("📜 CONVERSATION HISTORY")
        print("="*50)
        
        for i, message in enumerate(self.conversation_history, 1):
            role = message["role"]
            content = message["content"]
            
            if role == "user":
                print(f"\n👤 User ({i//2 + 1}):")
                print(f"   {content}")
            else:
                print(f"\n🤖 Assistant ({i//2}):")
                print(f"   {content}")
        
        print("\n" + "="*50)

def get_system_prompt_presets():
    """Return predefined system prompts"""
    return {
        "1": ("General Assistant", "You are a helpful, friendly, and knowledgeable AI assistant."),
        "2": ("Code Tutor", "You are an expert programming tutor. Explain coding concepts clearly with examples. Always ask if the student understands before moving on."),
        "3": ("Creative Writer", "You are a creative writing assistant. Help with brainstorming, storytelling, and creative projects. Be imaginative and inspiring."),
        "4": ("Technical Expert", "You are a technical expert. Provide detailed, accurate technical information with step-by-step explanations."),
        "5": ("Friendly Companion", "You are a warm, empathetic companion. Be supportive, encouraging, and conversational."),
    }

def display_help():
    """Display available commands"""
    print("\n" + "="*50)
    print("🤖 CHATBOT COMMANDS")
    print("="*50)
    print("💬 Just type your message to chat")
    print("📝 /system    - Change system prompt")
    print("📜 /history   - Show conversation history")  
    print("💾 /save      - Save conversation to file")
    print("📂 /load      - Load conversation from file")
    print("🧹 /clear     - Clear conversation history")
    print("❓ /help      - Show this help message")
    print("🚪 /exit      - Exit the chatbot")
    print("="*50)

def main():
    print("🤖 Welcome to the Simple ChatBot!")
    print("="*40)
    
    # Get API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        api_key = input("🔑 Please enter your OpenAI API key: ").strip()
        if not api_key:
            print("❌ API key is required to continue.")
            return
    
    # Initialize chatbot
    try:
        chatbot = SimpleChatBot(api_key)
        print("✅ Chatbot initialized successfully!")
    except Exception as e:
        print(f"❌ Failed to initialize chatbot: {e}")
        return
    
    display_help()
    print(f"\n💡 Current system prompt: {chatbot.system_prompt}")
    print("\n🚀 Ready to chat! Type your message or use commands starting with '/'")
    
    while True:
        try:
            user_input = input("\n👤 You: ").strip()
            
            if not user_input:
                continue
            
            # Handle commands
            if user_input.startswith('/'):
                command = user_input[1:].lower()
                
                if command == 'exit':
                    print("👋 Goodbye!")
                    break
                
                elif command == 'help':
                    display_help()
                
                elif command == 'clear':
                    chatbot.conversation_history = []
                    print("🧹 Conversation history cleared!")
                
                elif command == 'history':
                    chatbot.show_history()
                
                elif command == 'system':
                    print("\n📝 SYSTEM PROMPT OPTIONS:")
                    presets = get_system_prompt_presets()
                    for key, (name, _) in presets.items():
                        print(f"   {key}. {name}")
                    print("   custom. Enter your own prompt")
                    
                    choice = input("\nChoose option (1-5 or 'custom'): ").strip()
                    
                    if choice in presets:
                        name, prompt = presets[choice]
                        chatbot.set_system_prompt(prompt)
                        print(f"✅ Switched to: {name}")
                    elif choice.lower() == 'custom':
                        custom_prompt = input("Enter your custom system prompt: ").strip()
                        if custom_prompt:
                            chatbot.set_system_prompt(custom_prompt)
                    else:
                        print("❌ Invalid choice.")
                
                elif command == 'save':
                    filename = input("Enter filename (press Enter for auto-generated): ").strip()
                    filename = filename if filename else None
                    chatbot.save_conversation(filename)
                
                elif command == 'load':
                    filename = input("Enter filename to load: ").strip()
                    if filename:
                        chatbot.load_conversation(filename)
                
                else:
                    print(f"❌ Unknown command: {command}. Type '/help' for available commands.")
            
            else:
                # Regular chat message
                print("\n🤖 Assistant:", end=" ")
                response = chatbot.get_response(user_input)
                print(response)
        
        except KeyboardInterrupt:
            print("\n\n👋 Chat interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
