---
id: brute-force
title: Brute Force Attack
sidebar_position: 3
---

# 🔑 Brute Force Attack

A brute-force (or dictionary) attack systematically tries credentials from a list until one works. It requires no understanding of the target application — just time and a good wordlist.

---

## How It Works

```python title="Simplified attack logic"
for password in wordlist:
    if login(target_user, password):
        print(f"Cracked: {password}")
        break
```

The attacker doesn't exploit a code vulnerability — they exploit **weak passwords** and the absence of rate limiting.

### The Wordlist

Real-world attackers use lists of billions of leaked credentials. The most famous is **RockYou** — 14 million real passwords from a 2009 breach — freely available in most penetration testing distributions.

CyberSim's simulator uses a condensed list of the most common passwords:

| # | Password | # | Password |
|---|---|---|---|
| 1 | `password` | 9 | `master` |
| 2 | `123456` | 10 | `dragon` |
| 3 | `admin` | 11 | `sunshine` |
| 4 | `letmein` | 12 | `princess` |
| 5 | `password123` | 13 | `welcome` |
| 6 | `qwerty` | 14 | `shadow` |
| 7 | `abc123` | 15 | `superman` |
| 8 | `monkey` | | |

All three target account passwords are somewhere in this list.

---

## Target Accounts

| Account | Password | Location in wordlist |
|---|---|---|
| `admin` | `password123` | Position 5 |
| `alice` | `letmein` | Position 4 |
| `bob` | `shadow` | Position 14 |

Try all three to unlock the **Full Compromise** achievement.

---

## The Terminal Visualizer

After running a simulation, each attempt animates into the terminal one line at a time:

```
01  admin  password   ✗ FAIL
02  admin  123456     ✗ FAIL
03  admin  admin      ✗ FAIL
04  admin  letmein    ✗ FAIL
05  admin  password123  ✓ CRACKED
```

The matched password is also highlighted in the wordlist grid below the terminal.

---

## Scoring

| Achievement | Condition | Points |
|---|---|---|
| First Strike | Run any simulation | +10 |
| Admin Owned | Crack `admin` account | +35 |
| Alice Owned | Crack `alice` account | +35 |
| Bob Owned | Crack `bob` account | +35 |
| Full Compromise | Crack all three | +20 bonus |
| BF Scholar | Read the defense guide | +15 |

Maximum: **100 pts** (capped)

---

## Defenses

### Rate Limiting

Limit the number of login attempts per IP per time window. In Flask:

```python title="Flask-Limiter"
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(app, key_func=get_remote_address)

@app.route('/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    ...
```

After 5 failed attempts in a minute, the endpoint returns `429 Too Many Requests`.

---

### Account Lockout

Lock the account after N consecutive failures:

```python title="Pseudo-implementation"
if failed_attempts[username] >= 5:
    return "Account locked. Contact support.", 403
```

:::warning Lockout trade-off
Aggressive lockout policies can be abused as a **Denial of Service** — an attacker could lock every account on the platform by triggering failures. Balance lockout threshold against user experience and DoS risk.
:::

---

### Multi-Factor Authentication (MFA)

Even a cracked password is useless if the attacker also needs:

- A TOTP code (Google Authenticator, Authy)
- An SMS/email OTP
- A hardware key (YubiKey)

MFA is the **single most effective** defense against credential-based attacks.

---

### CAPTCHA

A CAPTCHA challenge after a threshold of failed attempts blocks automated scripts:

```python
from flask_recaptcha import ReCaptcha
recaptcha = ReCaptcha(app)

@app.route('/login', methods=['POST'])
def login():
    if failed_attempts > 3 and not recaptcha.verify():
        return "CAPTCHA required", 403
    ...
```

---

### Strong Passwords

The real root cause is weak passwords. A password like `shadow` falls on attempt 14. A randomly generated 20-character password would take billions of years to crack.

| Password | Time to crack (offline, GPU) |
|---|---|
| `shadow` | < 1 millisecond |
| `password123` | < 1 millisecond |
| `j9#Kx$mL2!pQr7vN&sZ` | Billions of years |

Use a **password manager** (Bitwarden, 1Password, KeePass) to generate and store unique passwords for every service.

---

## Defense Summary

| Defense | Stops | Complexity |
|---|---|---|
| Rate limiting | Automated attacks | Low |
| Account lockout | Sustained attacks | Low |
| CAPTCHA | Automated scripts | Medium |
| MFA / 2FA | Even cracked passwords | Medium |
| Strong passwords | Makes cracking infeasible | Low (with a password manager) |
| Credential breach monitoring | Reused/leaked passwords | Low |

---

## Further Reading

- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [NIST Password Guidelines (SP 800-63B)](https://pages.nist.gov/800-63-3/sp800-63b.html)
- [Have I Been Pwned](https://haveibeenpwned.com) — check if credentials have appeared in known breaches
- [PortSwigger Authentication Labs](https://portswigger.net/web-security/authentication)
