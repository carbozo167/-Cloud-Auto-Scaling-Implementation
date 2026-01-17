# Cloud Auto-Scaling Microservice

## Overview
This project demonstrates a microservice with **auto-scaling logic** based on:
- CPU utilization
- Memory usage
- Request queue length

Scaling thresholds, cooldown periods, and cost efficiency are simulated.

## Features
- Built with **FastAPI**
- Uses **psutil** for CPU/memory metrics
- Simulates traffic spikes and scaling decisions
- Adjustable thresholds and cooldowns

## Run Locally
```bash
pip install fastapi uvicorn psutil
uvicorn app:app --reload
