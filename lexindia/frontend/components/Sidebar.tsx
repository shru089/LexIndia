import React from 'react';
import styles from './Sidebar.module.css';

const Sidebar = () => {
  return (
    <aside className={`${styles.sidebar} glass`}>
      <div className={styles.logo}>
        <h1>LEX<span>INDIA</span></h1>
      </div>
      <nav className={styles.nav}>
        <ul>
          <li className={styles.active}>Research</li>
          <li>Documents</li>
          <li>Workflows</li>
          <li>Analytics</li>
          <li>Library</li>
        </ul>
      </nav>
      <div className={styles.footer}>
        <div className={styles.profile}>
          <div className={styles.avatar}></div>
          <span>Senior Counsel</span>
        </div>
      </div>
    </aside>
  );
};

export default Sidebar;
