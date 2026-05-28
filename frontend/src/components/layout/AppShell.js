import TopNav from "./TopNav";
import TrustBanner from "@/components/shared/TrustBanner";

export default function AppShell({ children }) {
  return (
    <div className="app-shell">
      <TopNav />
      <main className="page-main">
        <div className="page-shell">
          <TrustBanner />
          {children}
        </div>
      </main>
      <footer className="footer">
        <div className="footer-grid">
          <div>
            <strong>Lex India</strong>
            <p>
              India-first legal intelligence for citizens and advocates, built
              to simplify legal language without pretending to replace legal
              counsel.
            </p>
          </div>
          <div>
            <strong>Core promise</strong>
            <p>Understand the issue, see the law, then decide whether to involve a lawyer.</p>
          </div>
          <div>
            <strong>Mandatory reminder</strong>
            <p>
              This platform provides AI-generated legal information, not legal
              advice. Users should verify current law and consult a licensed
              advocate before acting.
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
}
