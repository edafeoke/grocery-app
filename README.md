# Grocery App

This is a simple grocery app built with FastAPI.

## Setup

1. Install dependencies:
    ```bash
    pip install fastapi sqlalchemy "passlib[bcryt]"
    ```

2. Run the application:
    ```bash
    uvicorn app.main:app --reload
    ```

## Endpoints

- `GET /items/`: Get all items
- `POST /items/`: Create a new item
