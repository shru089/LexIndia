"use client";

import { useState, useEffect } from 'react';
import { useSearchParams, useRouter } from 'next/navigation';

export default function CaseResearch() {
  const searchParams = useSearchParams();
  const router = useRouter();
  const query = searchParams.get('q') || '';
  
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [searchInput, setSearchInput] = useState(query);

  useEffect(() => {
    if (query) {
      setLoading(true);
      fetch(`http://localhost:8000/api/v1/cases?q=${encodeURIComponent(query)}`)
        .then(res => res.json())
        .then(data => {
          setResults(data.results);
          setLoading(false);
        });
    } else {
      // Default cases
      fetch(`http://localhost:8000/api/v1/cases`)
        .then(res => res.json())
        .then(data => setResults(data.results));
    }
  }, [query]);

  const handleSearch = (e) => {
    e.preventDefault();
    router.push(`/research?q=${encodeURIComponent(searchInput)}`);
  };

  return (
    <div style={{ padding: '2rem 4rem', background: '#F8F9FA', minHeight: 'calc(100vh - 150px)', display: 'flex', gap: '2rem' }}>
      {/* Left Column - Main Case Details */}
      <div style={{ flex: 2, display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
        
        <form onSubmit={handleSearch} style={{ display: 'flex', width: '100%', background: 'white', padding: '0.5rem', borderRadius: 'var(--border-radius-md)', boxShadow: 'var(--shadow-sm)' }}>
          <div style={{ display: 'flex', alignItems: 'center', padding: '0 1rem', color: '#888' }}>🔍</div>
          <input 
            type="text" 
            value={searchInput}
            onChange={(e) => setSearchInput(e.target.value)}
            placeholder="Search judgments, laws, or acts..." 
            style={{ flex: 1, border: 'none', outline: 'none', fontSize: '1rem', fontFamily: 'var(--font-inter)' }} 
          />
          <button type="submit" className="btn-primary">Search</button>
        </form>

        <h2 style={{ fontSize: '1.5rem', fontFamily: 'var(--font-playfair)' }}>
          {query ? `Search Results for "${query}"` : 'Recent Judgments Database'}
        </h2>

        {loading ? (
          <div>Loading database...</div>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            {results.map(caseItem => (
              <div key={caseItem.id} className="glass-panel" style={{ background: 'white', padding: '1.5rem', cursor: 'pointer' }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem' }}>
                  <span style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', fontWeight: 'bold' }}>{caseItem.court} - {caseItem.year}</span>
                  <span style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>{caseItem.citation}</span>
                </div>
                <h3 style={{ fontSize: '1.2rem', marginBottom: '0.5rem', fontFamily: 'var(--font-playfair)' }}>{caseItem.title}</h3>
                <p style={{ color: 'var(--success-color)', fontSize: '0.85rem', fontWeight: 'bold' }}>✨ AI Summary Available</p>
              </div>
            ))}
            {results.length === 0 && <div>No cases found for your query.</div>}
          </div>
        )}
      </div>

      {/* Right Column - Sidebar */}
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
        {/* Outcome Trends */}
        <div className="glass-panel" style={{ background: 'var(--neutral-color)', padding: '1.5rem' }}>
          <h3 style={{ fontSize: '1.1rem', marginBottom: '1.5rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}><span>📈</span> Database Insights</h3>
          
          <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.85rem', fontWeight: 'bold', marginBottom: '0.5rem' }}>
            <span>Total Indexed Cases</span>
            <span style={{ color: 'var(--success-color)' }}>5.2M+</span>
          </div>
          
          <div style={{ background: 'white', padding: '1rem', borderRadius: 'var(--border-radius-sm)', marginBottom: '1.5rem', fontSize: '0.85rem' }}>
            <span style={{ fontStyle: 'italic', color: 'var(--text-secondary)', display: 'block', marginBottom: '0.5rem' }}>AI Observation:</span>
            Over 150,000 cases added this week from the Supreme Court and High Courts.
          </div>
        </div>
      </div>
    </div>
  );
}
