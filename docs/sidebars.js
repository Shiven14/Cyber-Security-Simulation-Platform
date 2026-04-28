/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  mainSidebar: [
    {
      type: 'doc',
      id: 'intro',
      label: '🔒 Introduction',
    },
    {
      type: 'doc',
      id: 'getting-started',
      label: '🚀 Getting Started',
    },
    {
      type: 'category',
      label: '⚔️ Challenges',
      collapsed: false,
      items: [
        {
          type: 'doc',
          id: 'challenges/sql-injection',
          label: '💉 SQL Injection',
        },
        {
          type: 'doc',
          id: 'challenges/xss',
          label: '📜 Cross-Site Scripting',
        },
        {
          type: 'doc',
          id: 'challenges/brute-force',
          label: '🔑 Brute Force',
        },
      ],
    },
    {
      type: 'doc',
      id: 'scoring',
      label: '🏆 Scoring & Ranks',
    },
    {
      type: 'doc',
      id: 'security',
      label: '⚠️ Security Disclaimer',
    },
  ],
};

module.exports = sidebars;
