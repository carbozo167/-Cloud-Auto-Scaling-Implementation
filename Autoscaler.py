import time
from config.settings import *
from app.metrics import get_cpu_usage, get_memory_usage, get_queue_length

class AutoScaler:
    def __init__(self):
        self.instances = 2
        self.last_scale_time = time.time()

    def evaluate(self):
        cpu = get_cpu_usage()
        mem = get_memory_usage()
        queue = get_queue_length()

        print(f"CPU: {cpu}%, MEM: {mem}%, QUEUE: {queue}")

        now = time.time()

        # SCALE UP
        if ((cpu > CPU_SCALE_UP and mem > MEMORY_SCALE_UP) or queue > QUEUE_SCALE_UP):
            if now - self.last_scale_time > SCALE_UP_COOLDOWN:
                self.scale_up()

        # SCALE DOWN
        elif ((cpu < CPU_SCALE_DOWN and mem < MEMORY_SCALE_DOWN) and queue < QUEUE_SCALE_DOWN):
            if now - self.last_scale_time > SCALE_DOWN_COOLDOWN:
                self.scale_down()

    def scale_up(self):
        if self.instances < MAX_INSTANCES:
            self.instances += 1
            self.last_scale_time = time.time()
            print(f"⬆ Scaling UP → Instances: {self.instances}")

    def scale_down(self):
        if self.instances > MIN_INSTANCES:
            self.instances -= 1
            self.last_scale_time = time.time()
            print(f"⬇ Scaling DOWN → Instances: {self.instances}")
