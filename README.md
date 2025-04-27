# FastAPI CRUD API with PostgreSQL

This is a simple CRUD API built using FastAPI, SQLAlchemy, and PostgreSQL. It provides endpoints to create, read, update, and delete items from a PostgreSQL database. The project is organized into separate modules for database connection, models, schemas, and main application logic.

The application uses:
- FastAPI for building the API
- SQLAlchemy for ORM (Object Relational Mapping)
- PostgreSQL as the database
- Pydantic for data validation
- Uvicorn as the ASGI server

The main files included are:
- `main.py`: Defines API endpoints for CRUD operations.
- `models.py`: Defines database models using SQLAlchemy.
- `schemas.py`: Defines data schemas using Pydantic.
- `database.py`: Configures the database connection and session.
- `requirements.txt`: Lists the Python packages required to run the project.
- `.env`: Stores environment variables like the database connection URL.

To run the project:

1. Clone the repository:
    ```
    git clone https://github.com/Smokecigarette2/fastapi-crud-postgres.git
    cd fastapi-crud-postgres
    ```

2. Create and activate a virtual environment:
    ```
    python -m venv venv
    venv\Scripts\activate    # For Windows
    source venv/bin/activate # For Linux or MacOS
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Set up your `.env` file with your database connection string:
    ```
    DATABASE_URL=postgresql://your_username:your_password@localhost:5432/your_database_name
    ```

5. Run the application:
    ```
    uvicorn main:app --reload
    ```

6. Access the API documentation:
    - Swagger UI: http://127.0.0.1:8000/docs
    - ReDoc: http://127.0.0.1:8000/redoc

This project was created by Smokecigarette2. It can be used for learning how to structure a basic FastAPI project with database support.
