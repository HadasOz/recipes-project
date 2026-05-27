# Gourmet Recipes - Full-Stack Web Application

A robust, modern Full-Stack Web Application for managing and exploring culinary recipes. This project features a Python-based backend API integrated with a relational database and an interactive user interface, alongside an AI-powered culinary assistant feature.

## 🚀 Features

* **Recipe Management:** Full CRUD operations (Create, Read, Update, Delete) for managing a database of custom recipes.
* **Smart Categorization:** Filter and discover recipes dynamically based on categories utilizing SQL relationship joins.
* **AI Chef Assistant:** Integrated an interactive chat interface leveraging Google Gemini AI to answer baking and cooking queries.
* **Robust Error Handling:** Implemented defensive programming mechanisms to gracefully manage network errors and secure secure communication workflows.
* **Modern API Architecture:** Fast, structured, and async-supported RESTful API endpoints.

## 🛠️ Tech Stack

* **Backend:** Python, FastAPI, Uvicorn
* **Database:** Microsoft SQL Server (MS SQL), pyodbc
* **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
* **AI Integration:** Google GenAI (Gemini API)
* **Environment Management:** python-dotenv (Secure Configuration)

## 🔒 Security & Best Practices

* **Secure Environments:** Implemented environment variables (`.env`) to decouple sensitive data (such as API keys) from the source code, adhering to industry security standards.
* **Database Clean Architecture:** Managed independent, isolated request connections to prevent connection leaks and optimize query execution.

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/HadasOz/recipes-project.git](https://github.com/HadasOz/recipes-project.git)
   cd recipes-project
