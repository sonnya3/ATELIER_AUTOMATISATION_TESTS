import requests
import time

def call_agify(name="michael"):
    url = f"https://api.agify.io?name={name}"
    start_time = time.time()
    try:
        response = requests.get(url, timeout=10)
        latency = round(time.time() - start_time, 3)
        return response, latency
    except Exception as e:
        return None, 0
