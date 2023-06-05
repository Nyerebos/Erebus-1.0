import datetime

def log_conversation(event_type, message):
    with open('conversation_log.txt', 'a') as log_file:
        timestamp = datetime.datetime.now()
        log_file.write(f"[{timestamp}] {event_type}: {message}\n")
