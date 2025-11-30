
#!/usr/bin/env python3

import psutil
import time

# Predefined CPU usage threshold
THRESHOLD = 80  # in percentage

def monitor_cpu(threshold):
    print("Monitoring CPU usage... Press Ctrl+C to stop.")
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)  # Check every second
            if cpu_usage > threshold:
                print(f"⚠️ Alert! CPU usage exceeds threshold: {cpu_usage}%")
            else:
                print(f"CPU usage: {cpu_usage}%")
            time.sleep(1)  # Optional: add delay for readability
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    monitor_cpu(THRESHOLD)
