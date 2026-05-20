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
  source?: string;
};

export default function Dashboard() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<SearchResult[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [searched, setSearched] = useState(false);

  const handleSearch = async () => {
    const trimmed = query.trim();
    if (!trimmed || loading) return;

    setLoading(true);
    setError('');
    setSearched(true);

    try {
      const response = await fetch(
        `${API_BASE_URL}/api/v1/research/search?query=${encodeURIComponent(trimmed)}&limit=10`
      );
      if (!response.ok) {
        throw new Error(`Search failed with status ${response.status}`);
      }
      const data = await response.json();
      setResults(data.results ?? []);
    } catch (err) {
      console.error('Search failed:', err);
      setResults([]);
      setError(
        'Search is temporarily unavailable. Please verify the API and search services are running.'
      );
    } finally {
      setLoading(false);
    }
  };

  const handleClear = () => {
    setQuery('');
    setResults([]);
    setError('');
    setSearched(false);
  };

  return (
    <div className={styles.container}>
      <Sidebar />
      <AIAssistant />

      <main className={styles.main}>
        <div className={styles.searchHero}>
          <p className={styles.subtitle}>Elite Counsel &amp; Quantitative Research</p>
          <h2 className={styles.title}>LexIndia Intelligence</h2>

          <div className={`${styles.searchBar} glass`}>
            <input
              id="legal-search-input"
              type="search"
              placeholder="Search case law, statutes, or ask in natural language..."
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && handleSearch()}
              aria-label="Legal search query"
              autoComplete="off"
            />
            <button
              id="legal-search-button"
              className={styles.searchButton}
              onClick={handleSearch}
              disabled={loading || !query.trim()}
              aria-busy={loading ? 'true' : 'false'}
              aria-label="Run search"
            >
              {loading ? <span className={styles.spinner} aria-label="Searching…" /> : 'SEARCH'}
            </button>
          </div>
        </div>

        <div className={styles.resultsContainer}>
          {error && (
            <p className={styles.errorText} role="alert">
              {error}
            </p>
          )}

          {!error && searched && !loading && results.length === 0 && (
            <p className={`text-sm text-muted ${styles.noResults}`}>
              No results found for &quot;{query}&quot;. Try different keywords.
            </p>
          )}

          {results.length > 0 ? (
            <div className={styles.resultsList}>
              {results.map((res, idx) => (
                <div key={res.id ?? idx} className="glass-card mb-4 p-6">
                  <div className={styles.resultHeader}>
                    <h3 className={styles.resultTitle}>
                      {res.title ?? 'Judgment Title'}
                    </h3>
                    {res.source && (
                      <span className={`text-sm text-muted ${styles.resultSource}`}>
                        {res.source}
                      </span>
                    )}
                  </div>
                  {res.summary && (
                    <p className="text-muted text-sm mb-2">{res.summary}</p>
                  )}
                  {res.citation && (
                    <p className={`text-muted text-sm ${styles.resultCitation}`}>{res.citation}</p>
                  )}
                </div>
              ))}
            </div>
          ) : !searched ? (
            /* Default empty state — shown before any search */
            <div className={styles.statsGrid}>
              <div className="glass-card">
                <h4>Latest Analytics</h4>
                <p className="text-sm">
                  Supreme Court Ruling 22-A109 affects current litigation strategy.
                </p>
              </div>
              <div className="glass-card">
                <h4>Active Cases</h4>
                <p className="text-sm">
                  Geller vs. Paradigm Corp: Briefing due in 4 hours.
                </p>
              </div>
              <div className="glass-card">
                <h4>New Statutes</h4>
                <p className="text-sm">
                  Digital Personal Data Protection Act, 2023 — key compliance update.
                </p>
              </div>
              <div className="glass-card">
                <h4>Research Queue</h4>
                <p className="text-sm">
                  3 pending research tasks from the last 48 hours.
                </p>
              </div>
            </div>
          ) : null}
        </div>
      </main>
    </div>
  );
}
