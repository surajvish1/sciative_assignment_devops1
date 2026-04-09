from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok", "time": datetime.utcnow()}

@app.get("/api1")
def public_api():
    return {"message": "Hello from API1"}

@app.get("/api2")
def internal_api():
    return {"internal": "This is API2", "time": datetime.utcnow()}
