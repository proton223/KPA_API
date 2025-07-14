# KPA API Assignment - FastAPI

## 📦 Project Description

This FastAPI backend implements two endpoints to create and retrieve KPA form data using an SQLite database.

## ▶️ How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Start the development server:
uvicorn main:app --reload

3. Open Swagger UI to test:
http://127.0.0.1:8000/docs


## 🚀 API Endpoints

- **POST** `/kpa`  
  Create a new KPA form

- **GET** `/kpa/{id}`  
  Retrieve form data by ID

## 🗃 Tech Stack

- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite (via SQLAlchemy)
- Python-dotenv

