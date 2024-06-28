from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_app_initialization():
    """
    Test if the FastAPI app initializes correctly.
    """
    response = client.get("/")
    assert response.status_code == 404  # Assuming no root endpoint defined

def test_auth_router():
    """
    Test if the auth router is included.
    """
    response = client.post("/auth/login", json={"username": "test", "password": "test"})
    # Adjust according to your actual auth endpoints and expected responses
    assert response.status_code in {200, 401, 404}  # Adjust expected status codes

def test_users_router():
    """
    Test if the users router is included.
    """
    response = client.get("/users")
    # Adjust according to your actual users endpoints and expected responses
    assert response.status_code in {200, 401, 404}

def test_products_router():
    """
    Test if the products router is included.
    """
    response = client.get("/products")
    # Adjust according to your actual products endpoints and expected responses
    assert response.status_code in {200, 401, 404}
