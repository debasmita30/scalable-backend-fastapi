## Scalable Backend Service — FastAPI

A production-ready backend service built with FastAPI, JWT authentication, SQLAlchemy, and Docker, accompanied by a modern interactive frontend for live API demonstration.

This project demonstrates real-world backend engineering practices: authentication, protected routes, pagination, clean architecture, containerization, and frontend–backend integration.

🚀 Features

RESTful APIs using FastAPI

JWT-based authentication (OAuth2 password flow)

Protected routes with Bearer token authorization

SQLAlchemy ORM with SQLite (easily extensible to PostgreSQL)

Pagination support for scalable APIs

Dockerized for consistent deployment

Interactive frontend demo (HTML + JS)

Swagger UI for API exploration

Clean, modular project structure

Ready for cloud deployment

🧱 Tech Stack

Backend: FastAPI, SQLAlchemy, Pydantic

Auth: JWT (python-jose), OAuth2

Database: SQLite

Server: Uvicorn

Containerization: Docker

Frontend: HTML, CSS, Vanilla JavaScript

API Docs: Swagger UI

📁 Project Structure
scalable-backend-python/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── auth.py
│   ├── database.py
│   ├── schemas.py
│   ├── crud.py
│   ├── dependencies.py
│   └── routers/
│       ├── __init__.py
│       ├── users.py
│       └── tasks.py
├── frontend/
│   └── index.html
├── tests/
│   ├── test_users.py
│   └── test_tasks.py
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md

▶️ Running Locally (Without Docker)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload


Open:

API Docs: http://localhost:8000/docs

Frontend: open frontend/index.html in browser

🐳 Running with Docker
docker build -t scalable-backend .
docker run -p 8000:8000 scalable-backend


Open:

API Docs: http://localhost:8000/docs

🔐 Authentication Flow (Demo)

Login using demo credentials

Receive JWT access token

Token automatically used for protected API calls

Access secured endpoints like /users

🧪 API Demo Flow (Swagger)

POST /users/login

Authorize using Bearer token

Call GET /users (protected)

View paginated results

🎨 Frontend Demo

The frontend provides:

One-click demo data loading

Login with visual feedback

Token handling and inspection

Protected API calls

User table rendering

Request timeline tracking

Live status indicators

This frontend is designed only for demonstration and validation of backend functionality.

🧩 Why This Project Matters

This is not just a login page.

It showcases:

Backend system design

Authentication and authorization

API security patterns

Clean code architecture

Docker-based deployment

Full backend-frontend integration

Equivalent to what is expected in real production services.

📌 Future Enhancements

Role-based access control

Refresh tokens

PostgreSQL integration

CI/CD pipeline

Rate limiting

API versioning

👤 Author

Debasmita Chatterjee
Backend • Data • Systems Engineering
