"use client";

import { useState } from 'react';
import { useRouter } from 'next/navigation';

export default function Home() {
  const [query, setQuery] = useState('');
  const router = useRouter();

  const handleSearch = (e) => {
    e.preventDefault();
    if (query.trim()) {
      router.push(`/research?q=${encodeURIComponent(query)}`);
    }
  };

  return (
    <div style={{ minHeight: '100vh' }}>
      {/* Hero Section */}
      <section style={{
        background: 'linear-gradient(to bottom, #F4F4F4, var(--neutral-color))',
        padding: '6rem 2rem',
        textAlign: 'center',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center'
      }}>
        <h1 style={{ fontSize: '3.5rem', maxWidth: '800px', marginBottom: '1rem', color: 'var(--text-primary)', fontFamily: 'var(--font-playfair)' }}>
          Navigating Indian Law with AI Intelligence.
        </h1>
        <p style={{ color: 'var(--text-secondary)', fontSize: '1.1rem', maxWidth: '600px', marginBottom: '2.5rem' }}>
          Instant access to 5M+ judgments, real-time legal research, and automated document drafting tailored for the Indian judiciary.
        </p>
        
        <form onSubmit={handleSearch} style={{
          display: 'flex', width: '100%', maxWidth: '700px', background: 'white',
          padding: '0.5rem', borderRadius: 'var(--border-radius-md)', boxShadow: 'var(--shadow-md)'
        }}>
          <div style={{ display: 'flex', alignItems: 'center', padding: '0 1rem', color: '#888' }}>⚖️</div>
          <input 
            type="text" 
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search judgments, laws, or describe your situation..." 
            style={{ flex: 1, border: 'none', outline: 'none', fontSize: '1rem', fontFamily: 'var(--font-inter)' }} 
          />
          <button type="submit" className="btn-primary" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            Analyze ✨
          </button>
        </form>
        
        <div style={{ marginTop: '1rem', fontSize: '0.85rem', color: 'var(--text-secondary)', display: 'flex', gap: '1.5rem' }}>
          <span style={{ cursor: 'pointer' }} onClick={() => router.push('/research?q=IT Act Amendment')}>↗ Trending: IT Act Amendment</span>
          <span style={{ cursor: 'pointer' }} onClick={() => router.push('/research?q=EC Ruling on Privacy')}>↗ Recent: EC Ruling on Privacy</span>
        </div>
      </section>

      {/* Cards Section */}
      <section style={{ padding: '4rem', display: 'flex', gap: '2rem', justifyContent: 'center', background: '#F8F9FA' }}>
        <div className="glass-panel" style={{ flex: 1, maxWidth: '500px', padding: '2rem', background: 'white' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1.5rem' }}>
            <div style={{ width: '48px', height: '48px', background: 'var(--neutral-color)', borderRadius: 'var(--border-radius-sm)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '1.5rem' }}>
              👤
            </div>
            <span style={{ color: 'var(--success-color)', fontWeight: 'bold', fontSize: '0.75rem', letterSpacing: '1px' }}>CITIZEN ACCESS</span>
          </div>
          <h2 style={{ fontSize: '1.8rem', marginBottom: '1rem', fontFamily: 'var(--font-playfair)' }}>For Citizens</h2>
          <p style={{ color: 'var(--text-secondary)', marginBottom: '2rem', fontSize: '0.95rem' }}>
            Simplified legal tools for individuals to understand their rights and manage personal legal matters.
          </p>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
            <div style={{ display: 'flex', gap: '1rem', cursor: 'pointer' }} onClick={() => router.push('/ai-assistant')}>
              <div>🔍</div>
              <div>
                <h4 style={{ marginBottom: '0.25rem' }}>Analyze Case</h4>
                <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>Get a layman's summary of any legal notice.</p>
              </div>
            </div>
            <div style={{ display: 'flex', gap: '1rem', cursor: 'pointer' }} onClick={() => router.push('/document-generator')}>
              <div>📄</div>
              <div>
                <h4 style={{ marginBottom: '0.25rem' }}>Draft Documents</h4>
                <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>Generate rent agreements, affidavits, and wills.</p>
              </div>
            </div>
          </div>
        </div>

        <div className="glass-panel" style={{ flex: 1, maxWidth: '500px', padding: '2rem', background: 'var(--surface-dark)', color: 'white' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1.5rem' }}>
            <div style={{ width: '48px', height: '48px', background: 'rgba(255,255,255,0.1)', borderRadius: 'var(--border-radius-sm)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '1.5rem' }}>
              💼
            </div>
            <span style={{ color: '#D4CBB6', fontWeight: 'bold', fontSize: '0.75rem', letterSpacing: '1px' }}>PROFESSIONAL TIER</span>
          </div>
          <h2 style={{ fontSize: '1.8rem', marginBottom: '1rem', fontFamily: 'var(--font-playfair)' }}>For Professionals</h2>
          <p style={{ color: '#E0E0E0', marginBottom: '2rem', fontSize: '0.95rem' }}>
            Advanced AI-powered research and practice management suite for advocates and legal teams.
          </p>
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
            <div style={{ display: 'flex', gap: '1rem', background: 'rgba(255,255,255,0.05)', padding: '1rem', borderRadius: 'var(--border-radius-sm)', cursor: 'pointer' }} onClick={() => router.push('/research')}>
              <div>📚</div>
              <div>
                <h4 style={{ marginBottom: '0.25rem' }}>Research Precedents</h4>
                <p style={{ fontSize: '0.85rem', color: '#CCC' }}>Hyper-targeted case law search with AI citations.</p>
              </div>
            </div>
            <div style={{ display: 'flex', gap: '1rem', background: 'rgba(255,255,255,0.05)', padding: '1rem', borderRadius: 'var(--border-radius-sm)', cursor: 'pointer' }} onClick={() => router.push('/workspace')}>
              <div>⚖️</div>
              <div>
                <h4 style={{ marginBottom: '0.25rem' }}>Manage Practice</h4>
                <p style={{ fontSize: '0.85rem', color: '#CCC' }}>Automated cause lists and digital case files.</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Footer Section */}
      <section style={{ margin: '4rem auto', maxWidth: '1050px', background: 'var(--surface-dark)', borderRadius: 'var(--border-radius-md)', color: 'white', display: 'flex', overflow: 'hidden' }}>
        <div style={{ flex: 1, padding: '4rem' }}>
          <h2 style={{ fontSize: '2.5rem', marginBottom: '1rem', color: 'white', fontFamily: 'var(--font-playfair)' }}>Ready to transform your legal workflow?</h2>
          <p style={{ color: '#D4CBB6', marginBottom: '2rem' }}>
            Join over 15,000 legal professionals and thousands of citizens using Lex India to simplify justice.
          </p>
          <div style={{ display: 'flex', gap: '1rem' }}>
            <button className="btn-secondary" style={{ padding: '0.8rem 2rem' }}>Start Free Trial</button>
            <button style={{ background: 'transparent', border: '1px solid rgba(255,255,255,0.3)', color: 'white', padding: '0.8rem 2rem', borderRadius: 'var(--border-radius-sm)', fontWeight: 'bold' }}>Schedule a Demo</button>
          </div>
        </div>
      </section>
    </div>
  );
}
