NPI Calculator

Description:
This is a simple NPI (Numeric Postfix Integer) Calculator built using FastAPI for the backend and React for the frontend. The application evaluates postfix expressions and stores the results in a SQLite database.

Project Structure:
npi_calculator/
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI application entry point
│   │   ├── database.py      # Database setup and session management
│   │   ├── models.py        # SQLAlchemy models
│   │   ├── schemas.py       # Pydantic schemas for request validation
│   │   ├── npi.py           # Logic for evaluating NPI expressions
│   ├── Dockerfile            # Docker configuration for the backend
│   ├── requirements.txt      # Python dependencies
├── frontend/
│   ├── Dockerfile            # Docker configuration for the frontend
│   ├── src/                 # React application source code
├── docker-compose.yml        # Docker Compose configuration
└── README.txt                # Project documentation

Prerequisites:
- Docker
- Docker Compose

Getting Started:
1. Clone the repository and redirect to the folder:
   cd npi_calculator

2. Build and run the application:
   docker-compose up --build

3. Access the application:
   - Backend API: http://localhost:8000
   - Frontend: http://localhost:3000

API Endpoints:
- POST /calculate: Evaluate a postfix expression.
  Request Body:
  {
    "expression": "3 4 + 2 * 7 /"
  }
  Response:
  {
    "expression": "3 4 + 2 * 7 /",
    "result": 2.0
  }

- GET /export_csv: Export calculation results to a CSV file. you can test this endpoint by running the url : http://localhost:8000/export_csv

Database:
This application uses SQLite to store calculations. The database file (npi.db) is created inside the Docker container.

Author:
Yakoub AZZOUNI
