import re
import html


def log_attempt(attempt_info):
    with open("brute_force_attempts.log", "a") as log_file:
        log_file.write(f"Brute-force attempt: {attempt_info}\n")


def sanitize_input(text):
    return html.escape(text)


def detect_xss_pattern(text):
    patterns = [
        r'<script[^>]*>',
        r'on\w+\s*=',
        r'javascript:',
        r'<iframe',
        r'<img[^>]+onerror',
    ]
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False
