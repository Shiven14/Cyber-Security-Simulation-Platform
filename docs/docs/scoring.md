---
id: scoring
title: Scoring & Ranks
sidebar_position: 4
---

# 🏆 Scoring & Ranks

CyberSim tracks your progress across all three challenge modules using a session-based scoring system. Points reset when you log out.

---

## Score Overview

| Challenge | Max Points |
|---|---|
| SQL Injection | 100 |
| Cross-Site Scripting | 100 |
| Brute Force | 100 |
| **Total** | **300** |

---

## SQL Injection Scoring

| Action | Achievement Unlocked | Points |
|---|---|---|
| Any successful injection result | First Injection | +10 |
| `OR`-based auth bypass | Auth Bypass | +20 |
| `--` comment bypass | Comment Killer | +30 |
| `UNION` data extraction | UNION Master | +50 |
| Read the defense guide | SQLi Scholar | +15 |

> Points are cumulative per technique. If you use a `UNION` attack, you also get credit for the preceding techniques automatically if they haven't been awarded yet.

---

## XSS Scoring

| Action | Achievement Unlocked | Points |
|---|---|---|
| Basic `<script>` injection | Script Kiddie | +25 |
| `onerror` attribute exploit | Event Handler | +30 |
| `document.cookie` access | Cookie Monster | +40 |
| Read the defense guide | XSS Scholar | +15 |

---

## Brute Force Scoring

| Action | Achievement Unlocked | Points |
|---|---|---|
| Run any simulation | First Strike | +10 |
| Crack `admin` account | Admin Owned | +35 |
| Crack `alice` account | Alice Owned | +35 |
| Crack `bob` account | Bob Owned | +35 |
| Crack all three accounts | Full Compromise | +20 bonus |
| Read the defense guide | BF Scholar | +15 |

---

## Rank System

Your rank is calculated from your total score out of 300:

| Rank | Score Range | Description |
|---|---|---|
| ⭕ **Newbie** | 0 – 89 | Just getting started |
| ▶ **Intermediate** | 90 – 179 | Making solid progress |
| ▲ **Advanced** | 180 – 269 | Strong across multiple areas |
| ★ **Elite Hacker** | 270 – 300 | Mastered all challenges |

---

## Achievements

There are **15 achievements** in total. All are shown on the dashboard when unlocked.

### SQL Injection Achievements

| Badge | Title | How to Unlock |
|---|---|---|
| 📄 | First Injection | Any successful SQLi result |
| 🔓 | Auth Bypass | `OR`-based login bypass |
| 📝 | Comment Killer | `--` drops the password check |
| ⚠️ | UNION Master | `UNION SELECT` attack |
| 📚 | SQLi Scholar | Read the defense guide |

### XSS Achievements

| Badge | Title | How to Unlock |
|---|---|---|
| 📜 | Script Kiddie | `<script>` tag injection |
| 📷 | Event Handler | `onerror` attribute exploit |
| 🍪 | Cookie Monster | `document.cookie` payload |
| 📚 | XSS Scholar | Read the defense guide |

### Brute Force Achievements

| Badge | Title | How to Unlock |
|---|---|---|
| 🔍 | First Strike | Run any brute-force simulation |
| 🔐 | Admin Owned | Crack the `admin` account |
| 🔐 | Alice Owned | Crack the `alice` account |
| 🔐 | Bob Owned | Crack the `bob` account |
| 🎉 | Full Compromise | Crack all three accounts |
| 📚 | BF Scholar | Read the defense guide |

---

## Defense Guide Bonus

Each challenge includes a **defense guide** in the right panel. Clicking "Mark as Learned" awards **+15 points** once per topic. This is capped per-topic — clicking it twice does not double the reward.

The endpoint is:

```
POST /learn/<topic>
```

Where `<topic>` is `sql`, `xss`, or `brute`.

Response:

```json
{
  "points_earned": 15,
  "new_score": 65,
  "total": 185
}
```

---

## Technical Notes

- All scores are stored in the **Flask session** (server-side, cookie-based)
- Scores are **not persisted** — logging out clears everything
- Each achievement can only be earned **once per session**
- Score values are capped at **100 per category** — overlapping techniques don't stack beyond the cap
