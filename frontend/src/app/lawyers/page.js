import { lawyerCards } from "@/lib/constants/site";

export default function LawyersPage() {
  return (
    <div className="section-stack">
      <section>
        <div className="section-head">
          <div>
            <span className="kicker">Verified lawyer marketplace</span>
            <h1>Move from AI understanding to real legal aid without losing context.</h1>
            <p>
              Lawyer discovery should be a core product path, especially after a
              citizen gets document analysis or a generated draft that still
              needs professional review.
            </p>
          </div>
        </div>

        <div className="route-bar">
          <span className="route-chip">City / PIN</span>
          <span className="route-chip">Specialization</span>
          <span className="route-chip">Language</span>
          <span className="route-chip">Fee range</span>
          <span className="route-chip">Verified only</span>
        </div>

        <div className="three-grid">
          {lawyerCards.map((lawyer) => (
            <article key={lawyer.name} className="lawyer-card">
              <span className="kicker">Verified listing</span>
              <strong>{lawyer.name}</strong>
              <p>{lawyer.meta}</p>
              <p className="muted">{lawyer.detail}</p>
              <div className="badge-row">
                <span className="badge good">Bar verification pending UI hook</span>
              </div>
            </article>
          ))}
        </div>
      </section>
    </div>
  );
}
