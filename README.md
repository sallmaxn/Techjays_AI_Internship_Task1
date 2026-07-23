# 🤖 ChatGPT Clone

### Techjays AI Internship – Phase 1

> A modern AI-powered conversational web application built with **Django**, **OpenRouter**, and the **OpenAI Python SDK**, featuring secure authentication, persistent chat sessions, conversation memory, and a ChatGPT-inspired user interface.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-5.x-green?style=for-the-badge&logo=django)
![OpenRouter](https://img.shields.io/badge/OpenRouter-AI-purple?style=for-the-badge)
![Pylint](https://img.shields.io/badge/Pylint-10.0%2F10-brightgreen?style=for-the-badge)
![Tests](https://img.shields.io/badge/Tests-Passed-success?style=for-the-badge)

---

# 👨‍💻 Author

**Salman Paris**

B.Sc. Artificial Intelligence & Machine Learning

---

# 📖 Project Overview

This project is a **ChatGPT-inspired AI web application** developed as part of the **Techjays AI Internship – Phase 1**.

The application allows users to securely register, log in, create multiple chat sessions, and interact with an AI assistant powered by an **OpenAI-compatible Large Language Model** through **OpenRouter**.

Each conversation is permanently stored in the database, allowing users to revisit previous chats while maintaining complete conversational context.

The project demonstrates backend development using Django, AI integration with the OpenAI Python SDK, session management, authentication, asynchronous communication using AJAX, and clean software engineering practices.

---

# ✨ Features

## 🔐 Authentication

- User Registration
- Secure Login & Logout
- Django Authentication System
- Session-Based Authentication

## 💬 Chat Features

- ChatGPT-style Interface
- Multiple Chat Sessions
- Persistent Chat History
- Conversation Memory
- Context-Aware AI Responses
- Dynamic Chat Titles

## ⚡ User Experience

- AJAX Messaging (No Page Reload)
- Responsive Dark Mode UI
- Loading Indicator
- Auto Scroll
- Enter Key to Send Messages
- Markdown Rendering for AI Responses

## 🤖 AI Integration

- OpenRouter API
- OpenAI Python SDK
- OpenAI-Compatible Architecture
- Easily Switch LLM Providers

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Backend | Django |
| Frontend | HTML, CSS, JavaScript (AJAX) |
| Authentication | Django Authentication |
| Database | SQLite |
| AI SDK | OpenAI Python SDK |
| AI Provider | OpenRouter |
| Version Control | Git & GitHub |

---

# 🏗️ Architecture

```text
                    User
                      │
                      ▼
            Django Authentication
                      │
                      ▼
               Django Views
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
   ChatSession Model        Message Model
                      │
                      ▼
         OpenAI Python SDK Client
                      │
                      ▼
              OpenRouter API
                      │
                      ▼
           AI Generated Response
```

---

# 🗄️ Database Design

```text
User
│
└── ChatSession
      │
      ├── Title
      ├── Created At
      │
      └── Message
            ├── role = user
            └── role = assistant
```

Each authenticated user can create multiple chat sessions. Every chat session stores the complete conversation history, allowing the AI to generate context-aware responses by using previous messages.

---

# 📸 Application Screenshots

## 🔑 Login Page

![Login](screenshots/login.png)

---

## 📝 Signup Page

![Signup](screenshots/signup.png)

---

## 💬 Chat Interface

![Chat](screenshots/chat.png)

---

## 📚 Chat History

![History](screenshots/history.png)

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY.git
```

## Navigate to the Project

```bash
cd YOUR_REPOSITORY
```

## Create a Virtual Environment

```bash
python -m venv venv
```

## Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=YOUR_OPENROUTER_API_KEY
```

## Apply Database Migrations

```bash
python manage.py migrate
```

## Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/login
```

---

# 📋 Usage

1. Create a new account.
2. Log in securely.
3. Click **New Chat** to start a conversation.
4. Send a message to the AI assistant.
5. Continue conversations with full context preserved.
6. Switch between previous chat sessions from the sidebar.
7. Log out securely when finished.

---

# 🧪 Testing

Run all Django unit tests:

```bash
python manage.py test
```

---

# 📊 Code Quality

Check the project using Pylint:

```bash
pylint chat
```

**Pylint Score:** **10.00 / 10** ✅

**Django Tests:** ✅ All Passed

---

# 📂 Project Structure

```text
chatgpt-clone/
│
├── accounts/
├── chat/
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── static/
├── templates/
├── screenshots/
├── README.md
├── requirements.txt
├── .gitignore
└── manage.py
```

---

# 🚀 Future Improvements

- 🗑️ Delete Chat Sessions
- ✏️ Rename Chat Sessions
- 📄 Export Chat History
- 📎 File Upload Support
- 🌊 Streaming AI Responses
- 🤖 Multiple AI Model Selection
- 📱 Progressive Web App (PWA)

---

# 📚 Learning Outcomes

This project helped me gain practical experience in:

- Django Authentication
- Django ORM & Database Design
- Session Management
- OpenAI Python SDK
- OpenRouter API Integration
- Prompt Engineering Fundamentals
- Conversation Memory
- AJAX & Asynchronous Requests
- Git & GitHub Workflow
- Django Unit Testing
- Code Quality using Pylint
- Modern Backend Development Practices

---

# 👨‍💻 Author

**Salman Paris**

🎓 B.Sc. Artificial Intelligence & Machine Learning

GitHub:
https://github.com/sallmaxn

---

# ⭐ Techjays AI Internship – Phase 1

This project was developed as part of the **Techjays AI Internship – Phase 1** to demonstrate practical skills in:

- Backend Development with Django
- AI Integration using OpenAI-Compatible APIs
- Authentication & Session Management
- Persistent Chat Applications
- Clean Software Architecture
- Version Control with Git & GitHub
- Professional Project Documentation

---

## 📜 License

This project is licensed under the **MIT License**.