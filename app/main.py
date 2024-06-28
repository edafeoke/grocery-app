from fastapi import FastAPI
from .routers import auth, users, products, orders
from .database import engine, Base

# Drop all tables (for development purposes)
Base.metadata.drop_all(bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)
