# Intelligent Tool Recommendation System

This project is a **modular, intelligent tool recommendation system** designed to assist developers, engineers, and technical professionals in discovering, analyzing, and installing the best development tools for their projects and workflows.

## 🚀 Key Features

### Tool Recommendation Engine

- **Live Web Search**: Uses Brave API for current tool discovery
- **AI-Powered Analysis**: Gemini AI evaluates tools for relevance, reliability, and ease of use
- **Smart Rankings**: Tools ranked based on multiple criteria including community support and security
- **Installation Guides**: Automatic generation of official installation instructions
- **Comparative Analysis**: Side-by-side tool comparisons
- **Task-Specific Recommendations**: Curated suggestions for specific development workflows

### Development Tool Discovery

- **Multi-Category Support**: Web development, mobile apps, desktop applications, databases, DevOps, testing, design, data science, AI/ML, game development, security, and productivity tools
- **Framework Recommendations**: React, Vue.js, Angular, Django, Flask, Express.js, and more
- **Tool Comparison**: Side-by-side analysis of similar tools
- **Technology Stack Guidance**: Complete toolchain recommendations for specific project types

### Multi-AI Support

- **OpenAI GPT Models** (default)
- **Anthropic Claude**
- **Google Gemini**
- **DeepSeek** (via OpenAI API)

## 🛠 Architecture

Built on **Pydantic AI** and **Model Context Protocol (MCP)** for clean, modular design:

```text
app.py                          # Main chat interface
tool_recommendation/
└── mcp_server.py              # 🆕 Intelligent tool discovery & analysis
brave_search.py                 # Brave API integration
python_tools.py                 # Data processing utilities
```

**Current Status:** Fully operational system with intelligent tool recommendation, multi-AI support, interactive chat with permission prompts, and comprehensive development tool analysis capabilities. The tool recommendation engine provides smart suggestions for web development, mobile development, DevOps, databases, testing frameworks, and more.

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone <repository-url>
cd Docy_Search

# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

Create a `.env` file with your API keys:

```env
# Required for tool recommendation system
BRAVE_API_KEY=your_brave_search_api_key
GOOGLE_API_KEY=your_gemini_api_key

# Optional: Choose your preferred AI model
AI_MODEL=gemini  # Options: openai, claude, gemini, deepseek

# Add other API keys as needed
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_claude_key
```

### 3. Set Up Project Context (Optional)

Create a `project_context.md` file with details about your project:

```bash
# Copy the example and customize it
cp project_context_example.md project_context.md
# Edit with your project details
nano project_context.md
```

The assistant will automatically load this context and provide more targeted recommendations based on your specific project, tech stack, and goals.

### 4. Test the System

```bash
# Test tool recommendation functionality
python test_tool_recommendation.py

# Start the interactive chat
python app.py
```

## 💡 Usage Examples

### Tool Discovery & Recommendations

```text
User: "I need tools for React web development"
Bot: I'll search for React development tools and analyze the best options...

User: "Compare Vue.js vs Angular"
Bot: I'll provide a detailed comparison of these JavaScript frameworks...

User: "How do I set up a Django project?"
Bot: I'll generate step-by-step setup instructions for Django development...
```

### Development Workflows

```text
User: "What's the best database for a Node.js project?"
Bot: I'll recommend databases that work well with Node.js and provide setup guides...

User: "Set up a complete full-stack development environment"
Bot: I'll suggest tools and provide setup instructions for frontend, backend, and database tools...
```

### Task-Specific Workflows

```text
User: "What tools should a beginner use for web development?"
Bot: I'll recommend beginner-friendly web development tools with installation guides...

User: "Best DevOps tools for small teams"
Bot: I'll suggest DevOps tools suitable for small development teams...
```

## 🔧 Advanced Features

### Tool Categories

- **Web Development**: React, Vue.js, Angular, Django, Flask, Express.js
- **Mobile Development**: React Native, Flutter, Xamarin, Ionic
- **Desktop Applications**: Electron, Tauri, Qt, .NET
- **Databases**: PostgreSQL, MongoDB, Redis, MySQL, SQLite
- **DevOps**: Docker, Kubernetes, Jenkins, GitLab CI, Terraform
- **Testing**: Jest, Pytest, Selenium, Cypress, Postman
- **Design**: Figma, Sketch, Adobe XD, Canva, GIMP
- **Data Science**: Pandas, NumPy, Jupyter, Tableau, Power BI
- **AI/ML**: TensorFlow, PyTorch, Scikit-learn, Keras
- **Game Development**: Unity, Unreal Engine, Godot, Phaser
- **Security**: OWASP tools, security scanners, encryption libraries
- **Productivity**: VS Code, Git, Slack, Notion, Trello

### AI-Powered Analysis

Each tool recommendation includes:

- **Relevance Score** (1-10)
- **Reliability Assessment**
- **Installation Complexity** (Easy/Medium/Hard)
- **Community Support Rating**
- **Security & Trust Evaluation**
- **Use Case Scenarios**

### Integration Benefits

- **Live Data**: Always current tool information via Brave Search
- **Smart Analysis**: AI evaluates beyond simple search results
- **Practical Focus**: Real installation guides and usage tips
- **Skill-Adaptive**: Recommendations match user experience level
- **Development-Focused**: Tailored for software development workflows

## 📁 File Structure

```text
Docy_Search/
├── app.py                              # Main application
├── test_tool_recommendation.py         # Test script
├── demo_tool_recommendation.py         # Demo script
├── Tool_Recommendation_Guide.md        # Detailed usage guide
├── requirements.txt                    # Dependencies
├── .env                               # API keys (create this)
├── tool_recommendation/
│   └── mcp_server.py                  # Core recommendation engine
├── brave_search.py                    # Search API integration
└── python_tools.py                   # Utility functions
```

## 🤝 Contributing

This project uses a modular MCP (Model Context Protocol) architecture. To add new functionality:

1. Create new MCP server in appropriate directory
2. Follow the existing pattern (see `tool_recommendation/mcp_server.py`)
3. Add server to `app.py`
4. Update system prompt if needed

For detailed usage examples, see `Tool_Recommendation_Guide.md`.

