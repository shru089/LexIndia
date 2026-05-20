'use client';
import React from 'react';
import styles from './Sidebar.module.css';

type NavItem = {
  label: string;
  href: string;
  icon: string;
};

const NAV_ITEMS: NavItem[] = [
  { label: 'Research', href: '/', icon: '⚖' },
  { label: 'Documents', href: '/documents', icon: '📄' },
  { label: 'Workflows', href: '/workflows', icon: '⚙' },
  { label: 'Analytics', href: '/analytics', icon: '📊' },
  { label: 'Library', href: '/library', icon: '📚' },
];

const Sidebar = () => {
  // Minimal active detection without router dependency
  const currentPath = typeof window !== 'undefined' ? window.location.pathname : '/';

  return (
    <aside className={`${styles.sidebar} glass`} aria-label="Main Navigation">
      <div className={styles.logo}>
        <h1>LEX<span>INDIA</span></h1>
        <p className={styles.logoTagline}>Legal Intelligence</p>
      </div>

      <nav className={styles.nav} aria-label="Primary">
        <ul role="list">
          {NAV_ITEMS.map((item) => {
            const isActive = currentPath === item.href;
            return (
              <li key={item.label}>
                <a
                  href={item.href}
                  className={`${styles.navItem} ${isActive ? styles.active : ''}`}
                  aria-current={isActive ? 'page' : undefined}
                >
                  <span className={styles.navIcon} aria-hidden="true">{item.icon}</span>
                  <span>{item.label}</span>
                </a>
              </li>
            );
          })}
        </ul>
      </nav>

      <div className={styles.footer}>
        <div className={styles.profile}>
          <div className={styles.avatar} aria-hidden="true">
            <span>SC</span>
          </div>
          <div className={styles.profileInfo}>
            <span className={styles.profileName}>Senior Counsel</span>
            <span className={styles.profileRole}>Bar ID: ****</span>
          </div>
        </div>
      </div>
    </aside>
  );
};

export default Sidebar;
