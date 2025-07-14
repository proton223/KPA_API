
# KPA Form API – FastAPI Backend

A lightweight REST API built using FastAPI and SQLAlchemy for submitting and retrieving KPA form data. Developed as part of a backend assignment with structured project organization and Postman test support.

---

## Features

- ✅ Submit new KPA form data (POST `/kpa`)
- ✅ Retrieve form data by ID (GET `/kpa/{id}`)
- 📄 Swagger UI for API docs at `/docs`
- 🗃 SQLite database with SQLAlchemy ORM
- 🧪 Tested with Postman collection

---

## Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Pydantic
- dotenv

---

## Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/kpa_api_assignment
cd kpa_api_assignment

# 2. Create virtual environment
python -m venv env
env\Scripts\activate   # or source env/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
uvicorn main:app --reload
Open in browser: http://127.0.0.1:8000/docs

API Reference
POST /kpa
Create a new form record
Fields: name, email, mobile

GET /kpa/{id}
Retrieve form data by ID

Environment
.env

ini
Copy
Edit
DB_URL=sqlite:///./kpa_local.db
