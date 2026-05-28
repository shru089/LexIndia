import Link from "next/link";
import SectionCard from "@/components/shared/SectionCard";

const quickStarts = [
  "Upload a notice from a landlord, employer, bank, or police station",
  "Describe a dispute in plain language and get relevant laws explained simply",
  "Generate a safe first draft like an RTI, consumer complaint, or legal notice",
  "Ask a verified lawyer to review the case once you understand the basics",
];

export default function CitizenHomePage() {
  return (
    <div className="section-stack">
      <section className="hero">
        <div className="hero-grid">
          <div className="hero-copy">
            <span className="eyebrow">Citizen home</span>
            <h1>Start with the problem, not the jargon.</h1>
            <p className="lede">
              This side of Lex India is designed for ordinary users who need
              help understanding a legal notice, a police paper, a dispute, or
              what rights may apply before paying for professional consultation.
            </p>
            <div className="route-bar">
              <Link href="/citizen/analyze" className="btn-primary">
                Start new analysis
              </Link>
              <Link href="/citizen/documents" className="btn-secondary">
                Open document center
              </Link>
            </div>
          </div>
          <div className="surface-card">
            <span className="kicker">Quick starts</span>
            <ul>
              {quickStarts.map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>
          </div>
        </div>
      </section>

      <section>
        <div className="split-grid">
          <SectionCard
            kicker="Step 1"
            title="Understand the document or situation"
            description="The product should first translate legal complexity into plain language."
          >
            <Link href="/citizen/analyze" className="btn-ghost">
              Go to intake flow
            </Link>
          </SectionCard>
          <SectionCard
            kicker="Step 2"
            title="See the law, urgency, and next options"
            description="After the explanation, users should see relevant sections, deadlines, and whether they need human help."
          >
            <Link href="/citizen/result" className="btn-ghost">
              Preview result experience
            </Link>
          </SectionCard>
        </div>
      </section>
    </div>
  );
}
