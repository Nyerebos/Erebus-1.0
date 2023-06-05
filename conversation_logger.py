import datetime

def log_conversation(event_type, message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"conversation_log_{timestamp}.txt"
    with open(filename, 'a') as log_file:
        log_file.write(f"[{timestamp}] {event_type}: {message}\n")
