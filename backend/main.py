from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok", "time": str(datetime.utcnow())}

@app.get("/api1")
def api1():
    return {"message": "Hello from API1"}

@app.get("/api2")
def api2():
    return {"internal": "Secret API", "time": str(datetime.utcnow())}
