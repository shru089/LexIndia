export default function LawyerWorkspacePage() {
  return (
    <div className="section-stack">
      <section>
        <div className="section-head">
          <div>
            <span className="kicker">Workspace shell</span>
            <h1>Saved research, active drafting, and incoming review requests belong here.</h1>
          </div>
        </div>
        <div className="three-grid">
          <div className="route-card">
            <strong>Saved matter folders</strong>
            <p className="muted">Organize judgments, notes, and linked drafts by client or issue.</p>
          </div>
          <div className="route-card">
            <strong>Draft queue</strong>
            <p className="muted">Track what is in progress, pending review, or ready for export.</p>
          </div>
          <div className="route-card">
            <strong>Citizen handoff requests</strong>
            <p className="muted">Surface people who need professional review after AI analysis.</p>
          </div>
        </div>
      </section>
    </div>
  );
}
