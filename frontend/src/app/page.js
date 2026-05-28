import Link from "next/link";
import SectionCard from "@/components/shared/SectionCard";
import {
  citizenSummary,
  citizenUseCases,
  heroActions,
  lawyerCards,
  lawyerSummary,
  trustPoints,
} from "@/lib/constants/site";

export default function HomePage() {
  return (
    <div className="section-stack">
      <section className="hero">
        <div className="hero-grid">
          <div className="hero-copy">
            <span className="eyebrow">India-first legal intelligence</span>
            <h1>Understand your legal problem before it overwhelms you.</h1>
            <p className="lede">
              Lex India helps citizens decode legal notices, identify relevant
              Indian laws, and move toward verified human legal help. It also
              gives advocates a faster way to research judgments, compare
              precedents, and prepare draft work.
            </p>

            <div className="action-grid">
              {heroActions.map((action) => (
                <Link key={action.title} href={action.href} className="action-card">
                  <span className="kicker">{action.kicker}</span>
                  <strong>{action.title}</strong>
                  <p className="muted">{action.description}</p>
                </Link>
              ))}
            </div>
          </div>

          <aside className="hero-panel action-card">
            <div>
              <span className="kicker">What the product should feel like</span>
              <h2>Not a generic chatbot. A trusted legal operating layer.</h2>
            </div>
            <ul className="check-list">
              <li>Citizens get plain-language understanding before escalation.</li>
              <li>Advocates get a serious precedent and drafting workflow.</li>
              <li>Every answer stays framed as legal information, not legal advice.</li>
            </ul>
            <div className="badge-row">
              <span className="badge">Source-backed outputs</span>
              <span className="badge">Law-update flags</span>
              <span className="badge">Lawyer handoff path</span>
            </div>
          </aside>
        </div>
      </section>

      <section>
        <div className="section-head">
          <div>
            <span className="kicker">Two product journeys</span>
            <h2>Citizens and advocates should not feel like they are using the same product surface.</h2>
          </div>
        </div>
        <div className="split-grid">
          <SectionCard
            kicker="Citizen journey"
            title="Understand my problem, then find the right next step"
            description="Citizens need a calm, guided experience that makes legal language and paperwork less intimidating."
          >
            <ul>
              {citizenSummary.map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>
            <Link href="/citizen" className="btn-secondary">
              Explore citizen flow
            </Link>
          </SectionCard>

          <SectionCard
            kicker="Advocate journey"
            title="Research faster, prepare better, and stay visible to new clients"
            description="Professionals need a dense, efficient workspace that respects how legal research is actually done."
          >
            <ul>
              {lawyerSummary.map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>
            <Link href="/lawyer" className="btn-primary">
              Explore advocate flow
            </Link>
          </SectionCard>
        </div>
      </section>

      <section>
        <div className="section-head">
          <div>
            <span className="kicker">Common use cases</span>
            <h2>The homepage should open with real legal tasks, not abstract features.</h2>
            <p>
              These are the situations where users will likely begin: confused
              by a document, unsure what law applies, or trying to decide if a
              lawyer is needed now.
            </p>
          </div>
        </div>
        <div className="three-grid">
          {citizenUseCases.map((useCase) => (
            <div key={useCase} className="route-card">
              <span className="kicker">Use case</span>
              <strong>{useCase}</strong>
              <p className="muted">
                Start with document explanation, then surface the laws, urgency,
                and the option to involve a lawyer.
              </p>
            </div>
          ))}
        </div>
      </section>

      <section>
        <div className="section-head">
          <div>
            <span className="kicker">Trust layer</span>
            <h2>Legal UX lives or dies on credibility.</h2>
          </div>
        </div>
        <div className="three-grid">
          {trustPoints.map((point, index) => (
            <div key={point} className="metric-card">
              <div className="metric-value">0{index + 1}</div>
              <p className="muted">{point}</p>
            </div>
          ))}
        </div>
      </section>

      <section>
        <div className="section-head">
          <div>
            <span className="kicker">Human handoff</span>
            <h2>AI should guide the user toward verified legal help, not strand them.</h2>
          </div>
        </div>
        <div className="three-grid">
          {lawyerCards.map((lawyer) => (
            <article key={lawyer.name} className="lawyer-card">
              <span className="kicker">Verified advocate</span>
              <strong>{lawyer.name}</strong>
              <p>{lawyer.meta}</p>
              <p className="muted">{lawyer.detail}</p>
              <Link href="/lawyers" className="btn-ghost">
                View lawyer marketplace
              </Link>
            </article>
          ))}
        </div>
      </section>
    </div>
  );
}
