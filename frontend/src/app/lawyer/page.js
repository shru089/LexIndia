import Link from "next/link";

const modules = [
  "Recent research folders",
  "Active drafts",
  "Saved precedents",
  "Citizen review requests",
  "Profile visibility and lead intake",
  "Outcome and section trend insights",
];

export default function LawyerHomePage() {
  return (
    <div className="section-stack">
      <section className="hero">
        <div className="hero-grid">
          <div className="hero-copy">
            <span className="eyebrow">Advocate dashboard</span>
            <h1>Research faster and convert insight into client-ready work.</h1>
            <p className="lede">
              This side of the product should feel operational and dense. It is
              where advocates manage research, compare precedents, review drafts,
              and optionally receive new client discovery through verified
              listings.
            </p>
            <div className="route-bar">
              <Link href="/research" className="btn-primary">
                Start research
              </Link>
              <Link href="/lawyers" className="btn-ghost">
                View marketplace
              </Link>
            </div>
          </div>

          <div className="surface-card">
            <span className="kicker">Core modules</span>
            <ul>
              {modules.map((module) => (
                <li key={module}>{module}</li>
              ))}
            </ul>
          </div>
        </div>
      </section>
    </div>
  );
}
