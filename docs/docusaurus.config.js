// @ts-check
const { themes } = require('prism-react-renderer');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'CyberSim',
  tagline: 'Cybersecurity Attack & Defense Lab — Learn by doing.',
  favicon: 'img/favicon.svg',

  url: 'https://shiven14.github.io',
  baseUrl: '/Cyber-Security-Simulation-Platform/',

  organizationName: 'Shiven14',
  projectName: 'Cyber-Security-Simulation-Platform',
  trailingSlash: false,

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/Shiven14/Cyber-Security-Simulation-Platform/edit/main/docs/',
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        defaultMode: 'dark',
        disableSwitch: false,
        respectPrefersColorScheme: false,
      },

      image: 'img/social-card.png',

      navbar: {
        title: 'CyberSim',
        logo: {
          alt: 'CyberSim Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'mainSidebar',
            position: 'left',
            label: 'Docs',
          },
          {
            href: 'http://127.0.0.1:5000',
            label: 'Launch Lab',
            position: 'left',
          },
          {
            href: 'https://github.com/Shiven14/Cyber-Security-Simulation-Platform',
            label: 'GitHub',
            position: 'right',
          },
          {
            href: 'https://github.com/Shiven14/Cyber-Security-Simulation-Platform/releases',
            label: 'v1.0.0',
            position: 'right',
          },
        ],
      },

      footer: {
        style: 'dark',
        links: [
          {
            title: 'Documentation',
            items: [
              { label: 'Introduction', to: '/docs/intro' },
              { label: 'Getting Started', to: '/docs/getting-started' },
              { label: 'Scoring & Ranks', to: '/docs/scoring' },
            ],
          },
          {
            title: 'Challenges',
            items: [
              { label: 'SQL Injection', to: '/docs/challenges/sql-injection' },
              { label: 'Cross-Site Scripting', to: '/docs/challenges/xss' },
              { label: 'Brute Force', to: '/docs/challenges/brute-force' },
            ],
          },
          {
            title: 'Project',
            items: [
              { label: 'GitHub', href: 'https://github.com/Shiven14/Cyber-Security-Simulation-Platform' },
              { label: 'Releases', href: 'https://github.com/Shiven14/Cyber-Security-Simulation-Platform/releases' },
              { label: 'Security Disclaimer', to: '/docs/security' },
            ],
          },
        ],
        copyright: `© ${new Date().getFullYear()} Shiven Patel · CyberSim · For educational use only.`,
      },

      prism: {
        theme: themes.dracula,
        darkTheme: themes.dracula,
        additionalLanguages: ['python', 'bash', 'sql', 'json'],
      },

      announcementBar: {
        id: 'edu_disclaimer',
        content: '⚠️ <strong>Educational use only.</strong> All vulnerabilities are intentional simulations. Do not use these techniques on systems you do not own.',
        backgroundColor: '#1a1a2e',
        textColor: '#fbbf24',
        isCloseable: true,
      },
    }),
};

module.exports = config;
