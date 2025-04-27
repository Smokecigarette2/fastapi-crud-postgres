# FastAPI CRUD API with PostgreSQL

This project is a simple CRUD (Create, Read, Update, Delete) API built using FastAPI, SQLAlchemy, and PostgreSQL.  
It allows users to create, read, update, and delete user records stored in a PostgreSQL database.  
The application supports environment configuration using a `.env` file and can be run locally or containerized using Docker.

## Project Structure
- `main.py`: Defines the FastAPI app and API endpoints.
- `models.py`: Defines SQLAlchemy models for the database tables.
- `schemas.py`: Defines Pydantic models for request and response validation.
- `database.py`: Configures the PostgreSQL database connection.
- `requirements.txt`: Lists the Python dependencies.
- `.env`: Stores sensitive information like the database URL.

## How to run locally

1. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Set up your PostgreSQL database and configure your `.env` file:

    Example `.env` file:
    ```
    DATABASE_URL=postgresql://your_username:your_password@localhost:5432/your_database_name
    ```

3. Run the FastAPI application:
    ```
    uvicorn main:app --reload
    ```

4. Access the API documentation:
    - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
    - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Technologies used
- FastAPI
- SQLAlchemy
- PostgreSQL
- Uvicorn
- Pydantic
- Docker (optional for containerization)

## Author
Created by [Smokecigarette2](https://github.com/Smokecigarette2)
