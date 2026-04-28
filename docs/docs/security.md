---
id: security
title: Security Disclaimer
sidebar_position: 5
---

# ⚠️ Security Disclaimer

:::danger Important — Read Before Using
This project contains **intentionally vulnerable code**. It is designed exclusively for educational use in a controlled local environment.
:::

---

## Intended Use

CyberSim is built for:

- **Students** learning web application security fundamentals
- **Developers** who want to understand common vulnerability classes before they appear in production code
- **Security professionals** looking for a quick local demo environment
- **Educators** teaching offensive and defensive security concepts

---

## What Is Safe

| ✅ Safe | ❌ Not Safe |
|---|---|
| Running against `localhost` / `127.0.0.1` | Deploying to a public server |
| Using the built-in demo database | Connecting to real databases |
| Practicing payloads in the challenge UI | Using payloads against external systems |
| Learning the defense techniques shown | Ignoring the defense techniques shown |

---

## What the Vulnerabilities Are

Every vulnerability in CyberSim is:

1. **Intentional** — the code is deliberately written insecurely for demonstration
2. **Isolated** — all data lives in a local SQLite file (`demo.db`) that is reset on every server restart
3. **Contained** — no part of the application connects to external networks, APIs, or services
4. **Documented** — each vulnerability is paired with an explanation and secure alternative

The production-ready, secure equivalents are shown side-by-side in every challenge's defense panel.

---

## Legal Notice

> Using SQL injection, XSS, brute-force attacks, or any other exploitation technique against a web application, system, or network **without explicit written authorization from the owner** is illegal in most jurisdictions, including under:
>
> - The **Computer Fraud and Abuse Act (CFAA)** — United States
> - The **Computer Misuse Act 1990** — United Kingdom
> - The **Criminal Code** — Canada
> - The **Cybercrime Convention** — European Union
>
> Violations can result in criminal prosecution, civil liability, and significant financial penalties.

---

## Responsible Disclosure

If you discover a security vulnerability in a real application, follow responsible disclosure practices:

1. **Do not exploit** the vulnerability beyond what is needed to confirm it exists
2. **Contact the vendor** through their security disclosure channel (look for `security.txt` or a bug bounty program)
3. **Allow reasonable time** (typically 90 days) for the vendor to patch before publishing
4. **Report publicly** only after a fix has been deployed or the disclosure window has passed

Resources:
- [Google Project Zero Disclosure Policy](https://googleprojectzero.blogspot.com/p/vulnerability-disclosure-policy.html)
- [CERT/CC Vulnerability Reporting](https://www.kb.cert.org/vuls/report/)
- [HackerOne Responsible Disclosure](https://www.hackerone.com/disclosure-guidelines)

---

## No Liability

The authors and contributors of CyberSim accept **no responsibility or liability** for any misuse of this software. By using this project, you agree that:

- You will only use these techniques in environments you own or have explicit written permission to test
- You understand that intentional exploitation of real systems without authorization is illegal
- You accept full responsibility for any consequences arising from your use of this software

---

## Reporting Issues

If you find a bug or have a concern about this project, please open an issue on [GitHub](https://github.com/Shiven14/Cyber-Security-Simulation-Platform/issues).
