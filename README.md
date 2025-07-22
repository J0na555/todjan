# 📝 Todjan - Django Task Manager

**Todjan** is a simple web-based task management application built with Django. It includes features like user authentication, task creation and editing, and a minimal UI — perfect for learning full-stack Python web development!

---

## 🌐 Live Demo

🔗 [Visit Todjan on Render](https://todjan.onrender.com)

---

## 🚀 Features

- 🔐 User authentication (sign up, log in, log out)
- ✅ Add, edit, and delete tasks
- 🎯 Mark tasks as completed
- 📅 Due dates and task priorities (optional)
- 🌙 Dark mode (optional, if added)

---

## 🧠 Tech Stack

| Layer        | Technology       |
|--------------|------------------|
| Backend      | Django 5.2.4     |
| Frontend     | HTML, CSS, JS (vanilla) |
| Deployment   | [Render](https://render.com) |
| Python Env   | Python 3.13.4    |

---

## 🛠️ Local Development Setup

### Prerequisites

- Python 3.10+
- pip

### Clone and run locally

```bash
git clone https://github.com/Jona555/todjan.git
cd todjan
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
