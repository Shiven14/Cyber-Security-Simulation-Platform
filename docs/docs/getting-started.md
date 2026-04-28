---
id: getting-started
title: Getting Started
sidebar_position: 2
---

# 🚀 Getting Started

Get CyberSim running locally in under two minutes.

---

## Prerequisites

| Requirement | Minimum Version |
|---|---|
| Python | 3.8+ |
| pip3 | any recent version |
| A modern browser | Chrome, Firefox, Safari, Edge |

No Docker, no cloud accounts, no paid services required.

---

## Installation

### 1 — Clone the repository

```bash
git clone https://github.com/Shiven14/Cyber-Security-Simulation-Platform.git
cd Cyber-Security-Simulation-Platform
```

### 2 — (Recommended) Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate       # macOS / Linux
# venv\Scripts\activate        # Windows
```

### 3 — Install dependencies

```bash
pip3 install -r requirements.txt
```

`requirements.txt` contains only one package: `flask>=2.3.0`

### 4 — Start the server

```bash
python3 app.py
```

You should see:

```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### 5 — Open the lab

Navigate to **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your browser.

Enter any hacker alias on the login screen — no password required. You'll land on the dashboard.

---

## Project Structure

```
Cyber-Security-Simulation-Platform/
├── app.py                  # Flask routes, scoring logic, SQLite init
├── config.py               # SECRET_KEY, DB_PATH, DEBUG flag
├── utils.py                # Logging, sanitization, XSS pattern detection
├── requirements.txt        # Flask only
│
├── templates/
│   ├── base.html           # Shared layout — navbar, toast system, global JS
│   ├── index.html          # Login / landing page with matrix rain
│   ├── dashboard.html      # Score overview, challenge cards, achievements
│   ├── sql_injection.html  # SQLi challenge with live query preview
│   ├── xss.html            # XSS challenge — split vulnerable / secure view
│   └── brute_force.html    # Brute-force with animated terminal log
│
├── static/
│   └── styles.css          # Dark glassmorphism theme, all animations
│
├── docs/                   # This Docusaurus site
│
├── demo.db                 # Created on first run (gitignored)
└── brute_force_attempts.log # Created when BF challenge is used (gitignored)
```

---

## Files Created at Runtime

| File | Created By | Contents |
|---|---|---|
| `demo.db` | `app.py` on startup | SQLite DB with 3 demo user accounts |
| `brute_force_attempts.log` | Brute-force challenge | Plain-text log of every simulated attempt |

Both files are listed in `.gitignore` and will never be committed.

---

## Resetting the Lab

To reset scores and achievements, click **Logout** in the navbar — all session data is cleared.

To reset the SQLite demo database, restart the server (`Ctrl+C` then `python3 app.py` again). The `init_db()` function truncates and re-seeds the `demo_users` table on every start.

---

## Running the Docs Site

```bash
cd docs
npm install
npm start          # Dev server at http://localhost:3000
npm run build      # Production build → docs/build/
```

---

## Stopping the Server

Press `Ctrl+C` in the terminal where `python3 app.py` is running.

---

## Next Step

Head to the [SQL Injection challenge →](./challenges/sql-injection.md) — it's the best starting point.
