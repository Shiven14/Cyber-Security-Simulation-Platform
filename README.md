Cyber Security Simulation Platform

Project Structure:

cyber-security-sim/
│── app.py              # Main Flask application
│── templates/
│   ├── index.html      # Login page
│   ├── dashboard.html  # Dashboard with user interactions
│── static/
│   ├── styles.css      # CSS for UI styling
│── requirements.txt    # Dependencies (Flask, etc.)
│── README.md           # Project description and setup instructions
│── .gitignore          # Ignore unnecessary files in Git
│── utils.py            # Utility functions
│── config.py           # Configuration settings

README.md

# Cyber Security Simulation Platform

## Overview
This project is a hands-on cybersecurity simulation platform that enables users to practice real-world threat scenarios, including SQL Injection, Cross-Site Scripting (XSS), and brute-force attacks.

## Features
- Simulated **SQL Injection** vulnerabilities
- **XSS** attack demonstration
- **Brute-force attack** simulation
- A **scoring system** to assess user responses and learning
- **Flask-based web application** with an intuitive dashboard
- **AWS deployable** for scalability and security

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/cyber-security-sim.git
    cd cyber-security-sim
    ```
2. Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    python app.py
    ```
4. Access the web application at `http://127.0.0.1:5000`

## File Structure
```
cyber-security-sim/
│── app.py              # Main Flask application
│── templates/
│   ├── index.html      # Login page
│   ├── dashboard.html  # Dashboard with user interactions
│── static/
│   ├── styles.css      # CSS for UI styling
│── requirements.txt    # Dependencies (Flask, etc.)
│── README.md           # Project description and setup instructions
│── .gitignore          # Ignore unnecessary files in Git
│── utils.py            # Utility functions
│── config.py           # Configuration settings
```

## Security Disclaimer
This project is for **educational purposes only**. The vulnerabilities demonstrated are intentional and should not be used for malicious purposes. Always apply security best practices when developing web applications.

## License
MIT License
