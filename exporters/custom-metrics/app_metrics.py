from prometheus_client import start_http_server, Gauge
import random
import time

# Define a custom metric
REQUEST_TIME = Gauge('app_request_processing_seconds', 'Time spent processing request')

def process_request():
    """Simulate request processing time"""
    duration = random.uniform(0.1, 2.0)
    REQUEST_TIME.set(duration)
    time.sleep(duration)

if __name__ == '__main__':
    # Start the Prometheus metrics server on port 8000
    start_http_server(8000)
    print("Custom metrics exporter running on port 8000")
    
    while True:
        process_request()
