import Link from "next/link";
import { citizenDocuments } from "@/lib/mock/citizen";

export default function CitizenDocumentsPage() {
  return (
    <div className="section-stack">
      <section>
        <div className="section-head">
          <div>
            <span className="kicker">Citizen document center</span>
            <h1>Guide low-risk drafts with clear warnings and lawyer review options.</h1>
            <p>
              The drafting experience should clearly distinguish between helpful
              structured documents and high-risk submissions that need legal
              review before use.
            </p>
          </div>
        </div>
        <div className="three-grid">
          {citizenDocuments.map((doc) => (
            <div key={doc.title} className="route-card">
              <span className="kicker">Document type</span>
              <strong>{doc.title}</strong>
              <div className="badge-row">
                <span className="badge">{doc.risk}</span>
              </div>
              <p className="muted">
                {doc.use}
              </p>
              <Link href="/lawyers" className="btn-ghost">
                Review with a lawyer
              </Link>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
