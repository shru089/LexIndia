export default function AboutTrustPage() {
  return (
    <div className="section-stack">
      <section>
        <div className="section-head">
          <div>
            <span className="kicker">Trust and methodology</span>
            <h1>Legal products need a visible explanation of what they do and what they do not do.</h1>
          </div>
        </div>
        <div className="split-grid">
          <div className="result-block">
            <strong>What Lex India should do</strong>
            <ul>
              <li>Explain legal language in plain terms.</li>
              <li>Surface relevant laws and judgments from verified sources.</li>
              <li>Warn users when the answer is uncertain, recent, or risky.</li>
            </ul>
          </div>
          <div className="result-block">
            <strong>What Lex India should not claim</strong>
            <ul>
              <li>That it replaces an advocate.</li>
              <li>That a user will win a matter.</li>
              <li>That a generated draft is safe to file without review.</li>
            </ul>
          </div>
        </div>
      </section>
    </div>
  );
}
