'use client';
import React, { useState, useEffect } from 'react';
import Sidebar from '@/components/Sidebar';
import styles from './CaseView.module.css';

export default function CaseView({ params }: { params: { id: string } }) {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    // Simulated fetch of case data
    setData({
      title: "State of Maharashtra v. XYZ Corp (2024)",
      citation: "2024 INSC 123",
      text: "The appellant has filed this petition challenging the order passed by the High Court... [Full legal text would go here]",
      summary: {
        facts: "Dispute over possession of commercial property in Mumbai.",
        issue: "Whether locking of premises without notice violates Section 6 of SRA.",
        decision: "Judgment in favor of respondent; possession to be restored."
      }
    });
  }, [params.id]);

  if (!data) return <div className="p-10">Loading Intelligence...</div>;

  return (
    <div className={styles.container}>
      <Sidebar />
      <main className={styles.main}>
        <div className={styles.header}>
          <p className="text-muted text-sm">{data.citation}</p>
          <h1 className={styles.title}>{data.title}</h1>
        </div>

        <div className={styles.splitContent}>
          <div className={`${styles.judgmentBody} legal-text`}>
            {data.text}
          </div>

          <aside className={`${styles.aiSidebar} glass`}>
            <h3>LEXINDIA AI BRIEF</h3>
            <div className={styles.briefSection}>
              <h4>FACTS</h4>
              <p>{data.summary.facts}</p>
            </div>
            <div className={styles.briefSection}>
              <h4>ISSUE</h4>
              <p>{data.summary.issue}</p>
            </div>
            <div className={styles.briefSection}>
              <h4>DECISION</h4>
              <p>{data.summary.decision}</p>
            </div>
            <div className={styles.footer}>
              <p className="text-xs">Grounding: Llama 3 / Qdrant Vector DB</p>
            </div>
          </aside>
        </div>
      </main>
    </div>
  );
}
