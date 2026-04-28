# CyberSim — Cybersecurity Attack & Defense Lab

> An interactive, browser-based simulation platform for learning offensive security techniques through hands-on practice — safely, locally, and for free.

---

## Overview

CyberSim is a Flask-powered cybersecurity training lab that lets you practice three of the most common web attack vectors in a fully controlled environment. Every vulnerability is **intentional and isolated** — no real systems are touched. A built-in scoring system tracks your progress across challenges and awards achievements as you advance from Newbie to Elite Hacker.

---

## Features

| Module | What You Practice |
|---|---|
| **SQL Injection** | Auth bypass, comment injection (`--`), `OR`-based attacks, `UNION` data extraction |
| **Cross-Site Scripting (XSS)** | `<script>` injection, `onerror` events, `document.cookie` theft, DOM manipulation |
| **Brute Force** | Simulated dictionary attacks, real-time attempt logging, wordlist analysis |
| **Scoring System** | 100 pts per category (300 total), rank progression, achievement badges |
| **Defense Education** | Every challenge includes a side-by-side secure code comparison and defense guide |

---

## Tech Stack

- **Backend** — Python 3, Flask, SQLite
- **Frontend** — Vanilla JS, Inter + JetBrains Mono (Google Fonts), CSS glassmorphism
- **No paid services** — runs entirely on your machine, zero external dependencies at runtime

---

## Getting Started

### Prerequisites

- Python 3.8+
- `pip3`

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/cyber-security-sim.git
cd cyber-security-sim

# 2. (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows

# 3. Install dependencies
pip3 install -r requirements.txt

# 4. Start the server
python3 app.py
```

Open **http://127.0.0.1:5000** in your browser.

---

## Project Structure

```
cyber-security-sim/
├── app.py                  # Flask routes, scoring logic, SQLite demo DB
├── config.py               # Secret key, DB path
├── utils.py                # Logging, input sanitization, XSS detection
├── requirements.txt        # Python dependencies (Flask only)
│
├── templates/
│   ├── base.html           # Shared navbar, toast system, global JS
│   ├── index.html          # Login / landing page
│   ├── dashboard.html      # Score overview, challenge cards, achievements
│   ├── sql_injection.html  # SQLi challenge with live query preview
│   ├── xss.html            # XSS challenge with split vulnerable/secure view
│   └── brute_force.html    # Brute-force challenge with animated terminal
│
├── static/
│   └── styles.css          # Dark glassmorphism theme, animations
│
├── demo.db                 # SQLite DB created on first run (gitignored)
└── README.md
```

---

## Scoring

Each challenge is worth **100 points** (300 total). Points are session-based and reset on logout.

### SQL Injection (100 pts)
| Action | Points |
|---|---|
| Any successful injection | +10 |
| `OR`-based auth bypass | +20 |
| Comment-based bypass (`--`) | +30 |
| `UNION` data extraction | +50 |
| Read the defense guide | +15 |

### Cross-Site Scripting (100 pts)
| Action | Points |
|---|---|
| Basic `<script>` injection | +25 |
| `onerror` attribute exploit | +30 |
| `document.cookie` theft | +40 |
| Read the defense guide | +15 |

### Brute Force (100 pts)
| Action | Points |
|---|---|
| Run any simulation | +10 |
| Crack a single account | +35 |
| Crack all three accounts | +20 bonus |
| Read the defense guide | +15 |

---

## Demo Accounts (SQLi Target)

The demo database is seeded with three accounts for the SQL Injection challenge:

| Username | Password | Role |
|---|---|---|
| `admin` | `super_secret_pass` | admin |
| `alice` | `alice_pass` | user |
| `bob` | `bob_pass` | user |

Brute-force target passwords (`admin → password123`, `alice → letmein`, `bob → shadow`) are all present in the built-in wordlist.

---

## UI Highlights

- **Live SQL query preview** — the generated query updates character-by-character as you type, with injection points highlighted in red
- **Click-to-fill payloads** — payload table rows are clickable and auto-fill the attack form
- **Animated brute-force terminal** — each attempt line stagers in for a realistic attack visualization
- **Side-by-side XSS rendering** — vulnerable (raw HTML) and secure (escaped) views shown simultaneously
- **Toast notifications** — non-blocking score updates for every points event
- **Animated score counters** — dashboard stats count up on load

---

## Security Disclaimer

> This project is for **educational and research purposes only**.
>
> All vulnerabilities are **intentional** and contained within a local SQLite demo database. Nothing connects to external systems. Do not replicate these techniques against any application or system you do not own or have explicit written permission to test. The authors accept no liability for misuse.

---

## License

[MIT](LICENSE)
