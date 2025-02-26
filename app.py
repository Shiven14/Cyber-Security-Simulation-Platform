vfrom flask import Flask, render_template, request, session
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Sample user data (Insecure: Simulating a real-world vulnerability scenario)
users = {
    "admin": {
        "password": "password123",  # Intentionally weak for brute-force simulation
        "score": 0
    }
}

@app.route('/')
def home():
    return render_template('index.html')

# Simulated SQL Injection vulnerability
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Simulated vulnerable authentication (not using parameterized queries)
    if username in users and users[username]['password'] == password:
        session['user'] = username
        return render_template('dashboard.html', message="Login successful!", score=users[username]['score'])
    else:
        return render_template('index.html', message="Invalid credentials or possible SQL injection detected.")

# Simulated XSS vulnerability
@app.route('/comment', methods=['POST'])
def comment():
    user_comment = request.form['comment']
    return render_template('dashboard.html', message=f"User Comment: {user_comment}", score=session.get('user', 0))

# Brute-force attack simulation (naive approach)
@app.route('/brute_force', methods=['POST'])
def brute_force():
    attempts = request.form['attempts']
    if int(attempts) > 5:
        return render_template('dashboard.html', message="Too many failed attempts. You are locked out!", score=session.get('user', 0))
    return render_template('dashboard.html', message=f"Attempt {attempts}: Try again!", score=session.get('user', 0))

if __name__ == '__main__':
