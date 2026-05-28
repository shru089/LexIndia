import Link from "next/link";
import { citizenResult } from "@/lib/mock/citizen";

export default function CitizenResultPage() {
  return (
    <div className="section-stack">
      <section>
        <div className="section-head">
          <div>
            <span className="kicker">Result page</span>
            <h1>Explain first. Recommend carefully. Then offer human help.</h1>
            <p>
              This should feel like a real legal understanding screen: plain
              language first, then laws, then urgency, then next steps and
              escalation.
            </p>
          </div>
        </div>

        <div className="result-layout">
          <div className="result-list">
            <div className="result-block">
              <span className="kicker">Plain-language summary</span>
              <strong>{citizenResult.title}</strong>
              <p className="muted">{citizenResult.summary}</p>
            </div>

            <div className="result-block">
              <span className="kicker">Relevant laws</span>
              <div className="detail-stack">
                {citizenResult.laws.map((law) => (
                  <div key={law.heading} className="detail-row">
                    <strong>{law.heading}</strong>
                    <p className="muted">{law.detail}</p>
                  </div>
                ))}
              </div>
            </div>

            <div className="result-block">
              <span className="kicker">Urgency and risk</span>
              <strong>{citizenResult.urgency.level}</strong>
              <p className="muted">{citizenResult.urgency.note}</p>
            </div>

            <div className="result-block">
              <span className="kicker">What you can do next</span>
              <ul>
                {citizenResult.actions.map((action) => (
                  <li key={action}>{action}</li>
                ))}
              </ul>
            </div>

            <div className="result-block">
              <span className="kicker">Important legal terms explained simply</span>
              <div className="detail-stack">
                {citizenResult.terms.map((term) => (
                  <div key={term.label} className="detail-row">
                    <strong>{term.label}</strong>
                    <p className="muted">{term.meaning}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>

          <aside className="result-list">
            <div className="result-block">
              <span className="kicker">Trust markers</span>
              <div className="badge-row">
                <span className="badge good">Confidence: medium</span>
                <span className="badge">Sources available</span>
                <span className="badge alert">Verify current law</span>
              </div>
              <p className="muted">
                {citizenResult.disclaimer}
              </p>
            </div>

            <div className="result-block">
              <span className="kicker">Similar case patterns</span>
              <div className="detail-stack">
                {citizenResult.similarCases.map((item) => (
                  <div key={item.title} className="detail-row">
                    <strong>{item.title}</strong>
                    <p className="muted">{item.takeaway}</p>
                  </div>
                ))}
              </div>
            </div>

            <div className="result-block">
              <span className="kicker">Sources to inspect</span>
              <ul>
                {citizenResult.sources.map((source) => (
                  <li key={source}>{source}</li>
                ))}
              </ul>
            </div>

            <div className="result-block">
              <span className="kicker">Need human review?</span>
              <strong>Connect with a verified lawyer before acting on a risky notice.</strong>
              <p className="muted">
                This should be a strong conversion path from AI understanding to
                actual legal aid.
              </p>
              <Link href="/lawyers" className="btn-primary">
                Find a verified lawyer
              </Link>
              <Link href="/citizen/documents" className="btn-ghost">
                Prepare a draft safely
              </Link>
            </div>
          </aside>
        </div>
      </section>
    </div>
  );
}
