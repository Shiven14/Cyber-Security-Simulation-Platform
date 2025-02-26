

def log_attempt(attempts):
    with open("brute_force_attempts.log", "a") as log_file:
        log_file.write(f"Brute-force attempt: {attempts}\n")
