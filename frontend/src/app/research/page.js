import Link from "next/link";
import { researchRows } from "@/lib/constants/site";

export default function ResearchPage() {
  return (
    <div className="section-stack">
      <section>
        <div className="section-head">
          <div>
            <span className="kicker">Research workspace</span>
            <h1>Case law search should feel like legal work, not a generic result list.</h1>
            <p>
              This v1 shell reframes research around filters, summaries,
              precedent comparison, and saveable work product for advocates,
              students, and advanced users.
            </p>
          </div>
          <Link href="/lawyer/workspace" className="btn-secondary">
            Open advocate workspace
          </Link>
        </div>

        <div className="split-grid">
          <div className="surface-card">
            <span className="kicker">Search filters</span>
            <strong>By court, act, section, year, outcome, and semantic similarity</strong>
            <p className="muted">
              The production version should combine keyword search, metadata
              filtering, and vector retrieval instead of direct hardcoded fetches
              from page components.
            </p>
            <div className="badge-row">
              <span className="badge">Supreme Court</span>
              <span className="badge">High Courts</span>
              <span className="badge">Act and section filters</span>
            </div>
          </div>

          <div className="surface-card">
            <span className="kicker">Why this matters</span>
            <strong>Lawyers need outcomes, ratios, and patterns fast.</strong>
            <p className="muted">
              Search should show AI summary, outcome metadata, and similar case
              actions without pretending the result is authoritative on its own.
            </p>
          </div>
        </div>
      </section>

      <section className="surface-card">
        <div className="section-head">
          <div>
            <span className="kicker">Result rows</span>
            <h2>Representative precedent cards</h2>
          </div>
        </div>
        <div className="table-like">
          {researchRows.map((row) => (
            <div key={row.title} className="table-row">
              <div>
                <strong>{row.title}</strong>
                <p className="muted">
                  AI summary, cited sections, and save/similar actions should
                  live here.
                </p>
              </div>
              <div>{row.court}</div>
              <div>{row.year}</div>
              <div>{row.outcome}</div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
