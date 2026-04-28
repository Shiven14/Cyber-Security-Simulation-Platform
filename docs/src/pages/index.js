import React from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';

const FEATURES = [
  {
    icon: '💉',
    iconClass: 'icon-red',
    cardClass: 'feature-card-red',
    linkClass: 'feature-link-red',
    title: 'SQL Injection',
    desc: 'Exploit a live SQLite database through a vulnerable login form. Practice OR-based bypasses, comment injection, and UNION attacks against real query results.',
    to: '/docs/challenges/sql-injection',
  },
  {
    icon: '📜',
    iconClass: 'icon-amber',
    cardClass: 'feature-card-amber',
    linkClass: 'feature-link-amber',
    title: 'Cross-Site Scripting',
    desc: 'Inject scripts into a vulnerable comment board. Steal cookies, hijack the DOM, and see live side-by-side secure vs. vulnerable rendering.',
    to: '/docs/challenges/xss',
  },
  {
    icon: '🔑',
    iconClass: 'icon-blue',
    cardClass: 'feature-card-blue',
    linkClass: 'feature-link-blue',
    title: 'Brute Force',
    desc: 'Run a simulated dictionary attack against three target accounts. Watch each attempt animate in a real terminal — then read the defenses.',
    to: '/docs/challenges/brute-force',
  },
  {
    icon: '🏆',
    iconClass: 'icon-green',
    cardClass: 'feature-card-green',
    linkClass: 'feature-link-green',
    title: 'Scoring & Ranks',
    desc: '300 points across three challenges. Unlock 15 achievement badges and climb from Newbie to Elite Hacker as your skills grow.',
    to: '/docs/scoring',
  },
];

const STACK = [
  'Python 3', 'Flask', 'SQLite', 'Vanilla JS',
  'Inter Font', 'JetBrains Mono', 'CSS Glassmorphism', 'Docusaurus',
];

export default function Home() {
  const { siteConfig } = useDocusaurusContext();

  return (
    <Layout title="Home" description={siteConfig.tagline}>

      {/* ── Hero ── */}
      <section className="hero-section">
        <div>
          <div className="hero-tag">
            🔒 v1.0.0 · Open Source · Free to Use
          </div>

          <h1 className="hero-title">
            Cybersecurity<br />Attack &amp; Defense Lab
          </h1>

          <p className="hero-subtitle">
            Practice real-world web vulnerabilities hands-on — SQL injection, XSS,
            and brute-force attacks — in a fully isolated local environment.
            No cloud accounts. No cost.
          </p>

          <div className="hero-actions">
            <Link className="btn-hero-primary" to="/docs/getting-started">
              🚀 Get Started
            </Link>
            <Link className="btn-hero-secondary" to="/docs/intro">
              📖 Read the Docs
            </Link>
            <a
              className="btn-hero-secondary"
              href="https://github.com/Shiven14/Cyber-Security-Simulation-Platform"
              target="_blank"
              rel="noopener noreferrer"
            >
              ⭐ GitHub
            </a>
          </div>

          <div className="hero-stats">
            <div className="hero-stat">
              <div className="hero-stat-num">3</div>
              <div className="hero-stat-lbl">Challenges</div>
            </div>
            <div className="hero-stat">
              <div className="hero-stat-num">300</div>
              <div className="hero-stat-lbl">Total Points</div>
            </div>
            <div className="hero-stat">
              <div className="hero-stat-num">15</div>
              <div className="hero-stat-lbl">Achievements</div>
            </div>
            <div className="hero-stat">
              <div className="hero-stat-num">$0</div>
              <div className="hero-stat-lbl">Cost</div>
            </div>
          </div>
        </div>
      </section>

      {/* ── Features ── */}
      <section className="features-section">
        <h2 className="features-heading">Everything in One Lab</h2>
        <p className="features-subheading">
          Each challenge pairs an exploitable demo with a side-by-side defense guide.
        </p>
        <div className="features-grid">
          {FEATURES.map((f) => (
            <div key={f.title} className={`feature-card ${f.cardClass}`}>
              <div className={`feature-icon ${f.iconClass}`}>{f.icon}</div>
              <h3>{f.title}</h3>
              <p>{f.desc}</p>
              <Link className={`feature-link ${f.linkClass}`} to={f.to}>
                View docs →
              </Link>
            </div>
          ))}
        </div>
      </section>

      {/* ── Stack ── */}
      <section className="stack-section">
        <h2 style={{ fontSize: '1.5rem', fontWeight: 800, color: '#f1f5f9', marginBottom: '0.4rem' }}>
          Built with zero paid dependencies
        </h2>
        <p style={{ color: '#475569', fontSize: '0.9rem' }}>
          Runs entirely on your machine — no AWS, no Docker, no subscriptions.
        </p>
        <div className="stack-chips">
          {STACK.map((s) => (
            <span key={s} className="stack-chip">{s}</span>
          ))}
        </div>
      </section>

    </Layout>
  );
}
