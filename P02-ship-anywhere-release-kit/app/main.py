from fastapi import FastAPI

app = FastAPI(
    title="Ship Anywhere API",
    description="Production-style application for P02",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "Ship Anywhere API is running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@app.get("/products")
def get_products():
    return [
        {"id": 101, "name": "Laptop", "price": 55000},
        {"id": 102, "name": "Mobile", "price": 25000},
        {"id": 103, "name": "Headphones", "price": 2000}
    ]