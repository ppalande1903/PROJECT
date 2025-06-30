import streamlit as st
import json
import re
from datetime import datetime
from typing import Dict, List, Optional
import openai
from dataclasses import dataclass, asdict
import os

# Configure page
st.set_page_config(
    page_title="TalentScout - AI Hiring Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better UI
st.markdown("""
<style>
.main-header {
    text-align: center;
    padding: 2rem 0;
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 10px;
    margin-bottom: 2rem;
}

.chat-message {
    padding: 1rem;
    border-radius: 10px;
    margin: 1rem 0;
    border-left: 4px solid #667eea;
    background-color: #f8f9fa;
}

.user-message {
    background-color: #e3f2fd;
    border-left-color: #2196f3;
}

.bot-message {
    background-color: #f3e5f5;
    border-left-color: #9c27b0;
}

.info-card {
    background: white;
    padding: 1.5rem;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    margin: 1rem 0;
}
</style>
""", unsafe_allow_html=True)

@dataclass
class CandidateInfo:
    full_name: str = ""
    email: str = ""
    phone: str = ""
    experience_years: str = ""
    desired_position: str = ""
    location: str = ""
    tech_stack: List[str] = None
    
    def __post_init__(self):
        if self.tech_stack is None:
            self.tech_stack = []

class HiringAssistant:
    def __init__(self):
        self.conversation_stages = [
            "greeting",
            "name_collection",
            "email_collection", 
            "phone_collection",
            "experience_collection",
            "position_collection",
            "location_collection",
            "tech_stack_collection",
            "technical_questions",
            "conclusion"
        ]
        self.current_stage_index = 0
        self.candidate_info = CandidateInfo()
        self.technical_questions = []
        self.current_question_index = 0
        self.conversation_ended = False
        
    def get_current_stage(self):
        if self.current_stage_index < len(self.conversation_stages):
            return self.conversation_stages[self.current_stage_index]
        return "conclusion"
    
    def advance_stage(self):
        self.current_stage_index += 1
    
    def is_exit_keyword(self, user_input: str) -> bool:
        exit_keywords = ["bye", "goodbye", "exit", "quit", "end", "stop", "finish"]
        return any(keyword in user_input.lower() for keyword in exit_keywords)
    
    def validate_email(self, email: str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def validate_phone(self, phone: str) -> bool:
        # Remove all non-digit characters
        digits_only = re.sub(r'\D', '', phone)
        # Check if it has 10-15 digits (common phone number lengths)
        return 10 <= len(digits_only) <= 15
    
    def extract_tech_stack(self, user_input: str) -> List[str]:
        # Common tech stack keywords
        tech_keywords = [
            # Programming Languages
            "python", "java", "javascript", "typescript", "c++", "c#", "php", "ruby", "go", "rust", "kotlin", "swift",
            # Frontend
            "react", "angular", "vue", "html", "css", "bootstrap", "tailwind",
            # Backend
            "node.js", "express", "django", "flask", "spring", "laravel", "rails",
            # Databases
            "mysql", "postgresql", "mongodb", "redis", "sqlite", "oracle",
            # Cloud & DevOps
            "aws", "azure", "gcp", "docker", "kubernetes", "jenkins", "git",
            # Others
            "tensorflow", "pytorch", "pandas", "numpy", "rest", "graphql"
        ]
        
        found_tech = []
        user_lower = user_input.lower()
        
        for tech in tech_keywords:
            if tech in user_lower:
                found_tech.append(tech.title())
        
        return found_tech
    
    def generate_technical_questions(self, tech_stack: List[str]) -> List[str]:
        """Generate technical questions based on the candidate's tech stack"""
        questions = []
        
        # Question templates for different technologies
        question_templates = {
            "Python": [
                "What is the difference between list and tuple in Python?",
                "Explain Python's GIL (Global Interpreter Lock).",
                "How do you handle exceptions in Python?"
            ],
            "Java": [
                "What is the difference between JDK, JRE, and JVM?",
                "Explain the concept of polymorphism in Java.",
                "What are the main principles of OOP in Java?"
            ],
            "Javascript": [
                "What is the difference between == and === in JavaScript?",
                "Explain closures in JavaScript with an example.",
                "What is the event loop in JavaScript?"
            ],
            "React": [
                "What is the difference between state and props in React?",
                "Explain the React component lifecycle.",
                "What are React Hooks and why are they useful?"
            ],
            "Django": [
                "What is Django ORM and how does it work?",
                "Explain the MVC pattern in Django.",
                "What are Django middlewares and their use cases?"
            ],
            "Node.js": [
                "What is the event-driven architecture in Node.js?",
                "Explain the difference between synchronous and asynchronous programming.",
                "What are callbacks, promises, and async/await?"
            ],
            "Mysql": [
                "What is the difference between INNER JOIN and LEFT JOIN?",
                "Explain database normalization and its types.",
                "What are indexes and how do they improve query performance?"
            ],
            "Aws": [
                "What are the main AWS services you've worked with?",
                "Explain the difference between EC2 and Lambda.",
                "What is the purpose of AWS S3 and its use cases?"
            ]
        }
        
        # Generate questions for each technology in the stack
        for tech in tech_stack[:3]:  # Limit to 3 technologies to avoid too many questions
            if tech in question_templates:
                tech_questions = question_templates[tech]
                questions.extend(tech_questions[:2])  # Take 2 questions per technology
        
        # If no specific questions found, add general questions
        if not questions:
            questions = [
                "Describe a challenging technical problem you've solved recently.",
                "How do you stay updated with new technologies in your field?",
                "What's your approach to debugging code?",
                "How do you ensure code quality in your projects?"
            ]
        
        return questions[:5]  # Limit to 5 questions maximum
    
    def get_response(self, user_input: str) -> str:
        if self.is_exit_keyword(user_input):
            self.conversation_ended = True
            return "Thank you for your time! We'll review your information and get back to you soon. Have a great day! 👋"
        
        current_stage = self.get_current_stage()
        
        if current_stage == "greeting":
            self.advance_stage()
            return """Hello! 👋 Welcome to TalentScout's AI Hiring Assistant! 

I'm here to help with your initial screening for technology positions. I'll gather some basic information about you and ask a few technical questions based on your expertise.

This should take about 5-10 minutes. You can type 'exit' or 'bye' anytime to end our conversation.

Let's get started! What's your full name?"""

        elif current_stage == "name_collection":
            if user_input.strip():
                self.candidate_info.full_name = user_input.strip()
                self.advance_stage()
                return f"Nice to meet you, {self.candidate_info.full_name}! 😊\n\nCould you please provide your email address?"
            else:
                return "Please provide your full name to continue."

        elif current_stage == "email_collection":
            if self.validate_email(user_input.strip()):
                self.candidate_info.email = user_input.strip()
                self.advance_stage()
                return "Great! Now, what's your phone number?"
            else:
                return "Please provide a valid email address (e.g., john@example.com)."

        elif current_stage == "phone_collection":
            if self.validate_phone(user_input.strip()):
                self.candidate_info.phone = user_input.strip()
                self.advance_stage()
                return "Perfect! How many years of professional experience do you have in technology?"
            else:
                return "Please provide a valid phone number."

        elif current_stage == "experience_collection":
            if user_input.strip():
                self.candidate_info.experience_years = user_input.strip()
                self.advance_stage()
                return "Thanks! What position(s) are you interested in? (e.g., Software Developer, Data Scientist, DevOps Engineer)"
            else:
                return "Please specify your years of experience."

        elif current_stage == "position_collection":
            if user_input.strip():
                self.candidate_info.desired_position = user_input.strip()
                self.advance_stage()
                return "Excellent! What's your current location (city, state/country)?"
            else:
                return "Please specify the position you're interested in."

        elif current_stage == "location_collection":
            if user_input.strip():
                self.candidate_info.location = user_input.strip()
                self.advance_stage()
                return """Now for the technical part! 💻

Please tell me about your tech stack. List the programming languages, frameworks, databases, and tools you're proficient in.

For example: "Python, Django, React, PostgreSQL, AWS, Docker" """
            else:
                return "Please provide your current location."

        elif current_stage == "tech_stack_collection":
            if user_input.strip():
                tech_stack = self.extract_tech_stack(user_input)
                if tech_stack:
                    self.candidate_info.tech_stack = tech_stack
                    self.technical_questions = self.generate_technical_questions(tech_stack)
                    self.advance_stage()
                    return f"""Perfect! I've identified your expertise in: {', '.join(tech_stack)}

Now I'll ask you {len(self.technical_questions)} technical questions to assess your proficiency. Please answer them to the best of your ability.

**Question 1:** {self.technical_questions[0] if self.technical_questions else "Tell me about a recent project you've worked on."}"""
                else:
                    return "I couldn't identify specific technologies. Please mention specific programming languages, frameworks, or tools you know (e.g., Python, React, MySQL, etc.)."
            else:
                return "Please tell me about your technical skills and tools you use."

        elif current_stage == "technical_questions":
            if user_input.strip():
                self.current_question_index += 1
                
                if self.current_question_index < len(self.technical_questions):
                    return f"Thank you for your answer! 👍\n\n**Question {self.current_question_index + 1}:** {self.technical_questions[self.current_question_index]}"
                else:
                    self.advance_stage()
                    return """Excellent! You've completed all the technical questions. 🎉

Let me summarize the information we've collected:

""" + self.get_candidate_summary() + """

Thank you for taking the time to complete this screening! Our recruitment team will review your responses and contact you within 2-3 business days if your profile matches our current openings.

Is there anything else you'd like to know about TalentScout or our process?"""
            else:
                return "Please provide an answer to continue with the next question."

        else:  # conclusion stage
            return """Thank you for your interest in TalentScout! 🌟

Your information has been recorded and our team will be in touch soon. 

Have a wonderful day, and good luck with your job search!

Type 'bye' to end our conversation."""

    def get_candidate_summary(self) -> str:
        return f"""
**Candidate Summary:**
• **Name:** {self.candidate_info.full_name}
• **Email:** {self.candidate_info.email}
• **Phone:** {self.candidate_info.phone}
• **Experience:** {self.candidate_info.experience_years} years
• **Desired Position:** {self.candidate_info.desired_position}
• **Location:** {self.candidate_info.location}
• **Tech Stack:** {', '.join(self.candidate_info.tech_stack) if self.candidate_info.tech_stack else 'Not specified'}
• **Questions Completed:** {len(self.technical_questions)} technical questions answered
"""

# Initialize session state
if 'assistant' not in st.session_state:
    st.session_state.assistant = HiringAssistant()
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'conversation_started' not in st.session_state:
    st.session_state.conversation_started = False

# Header
st.markdown("""
<div class="main-header">
    <h1>🤖 TalentScout AI Hiring Assistant</h1>
    <p>Your intelligent partner for tech talent screening</p>
</div>
""", unsafe_allow_html=True)

# Sidebar with information
with st.sidebar:
    st.header("ℹ️ About This Assistant")
    st.write("""
    This AI assistant will help screen candidates for technology positions by:
    
    ✅ Collecting basic information
    ✅ Understanding your tech stack
    ✅ Asking relevant technical questions
    ✅ Providing a smooth interview experience
    
    **Privacy Notice:** All data is handled securely and used only for recruitment purposes.
    """)
    
    st.header("📊 Progress")
    if st.session_state.assistant:
        current_stage = st.session_state.assistant.get_current_stage()
        progress = (st.session_state.assistant.current_stage_index / len(st.session_state.assistant.conversation_stages)) * 100
        st.progress(progress / 100)
        st.write(f"Current Stage: {current_stage.replace('_', ' ').title()}")

# Main chat interface
st.header("💬 Chat Interface")

# Display conversation history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"""
        <div class="chat-message user-message">
            <strong>You:</strong> {message["content"]}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-message bot-message">
            <strong>Assistant:</strong> {message["content"]}
        </div>
        """, unsafe_allow_html=True)

# Start conversation button or chat input
if not st.session_state.conversation_started:
    if st.button("🚀 Start Screening Process", type="primary", use_container_width=True):
        st.session_state.conversation_started = True
        welcome_message = st.session_state.assistant.get_response("")
        st.session_state.messages.append({"role": "assistant", "content": welcome_message})
        st.rerun()
else:
    # Chat input
    if not st.session_state.assistant.conversation_ended:
        user_input = st.chat_input("Type your response here...")
        
        if user_input:
            # Add user message
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            # Get assistant response
            response = st.session_state.assistant.get_response(user_input)
            st.session_state.messages.append({"role": "assistant", "content": response})
            
            st.rerun()
    else:
        st.success("🎉 Conversation completed! Thank you for using TalentScout's AI Hiring Assistant.")
        
        # Show final summary
        if st.session_state.assistant.candidate_info.full_name:
            st.markdown("### 📋 Final Summary")
            st.markdown(st.session_state.assistant.get_candidate_summary())
        
        if st.button("🔄 Start New Conversation"):
            st.session_state.assistant = HiringAssistant()
            st.session_state.messages = []
            st.session_state.conversation_started = False
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>🏢 TalentScout - Connecting Tech Talent with Opportunities</p>
    <p><small>Built with Streamlit • Powered by AI</small></p>
</div>
""", unsafe_allow_html=True)