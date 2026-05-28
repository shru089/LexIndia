'use client';

import React, { useEffect, useState } from 'react';

import styles from './Dashboard.module.css';
import AIAssistant from '../components/AIAssistant';
import Sidebar from '../components/Sidebar';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? 'http://localhost:8000';

type SearchResult = {
  id?: string;
  title?: string;
  summary?: string;
  citation?: string;
  source?: string;
  topic?: string;
  court?: string;
  recommended_actions?: string[];
};

type Metric = {
  label: string;
  value: string;
  detail: string;
};

type WorkflowItem = {
  id: string;
  name: string;
  stage: string;
  sla: string;
  summary: string;
};

type CourtUpdate = {
  bench: string;
  matter: string;
  stage: string;
  next_event: string;
};

type Capability = {
  name: string;
  status: string;
  description: string;
};

type SectionMapHighlight = {
  bns_section: string;
  title: string;
  description: string;
};

type BriefingData = {
  mission: {
    title: string;
    summary: string;
  };
  metrics: Metric[];
  workflow_queue: WorkflowItem[];
  court_updates: CourtUpdate[];
  document_capabilities: Capability[];
  section_map_highlights: SectionMapHighlight[];
};

const EMPTY_BRIEFING: BriefingData = {
  mission: {
    title: 'Public-sector legal intelligence, built for operational confidence.',
    summary:
      'LexIndia combines legal research, statute translation, document review, and workflow visibility in one controlled workspace.',
  },
  metrics: [],
  workflow_queue: [],
  court_updates: [],
  document_capabilities: [],
  section_map_highlights: [],
};

const QUICK_QUERIES = [
  'Translate IPC 302 into BNS',
  'Privacy breach response for a government portal',
  'Procurement clause diligence checklist',
];

