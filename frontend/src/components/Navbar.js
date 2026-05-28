"use client";

import Link from 'next/link';
import { useState } from 'react';
import { useRouter } from 'next/navigation';

export default function Navbar() {
  const [query, setQuery] = useState('');
  const router = useRouter();

  const handleSearch = (e) => {
    e.preventDefault();
    if (query.trim()) {
      router.push(`/research?q=${encodeURIComponent(query)}`);
    }
  };

  return (
    <nav style={{
      display: 'flex', justifyContent: 'space-between', alignItems: 'center',
      padding: '1rem 4rem', borderBottom: '1px solid #EAEAEA',
      background: 'var(--surface-color)', position: 'sticky', top: 0, zIndex: 100
    }}>
      <div style={{ fontSize: '1.5rem', fontWeight: 700, fontFamily: 'var(--font-playfair)', color: 'var(--surface-dark)' }}>
        <Link href="/">Lex India</Link>
      </div>
      <div style={{ display: 'flex', gap: '2rem', alignItems: 'center', fontWeight: 600, fontSize: '0.95rem' }}>
        <Link href="/research" style={{ color: 'var(--success-color)', borderBottom: '2px solid var(--success-color)', paddingBottom: '0.2rem' }}>Research</Link>
        <Link href="/document-generator">Documents</Link>
        <Link href="/workspace">Workspace</Link>
      </div>
      <div style={{ display: 'flex', gap: '1rem', alignItems: 'center' }}>
        <form onSubmit={handleSearch} style={{ 
          display: 'flex', alignItems: 'center', background: 'var(--neutral-color)', 
          padding: '0.5rem 1rem', borderRadius: 'var(--border-radius-sm)', opacity: 0.7 
        }}>
          <span style={{ marginRight: '0.5rem' }}>🔍</span>
          <input 
            type="text" 
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Quick Search" 
            style={{ background: 'transparent', border: 'none', outline: 'none', width: '150px' }} 
          />
        </form>
        <div style={{ width: '36px', height: '36px', borderRadius: '50%', background: '#f0f0f0', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          👤
        </div>
      </div>
    </nav>
  );
}
