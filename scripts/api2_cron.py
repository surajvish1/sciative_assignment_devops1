import requests
from datetime import datetime

LOG_FILE = "/logs/api2.log"

try:
    res = requests.get("http://127.0.0.1/api2")
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {res.text}\n")
except Exception as e:
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - ERROR: {str(e)}\n")