export default function Dashboard() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<SearchResult[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [searched, setSearched] = useState(false);
  const [briefing, setBriefing] = useState<BriefingData>(EMPTY_BRIEFING);

  useEffect(() => {
    const loadBriefing = async () => {
      try {
        const response = await fetch(`${API_BASE_URL}/api/v1/research/briefing`);
        if (!response.ok) {
          throw new Error(`Briefing failed with status ${response.status}`);
        }

        const data = (await response.json()) as BriefingData;
        setBriefing(data);
      } catch (briefingError) {
        console.error('Briefing load failed:', briefingError);
      }
    };

    void loadBriefing();
  }, []);

  const executeSearch = async (rawQuery: string) => {
    const trimmed = rawQuery.trim();
    if (!trimmed || loading) return;

    setLoading(true);
    setError('');
    setSearched(true);

    try {
      const response = await fetch(
        `${API_BASE_URL}/api/v1/research/search?query=${encodeURIComponent(trimmed)}&limit=8`
      );
      if (!response.ok) {
        throw new Error(`Search failed with status ${response.status}`);
      }
      const data = await response.json();
      setResults(data.results ?? []);
    } catch (searchError) {
      console.error('Search failed:', searchError);
      setResults([]);
      setError(
        'Search is temporarily unavailable. Please verify the API and supporting services are running.'
      );
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = async () => {
    await executeSearch(query);
  };

  const handleQuickQuery = async (quickQuery: string) => {
    setQuery(quickQuery);
    await executeSearch(quickQuery);
  };

  const handleClear = () => {
    setQuery('');
    setResults([]);
    setError('');
    setSearched(false);
  };

  return (
    <div className={styles.shell}>
      <Sidebar />
      <AIAssistant />

      <main className={styles.main}>
        <section className={styles.hero} id="mission">
          <div className={styles.heroCopy}>
            <p className={styles.eyebrow}>Govtech legal command center</p>
            <h1 className={styles.heroTitle}>{briefing.mission.title}</h1>
            <p className={styles.heroSummary}>{briefing.mission.summary}</p>
          </div>

          <div className={styles.signalRow}>
            <span className={styles.signalPill}>Research + statute translation</span>
            <span className={styles.signalPill}>Document intelligence</span>
            <span className={styles.signalPill}>Pilot-ready workflows</span>
          </div>
        </section>

        <section className={styles.searchSection} id="search">
          <div className={`${styles.searchPanel} glass-card`}>
            <div className={styles.searchHeading}>
              <div>
                <p className={styles.sectionKicker}>Research workspace</p>
                <h2>Search law, policy, and operational guidance in one pass.</h2>
              </div>
              <p className={styles.searchSupport}>
                Built to keep legal teams aligned across authorities, document review, and public-service delivery.
              </p>
            </div>

            <div className={styles.searchBar}>
              <input
                id="legal-search-input"
                type="search"
                placeholder="Try: IPC 302 to BNS, privacy breach workflow, procurement diligence..."
                value={query}
                onChange={(event) => setQuery(event.target.value)}
                onKeyDown={(event) => event.key === 'Enter' && void handleSearch()}
                aria-label="Legal search query"
                autoComplete="off"
              />
              <button
                id="legal-search-button"
                className={styles.searchButton}
                onClick={() => void handleSearch()}
                disabled={loading || !query.trim()}
                aria-busy={loading ? 'true' : 'false'}
              >
                {loading ? 'Searching' : 'Run search'}
              </button>
              <button
                className={styles.clearButton}
                onClick={handleClear}
                disabled={loading && !searched}
              >
                Clear
              </button>
            </div>

            <div className={styles.quickQueryRow}>
              {QUICK_QUERIES.map((quickQuery) => (
                <button
                  key={quickQuery}
                  className={styles.quickQuery}
                  onClick={() => void handleQuickQuery(quickQuery)}
                  disabled={loading}
                >
                  {quickQuery}
                </button>
              ))}
            </div>
          </div>
        </section>

        <section className={styles.metricGrid} aria-label="Platform metrics">
          {briefing.metrics.map((metric) => (
            <article key={metric.label} className={`${styles.metricCard} glass-card`}>
              <p className={styles.metricLabel}>{metric.label}</p>
              <p className={styles.metricValue}>{metric.value}</p>
              <p className={styles.metricDetail}>{metric.detail}</p>
            </article>
          ))}
        </section>

        <section className={styles.workspace} id="operations">
          <div className={styles.primaryColumn}>
            <div className={`${styles.panel} glass-card`}>
              <div className={styles.panelHeader}>
                <div>
                  <p className={styles.sectionKicker}>Search results</p>
                  <h2>Authorities and operational notes</h2>
                </div>
                <p className={styles.panelMeta}>
                  {searched ? `${results.length} result${results.length === 1 ? '' : 's'}` : 'Ready for search'}
                </p>
              </div>

              {error ? (
                <p className={styles.errorText} role="alert">
                  {error}
                </p>
              ) : null}

              {results.length > 0 ? (
                <div className={styles.resultsList}>
                  {results.map((result, index) => (
                    <article key={result.id ?? index} className={styles.resultCard}>
                      <div className={styles.resultTop}>
                        <div>
                          <p className={styles.resultSource}>{result.source ?? 'research'}</p>
                          <h3 className={styles.resultTitle}>{result.title ?? 'Untitled authority'}</h3>
                        </div>
                        <span className={styles.resultCourt}>{result.court ?? 'LexIndia'}</span>
                      </div>

                      <p className={styles.resultSummary}>{result.summary ?? 'No summary available.'}</p>

                      <div className={styles.resultMetaRow}>
                        <span>{result.topic ?? 'General legal research'}</span>
                        {result.citation ? <span>{result.citation}</span> : null}
                      </div>

                      {result.recommended_actions?.length ? (
                        <div className={styles.actionBlock}>
                          <p className={styles.actionHeading}>Recommended next actions</p>
                          <ul className={styles.actionList}>
                            {result.recommended_actions.map((action) => (
                              <li key={action}>{action}</li>
                            ))}
                          </ul>
                        </div>
                      ) : null}
                    </article>
                  ))}
                </div>
              ) : searched && !loading ? (
                <div className={styles.emptyState}>
                  <h3>No matching authorities yet</h3>
                  <p>
                    Try a narrower section number, a statute name, or an operational scenario like privacy breach handling or FIR intake.
                  </p>
                </div>
              ) : (
                <div className={styles.emptyState}>
                  <h3>Mission preview</h3>
                  <p>{briefing.mission.summary}</p>
                </div>
              )}
            </div>
          </div>

          <aside className={styles.secondaryColumn} id="governance">
            <div className={`${styles.panel} glass-card`}>
              <div className={styles.panelHeader}>
                <div>
                  <p className={styles.sectionKicker}>Workflow queue</p>
                  <h2>Operational templates</h2>
                </div>
              </div>
              <div className={styles.stack}>
                {briefing.workflow_queue.map((workflow) => (
                  <article key={workflow.id} className={styles.stackCard}>
                    <div className={styles.stackRow}>
                      <h3>{workflow.name}</h3>
                      <span className={styles.stageBadge}>{workflow.stage}</span>
                    </div>
                    <p>{workflow.summary}</p>
                    <span className={styles.stackMeta}>Target SLA: {workflow.sla}</span>
                  </article>
                ))}
              </div>
            </div>

            <div className={`${styles.panel} glass-card`}>
              <div className={styles.panelHeader}>
                <div>
                  <p className={styles.sectionKicker}>Court watch</p>
                  <h2>Priority matters</h2>
                </div>
              </div>
              <div className={styles.stack}>
                {briefing.court_updates.map((update) => (
                  <article key={`${update.bench}-${update.matter}`} className={styles.stackCard}>
                    <div className={styles.stackRow}>
                      <h3>{update.matter}</h3>
                      <span className={styles.stackMeta}>{update.bench}</span>
                    </div>
                    <p>{update.stage}</p>
                    <span className={styles.stackMeta}>{update.next_event}</span>
                  </article>
                ))}
              </div>
            </div>

            <div className={`${styles.panel} glass-card`}>
              <div className={styles.panelHeader}>
                <div>
                  <p className={styles.sectionKicker}>Platform readiness</p>
                  <h2>Document and statute tools</h2>
                </div>
              </div>
              <div className={styles.stack}>
                {briefing.document_capabilities.map((capability) => (
                  <article key={capability.name} className={styles.stackCard}>
                    <div className={styles.stackRow}>
                      <h3>{capability.name}</h3>
                      <span className={styles.stageBadge}>{capability.status}</span>
                    </div>
                    <p>{capability.description}</p>
                  </article>
                ))}

                {briefing.section_map_highlights.map((section) => (
                  <article key={`${section.bns_section}-${section.title}`} className={styles.stackCard}>
                    <div className={styles.stackRow}>
                      <h3>BNS {section.bns_section}</h3>
                      <span className={styles.stackMeta}>{section.title}</span>
                    </div>
                    <p>{section.description}</p>
                  </article>
                ))}
              </div>
            </div>
          </aside>
        </section>
      </main>
    </div>
  );
}
