# 🤖 TalentScout AI Hiring Assistant

An intelligent chatbot for initial candidate screening in technology recruitment, built with Streamlit and advanced prompt engineering techniques.

## 📋 Project Overview

TalentScout's AI Hiring Assistant is designed to streamline the initial screening process for technology positions. The chatbot intelligently gathers candidate information, understands their technical expertise, and generates relevant technical questions based on their declared tech stack.

### Key Features

- **Intelligent Information Gathering**: Collects essential candidate details with validation
- **Dynamic Tech Stack Recognition**: Identifies technologies from natural language input
- **Adaptive Technical Questions**: Generates relevant questions based on candidate's expertise
- **Context-Aware Conversations**: Maintains conversation flow and handles edge cases
- **User-Friendly Interface**: Clean, intuitive Streamlit UI with progress tracking
- **Data Privacy Compliant**: Secure handling of candidate information
- **Graceful Exit Handling**: Responds to conversation-ending keywords

## 🚀 Installation Instructions

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd talentscout-hiring-assistant
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   streamlit run app.py
   ```

5. **Access the Application**
   - Open your browser and navigate to `http://localhost:8501`
   - The chatbot interface will be ready to use

## 📖 Usage Guide

### Starting a Conversation
1. Click the "🚀 Start Screening Process" button
2. Follow the chatbot's prompts to provide your information
3. Answer technical questions based on your expertise
4. Review the final summary of your screening

### Conversation Flow
1. **Greeting**: Welcome message and overview
2. **Personal Information**: Name, email, phone, experience, position, location
3. **Tech Stack Declaration**: List your technical skills and tools
4. **Technical Assessment**: Answer 3-5 relevant technical questions
5. **Conclusion**: Summary and next steps

### Exit Commands
Type any of these keywords to end the conversation:
- `bye`, `goodbye`, `exit`, `quit`, `end`, `stop`, `finish`

## 🛠️ Technical Details

### Architecture
- **Frontend**: Streamlit web framework
- **Backend**: Python with dataclasses for data management
- **State Management**: Streamlit session state
- **UI Components**: Custom CSS styling with responsive design

### Libraries Used
- **Streamlit** (>=1.28.0): Web framework for the user interface
- **dataclasses**: Structured data management for candidate information
- **re**: Regular expressions for email and phone validation
- **typing**: Type hints for better code documentation
- **datetime**: Timestamp management

### Core Components

#### 1. CandidateInfo Class
```python
@dataclass
class CandidateInfo:
    full_name: str = ""
    email: str = ""
    phone: str = ""
    experience_years: str = ""
    desired_position: str = ""
    location: str = ""
    tech_stack: List[str] = None
```

#### 2. HiringAssistant Class
Main chatbot logic with conversation management:
- Stage-based conversation flow
- Input validation and sanitization
- Tech stack extraction and question generation
- Context maintenance

### Key Methods

- `get_response()`: Main conversation handler
- `extract_tech_stack()`: Identifies technologies from user input
- `generate_technical_questions()`: Creates relevant technical questions
- `validate_email()` & `validate_phone()`: Input validation
- `is_exit_keyword()`: Detects conversation end requests

## 🎯 Prompt Design Strategy

### Information Gathering Prompts
The chatbot uses progressive disclosure, asking for one piece of information at a time to:
- Reduce cognitive load on candidates
- Ensure accurate data collection
- Maintain conversation flow
- Provide clear validation feedback

### Technical Question Generation
Questions are generated based on:
- **Tech Stack Mapping**: Pre-defined question banks for popular technologies
- **Difficulty Balancing**: Mix of fundamental and practical questions
- **Relevance Scoring**: Questions matched to candidate's declared expertise
- **Fallback Strategy**: General technical questions when specific tech not recognized

### Context Management
- **Stage Tracking**: Maintains current conversation stage
- **Information Persistence**: Stores candidate data throughout session
- **Error Handling**: Graceful handling of unexpected inputs
- **Conversation Recovery**: Guides users back on track after errors

