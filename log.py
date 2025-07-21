from datetime import datetime
import logging

def log_process(message,log_file = "log_file.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"{timestamp} - {message}\n"
    with open(log_file, "a") as file:
        file.write(log_message)
