"use client";

import { useState } from 'react';

export default function HelpDrawer() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <>
      <button 
        onClick={() => setIsOpen(true)}
        style={{
          position: 'fixed', bottom: '2rem', right: '2rem', zIndex: 1000,
          background: 'var(--surface-dark)', color: 'white',
          width: '60px', height: '60px', borderRadius: '50%',
          display: 'flex', alignItems: 'center', justifyContent: 'center',
          fontSize: '1.5rem', border: 'none', boxShadow: 'var(--shadow-md)',
          cursor: 'pointer', fontWeight: 'bold'
        }}
      >
        ?
      </button>

      {isOpen && (
        <div style={{
          position: 'fixed', top: 0, right: 0, bottom: 0, width: '400px',
          background: 'var(--surface-color)', zIndex: 1001, boxShadow: '-5px 0 15px rgba(0,0,0,0.1)',
          display: 'flex', flexDirection: 'column', transition: 'transform 0.3s ease'
        }}>
          <div style={{ padding: '1.5rem', borderBottom: '1px solid #EAEAEA', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <h2 style={{ fontSize: '1.2rem', fontFamily: 'var(--font-playfair)' }}>Lex India Help Guide</h2>
            <button onClick={() => setIsOpen(false)} style={{ background: 'none', border: 'none', fontSize: '1.5rem', cursor: 'pointer' }}>×</button>
          </div>
          <div style={{ padding: '1.5rem', overflowY: 'auto', flex: 1 }}>
            <h3 style={{ marginBottom: '1rem', color: 'var(--secondary-color)' }}>How to use this platform:</h3>
            
            <div style={{ marginBottom: '1.5rem' }}>
              <strong>1. AI Legal Assistant</strong>
              <p style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', marginTop: '0.5rem' }}>Describe your legal issue in plain language. The AI will identify applicable acts and recommend next steps.</p>
            </div>
            
            <div style={{ marginBottom: '1.5rem' }}>
              <strong>2. Case Research</strong>
              <p style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', marginTop: '0.5rem' }}>Search our database of 5M+ judgments. The AI will automatically generate briefs and identify outcomes.</p>
            </div>
            
            <div style={{ marginBottom: '1.5rem' }}>
              <strong>3. Document Generator</strong>
              <p style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', marginTop: '0.5rem' }}>Generate standardized legal drafts like FIRs, Affidavits, and Notices using our guided forms.</p>
            </div>
            
            <div style={{ padding: '1rem', background: '#FFF3F3', borderRadius: 'var(--border-radius-sm)', fontSize: '0.85rem', color: 'var(--warning-color)', marginTop: '2rem', border: '1px solid #FADBD8' }}>
              <strong>Important Disclaimer:</strong> Lex India provides legal information, not legal advice. Always consult a licensed advocate before taking legal action.
            </div>
          </div>
        </div>
      )}
    </>
  );
}