## 🔧 Challenges & Solutions

### Challenge 1: Tech Stack Recognition
**Problem**: Accurately identifying technologies from free-form text input
**Solution**: 
- Comprehensive keyword dictionary with common variations
- Case-insensitive matching
- Support for multiple formats (comma-separated, natural language)

### Challenge 2: Question Relevance
**Problem**: Generating appropriate technical questions for diverse skill sets
**Solution**:
- Technology-specific question banks
- Difficulty progression from basic to advanced
- Fallback to general technical questions

### Challenge 3: Conversation Flow Management
**Problem**: Maintaining context and handling unexpected user behavior
**Solution**:
- State machine pattern with defined stages
- Input validation at each stage
- Clear error messages and recovery paths

### Challenge 4: User Experience
**Problem**: Making the screening process engaging and professional
**Solution**:
- Progress tracking with visual indicators
- Friendly, conversational tone
- Clear instructions and expectations
- Professional summary at completion

## 📊 Data Handling & Privacy

### Data Storage
- **Session-based**: All data stored in Streamlit session state
- **No Persistence**: Data cleared when session ends
- **Local Processing**: No external API calls for sensitive data

### Privacy Measures
- Input validation to prevent injection attacks
- No logging of sensitive information
- Clear data usage disclosure
- Compliance with GDPR principles

### Security Features
- Email and phone number validation
- Sanitized input handling
- No external data transmission
- Secure local processing

## 🎨 UI/UX Features

### Visual Design
- **Modern Interface**: Clean, professional design with gradient headers
- **Responsive Layout**: Works on desktop and mobile devices
- **Color Coding**: Distinct styling for user and bot messages
- **Progress Indicators**: Visual feedback on screening progress

### Interactive Elements
- **Real-time Chat**: Instant message display and response
- **Progress Tracking**: Sidebar showing current stage and completion
- **Action Buttons**: Clear call-to-action elements
- **Status Indicators**: Visual feedback for different states

### Accessibility
- **High Contrast**: Meets WCAG color contrast requirements
- **Clear Typography**: Readable fonts and appropriate sizing
- **Keyboard Navigation**: Full keyboard accessibility
- **Screen Reader Support**: Semantic HTML structure

## 🚀 Deployment Options

### Local Deployment
```bash
streamlit run app.py
```

### Cloud Deployment (Bonus)

#### Streamlit Cloud
1. Push code to GitHub repository
2. Connect to Streamlit Cloud
3. Deploy with automatic updates

#### AWS/GCP Deployment
1. Create cloud instance
2. Install dependencies
3. Configure security groups
4. Run with production settings

## 🧪 Testing & Quality Assurance

### Test Scenarios
- Complete conversation flow
- Input validation edge cases
- Exit command handling
- Tech stack recognition accuracy
- Question generation quality

### Code Quality
- **PEP 8 Compliance**: Consistent Python styling
- **Type Hints**: Full type annotation
- **Documentation**: Comprehensive docstrings
- **Error Handling**: Robust exception management

## 🔄 Future Enhancements

### Potential Improvements
1. **Multi-language Support**: Internationalization capabilities
2. **Voice Interface**: Speech-to-text integration
3. **Resume Parsing**: Automatic skill extraction from uploaded resumes
4. **Analytics Dashboard**: Screening metrics and insights
5. **Integration APIs**: Connection with ATS systems
6. **Machine Learning**: Adaptive question selection based on performance

### Scalability Considerations
- Database integration for candidate storage
- Redis for session management
- Load balancing for multiple users
- Microservices architecture

## 📞 Support & Contact

For questions or issues with the TalentScout Hiring Assistant:
- Review this documentation
- Check the GitHub issues page
- Contact the development team

---

## 📄 License

This project is developed as part of an AI/ML internship assignment and is intended for educational and demonstration purposes.

**Built with ❤️ using Streamlit and Python**
