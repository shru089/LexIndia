'use client';
import React, { useState } from 'react';
import Sidebar from '../components/Sidebar';
import AIAssistant from '../components/AIAssistant';
import styles from './Dashboard.module.css';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? 'http://localhost:8000';

type SearchResult = {
  id?: string;
  title?: string;
  summary?: string;
  citation?: string;
};

export default function Dashboard() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<SearchResult[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSearch = async () => {
    if (!query) return;
    setLoading(true);
    setError('');
    try {
      const response = await fetch(`${API_BASE_URL}/api/v1/research/search?query=${encodeURIComponent(query)}`);
      if (!response.ok) {
        throw new Error(`Search request failed with status ${response.status}`);
      }
      const data = await response.json();
      setResults(data.results || []);
    } catch (error) {
      console.error("Search failed:", error);
      setResults([]);
      setError('Search is temporarily unavailable. Please verify the API and search services are running.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.container}>
      <Sidebar />
      <AIAssistant />
      <main className={styles.main}>
        <div className={styles.searchHero}>
          <p className={styles.subtitle}>ELITE COUNSEL & QUANTITATIVE RESEARCH</p>
          <h2 className={styles.title}>LexIndia Intelligence</h2>
          
          <div className={`${styles.searchBar} glass`}>
            <input 
              type="text" 
              placeholder="Search case law, statutes, or ask a natural language..." 
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && handleSearch()}
            />
            <button className={styles.searchButton} onClick={handleSearch}>
              {loading ? '...' : 'SEARCH'}
            </button>
          </div>
        </div>

        <div className={styles.resultsContainer}>
          {error ? <p className="text-sm text-muted">{error}</p> : null}
          {results.length > 0 ? (
            <div className={styles.resultsList}>
              {results.map((res, idx: number) => (
                <div key={res.id || idx} className="glass-card mb-4 p-6">
                  <h3 className="mb-2">{res.title || "Judgment Title"}</h3>
                  <p className="text-muted text-sm">{res.summary || "Case analysis snippet..."}</p>
                  {res.citation ? <p className="text-muted text-sm">{res.citation}</p> : null}
                </div>
              ))}
            </div>
          ) : (
            <div className={styles.statsGrid}>
              <div className="glass-card">
                <h4>Latest Analytics</h4>
                <p>Supreme Court Ruling 22-A109 affects current litigation strategy.</p>
              </div>
              <div className="glass-card">
                <h4>Active Cases</h4>
                <p>Geller vs. Paradigm Corp: Briefing due in 4 hours.</p>
              </div>
            </div>
          )}
        </div>
      </main>
    </div>
  );
}
