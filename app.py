from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import sqlite3
import os
from config import SECRET_KEY, DB_PATH
from utils import log_attempt, sanitize_input, detect_xss_pattern

app = Flask(__name__)
app.secret_key = SECRET_KEY

COMMON_PASSWORDS = [
    'password', '123456', 'admin', 'letmein', 'password123',
    'qwerty', 'abc123', 'monkey', 'master', 'dragon',
    'sunshine', 'princess', 'welcome', 'shadow', 'superman'
]

TARGET_ACCOUNTS = {
    'admin': 'password123',
    'alice': 'letmein',
    'bob':   'shadow',
}


# ── Database setup ────────────────────────────────────────────────────────────

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS demo_users
                 (id INTEGER PRIMARY KEY, username TEXT, password TEXT,
                  role TEXT, secret TEXT)''')
    c.execute("DELETE FROM demo_users")
    c.executemany(
        "INSERT INTO demo_users VALUES (?, ?, ?, ?, ?)",
        [
            (1, 'admin',  'super_secret_pass', 'admin', 'FLAG{sql_injection_master}'),
            (2, 'alice',  'alice_pass',         'user',  'flag{alice_secret}'),
            (3, 'bob',    'bob_pass',            'user',  'flag{bob_secret}'),
        ]
    )
    conn.commit()
    conn.close()


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# ── Context processor – injects score into every template ────────────────────

@app.context_processor
def inject_globals():
    score = session.get('score', {'sql': 0, 'xss': 0, 'brute': 0})
    return dict(
        g_score=score,
        g_total=sum(score.values()),
        g_user=session.get('username', ''),
        g_achievements=session.get('achievements', []),
    )


# ── Auth ──────────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '').strip() or 'hacker'
    session['username'] = username
    session.setdefault('score', {'sql': 0, 'xss': 0, 'brute': 0})
    session.setdefault('achievements', [])
    session.setdefault('xss_comments', [])
    return redirect(url_for('dashboard'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


# ── Dashboard ─────────────────────────────────────────────────────────────────

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('index'))
    return render_template('dashboard.html')


# ── SQL Injection ─────────────────────────────────────────────────────────────

@app.route('/sql-injection', methods=['GET', 'POST'])
def sql_injection():
    if 'username' not in session:
        return redirect(url_for('index'))

    result, query_shown, error, points_earned = None, None, None, 0
    success = False

    if request.method == 'POST':
        username = request.form.get('sqli_user', '')
        password = request.form.get('sqli_pass', '')

        # INTENTIONALLY VULNERABLE – educational demo only
        query = (
            f"SELECT id, username, role, secret FROM demo_users "
            f"WHERE username = '{username}' AND password = '{password}'"
        )
        query_shown = query

        try:
            conn = get_db()
            rows = conn.execute(query).fetchall()
            conn.close()
            if rows:
                result = [dict(r) for r in rows]
                success = True
                points_earned = _score_sqli(username, password)
        except sqlite3.OperationalError as e:
            error = str(e)

    score = session.get('score', {'sql': 0, 'xss': 0, 'brute': 0})
    return render_template('sql_injection.html',
                           result=result, query=query_shown,
                           error=error, success=success,
                           points_earned=points_earned,
                           sql_score=score['sql'])


def _score_sqli(username, password):
    score = session.get('score', {'sql': 0, 'xss': 0, 'brute': 0})
    achievements = session.get('achievements', [])
    earned = 0
    combined = (username + password).upper()

    if 'UNION' in combined and 'sql_union' not in achievements:
        achievements.append('sql_union')
        score['sql'] = min(score['sql'] + 50, 100)
        earned += 50
    elif '--' in combined and 'sql_comment' not in achievements:
        achievements.append('sql_comment')
        score['sql'] = min(score['sql'] + 30, 100)
        earned += 30
    elif (' OR ' in combined or "OR'" in combined) and 'sql_bypass' not in achievements:
        achievements.append('sql_bypass')
        score['sql'] = min(score['sql'] + 20, 100)
        earned += 20
    elif 'sql_basic' not in achievements:
        achievements.append('sql_basic')
        score['sql'] = min(score['sql'] + 10, 100)
        earned += 10

    session['score'] = score
    session['achievements'] = achievements
    session.modified = True
    return earned


# ── XSS ───────────────────────────────────────────────────────────────────────

@app.route('/xss', methods=['GET', 'POST'])
def xss():
    if 'username' not in session:
        return redirect(url_for('index'))

    points_earned = 0
    xss_found = False

    if request.method == 'POST':
        comment = request.form.get('comment', '')
        comments = session.get('xss_comments', [])
        comments.append({'text': comment, 'author': session['username']})
        session['xss_comments'] = comments[-12:]
        session.modified = True

        if detect_xss_pattern(comment):
            xss_found = True
            points_earned = _score_xss(comment)

    score = session.get('score', {'sql': 0, 'xss': 0, 'brute': 0})
    return render_template('xss.html',
                           comments=session.get('xss_comments', []),
                           xss_found=xss_found,
                           points_earned=points_earned,
                           xss_score=score['xss'])


def _score_xss(comment):
    score = session.get('score', {'sql': 0, 'xss': 0, 'brute': 0})
    achievements = session.get('achievements', [])
    earned = 0
    lower = comment.lower()

    if ('cookie' in lower or 'document.cookie' in lower) and 'xss_cookie' not in achievements:
        achievements.append('xss_cookie')
        score['xss'] = min(score['xss'] + 40, 100)
        earned += 40
    elif 'onerror' in lower and 'xss_onerror' not in achievements:
        achievements.append('xss_onerror')
        score['xss'] = min(score['xss'] + 30, 100)
        earned += 30
    elif 'xss_basic' not in achievements:
        achievements.append('xss_basic')
        score['xss'] = min(score['xss'] + 25, 100)
        earned += 25

    session['score'] = score
    session['achievements'] = achievements
    session.modified = True
    return earned


@app.route('/xss/clear', methods=['POST'])
def xss_clear():
    session['xss_comments'] = []
    session.modified = True
    return redirect(url_for('xss'))


# ── Brute Force ───────────────────────────────────────────────────────────────

@app.route('/brute-force', methods=['GET', 'POST'])
def brute_force():
    if 'username' not in session:
        return redirect(url_for('index'))

    result, attempts_log, points_earned = None, [], 0

    if request.method == 'POST':
        target = request.form.get('target_user', 'admin')
        correct = TARGET_ACCOUNTS.get(target, '')
        found_at = None

        for i, pwd in enumerate(COMMON_PASSWORDS):
            success = (pwd == correct)
            attempts_log.append({'attempt': i + 1, 'password': pwd, 'success': success})
            log_attempt(f"target={target}, password={pwd}, success={success}")
            if success:
                found_at = i + 1
                break

        if found_at:
            result = {'cracked': True, 'password': correct, 'attempts': found_at, 'target': target}
        else:
            result = {'cracked': False, 'attempts': len(COMMON_PASSWORDS), 'target': target}

        points_earned = _score_brute(result)

    score = session.get('score', {'sql': 0, 'xss': 0, 'brute': 0})
    return render_template('brute_force.html',
                           result=result,
                           attempts_log=attempts_log,
                           points_earned=points_earned,
                           brute_score=score['brute'],
                           targets=list(TARGET_ACCOUNTS.keys()),
                           wordlist=COMMON_PASSWORDS)


def _score_brute(result):
    score = session.get('score', {'sql': 0, 'xss': 0, 'brute': 0})
    achievements = session.get('achievements', [])
    earned = 0

    target = result.get('target', '')
    ach_key = f"brute_cracked_{target}"

    if result['cracked'] and ach_key not in achievements:
        achievements.append(ach_key)
        score['brute'] = min(score['brute'] + 35, 100)
        earned += 35
        if all(f"brute_cracked_{t}" in achievements for t in TARGET_ACCOUNTS):
            if 'brute_all' not in achievements:
                achievements.append('brute_all')
                score['brute'] = min(score['brute'] + 20, 100)
                earned += 20
    elif not result['cracked'] and 'brute_attempted' not in achievements:
        achievements.append('brute_attempted')
        score['brute'] = min(score['brute'] + 10, 100)
        earned += 10

    session['score'] = score
    session['achievements'] = achievements
    session.modified = True
    return earned


# ── Learn bonus endpoint ──────────────────────────────────────────────────────

@app.route('/learn/<topic>', methods=['POST'])
def learn(topic):
    if 'username' not in session:
        return jsonify({'error': 'not logged in'}), 401

    topic_map = {'sql': ('sql_learned', 'sql'), 'xss': ('xss_learned', 'xss'), 'brute': ('brute_learned', 'brute')}
    if topic not in topic_map:
        return jsonify({'error': 'unknown topic'}), 400

    ach, key = topic_map[topic]
    score = session.get('score', {'sql': 0, 'xss': 0, 'brute': 0})
    achievements = session.get('achievements', [])
    earned = 0

    if ach not in achievements:
        achievements.append(ach)
        score[key] = min(score[key] + 15, 100)
        earned = 15
        session['score'] = score
        session['achievements'] = achievements
        session.modified = True

    return jsonify({'points_earned': earned, 'new_score': score[key], 'total': sum(score.values())})


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
