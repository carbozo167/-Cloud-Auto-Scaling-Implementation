
import psutil
import random

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_queue_length():
    # Simulated request queue
    return random.randint(10, 120)
