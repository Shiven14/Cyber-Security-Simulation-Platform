---
id: intro
title: Introduction
sidebar_position: 1
slug: /intro
---

# 🔒 CyberSim

**CyberSim** is an interactive, browser-based cybersecurity training lab that lets you practice three of the most common web attack vectors in a fully controlled local environment.

Every vulnerability is **intentional and isolated** — contained within a local SQLite demo database. Nothing connects to external systems.

---

## What You'll Learn

| Challenge | Attack Technique | Defense |
|---|---|---|
| **SQL Injection** | Auth bypass, `UNION` extraction, comment injection | Parameterized queries |
| **Cross-Site Scripting** | `<script>` tags, `onerror` events, cookie theft | Output encoding, CSP |
| **Brute Force** | Dictionary attacks, credential stuffing | Rate limiting, MFA, strong passwords |

---

## How It Works

1. **Open a challenge** from the dashboard
2. **Exploit the vulnerability** using the attack panel on the left — try built-in payloads or craft your own
3. **Earn points** for each successful technique
4. **Read the defense guide** on the right panel to understand how to prevent the attack
5. **Collect achievements** and climb the rank ladder

---

## Key Features

### Live SQL Query Preview
As you type in the SQL Injection form, the generated query updates character-by-character. Injection points turn **red** so you can see exactly how your input breaks out of the string literal.

### Side-by-Side XSS Rendering
The XSS challenge shows the **vulnerable** (raw HTML rendered) and **secure** (HTML-escaped) versions of every comment simultaneously — making the difference immediately obvious.

### Animated Brute-Force Terminal
Each password attempt in the brute-force simulator animates into a terminal-style log, one line at a time, for a realistic attack visualization.

### Toast Notifications & Score Counters
All point events fire non-blocking toast notifications. Dashboard statistics animate from zero on load.

---

## Architecture

```
Browser  ←→  Flask (Python)  ←→  SQLite (demo.db)
                  ↕
            Session (scores,
            achievements,
            XSS comments)
```

- The Flask server handles all routing and scoring logic
- The SQLite database is reset to a known state on every `python3 app.py` start
- All state is stored in the Flask session — no persistence between logouts

---

## Next Steps

- [Getting Started →](./getting-started.md) — install and run in under 2 minutes
- [SQL Injection →](./challenges/sql-injection.md) — start with the first challenge
- [Scoring & Ranks →](./scoring.md) — understand how points are calculated
