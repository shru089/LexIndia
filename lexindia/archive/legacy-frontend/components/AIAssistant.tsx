import React from 'react';
import styles from './AIAssistant.module.css';

const AIAssistant = () => {
  return (
    <div className={`${styles.assistant} glass`}>
      <div className={styles.header}>
        <div className={styles.indicator}></div>
        <span>AI Research Associate</span>
      </div>
      <div className={styles.content}>
        <p>Welcome, Counsel. How can I assist with your research today?</p>
      </div>
      <div className={styles.inputArea}>
        <input type="text" placeholder="Ask LexIndia..." />
      </div>
    </div>
  );
};

export default AIAssistant;
