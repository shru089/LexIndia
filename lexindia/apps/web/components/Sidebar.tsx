'use client';

import React from 'react';

import styles from './Sidebar.module.css';

type NavItem = {
  label: string;
  href: string;
  index: string;
  description: string;
};

const NAV_ITEMS: NavItem[] = [
  { label: 'Mission', href: '#mission', index: '01', description: 'Positioning and public-sector fit' },
  { label: 'Research', href: '#search', index: '02', description: 'Search, retrieval, and analysis' },
  { label: 'Operations', href: '#operations', index: '03', description: 'Workflow and matter coordination' },
  { label: 'Governance', href: '#governance', index: '04', description: 'Readiness, controls, and statute mapping' },
];

const Sidebar = () => {
  return (
    <aside className={`${styles.sidebar} glass`}>
      <div className={styles.brandBlock}>
        <p className={styles.brandEyebrow}>LexIndia</p>
        <h1>Legal intelligence for public institutions</h1>
        <p className={styles.brandSummary}>
          A single workspace for legal research, document review, and operational follow-through.
        </p>
      </div>

      <nav className={styles.nav} aria-label="Primary">
        <ul role="list">
          {NAV_ITEMS.map((item) => (
            <li key={item.label}>
              <a href={item.href} className={styles.navItem}>
                <span className={styles.navIndex}>{item.index}</span>
                <span className={styles.navCopy}>
                  <strong>{item.label}</strong>
                  <small>{item.description}</small>
                </span>
              </a>
            </li>
          ))}
        </ul>
      </nav>

      <div className={styles.footer}>
        <div className={styles.statusCard}>
          <span className={styles.statusDot} aria-hidden="true" />
          <div>
            <strong>Pilot environment</strong>
            <small>Search, workflows, and analysis are live in demo mode.</small>
          </div>
        </div>
      </div>
    </aside>
  );
};

export default Sidebar;
