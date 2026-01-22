from fastapi import FastAPI
from app.autoscaler import AutoScaler
import threading
import time

app = FastAPI()
scaler = AutoScaler()

@app.get("/")
def home():
    return {"status": "Microservice Running"}

@app.get("/metrics")
def metrics():
    return {
        "instances": scaler.instances
    }

def auto_scaling_loop():
    while True:
        scaler.evaluate()
        time.sleep(10)

# Start autoscaling in background
threading.Thread(target=auto_scaling_loop, daemon=True).start()
