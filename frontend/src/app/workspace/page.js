export default function Workspace() {
  return (
    <div style={{ padding: '2rem 4rem', background: '#F8F9FA', minHeight: 'calc(100vh - 150px)' }}>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end', marginBottom: '2rem' }}>
        <div>
          <h1 style={{ fontSize: '2.5rem', marginBottom: '0.5rem', color: 'var(--text-primary)' }}>My Workspace</h1>
          <p style={{ color: 'var(--text-secondary)' }}>Welcome back, Adv. Sharma. Here is your legal overview for today.</p>
        </div>
        <div style={{ display: 'flex', gap: '1rem' }}>
          <button className="btn-primary" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <span>➕</span> New Analysis
          </button>
          <button className="btn-secondary" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <span>📄</span> Doc Gen
          </button>
        </div>
      </div>

      <div style={{ display: 'flex', gap: '1.5rem', alignItems: 'flex-start' }}>
        {/* Left Column */}
        <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          {/* Marketplace Profile */}
          <div className="glass-panel" style={{ padding: '1.5rem', background: 'white' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1rem' }}>
              <h3 style={{ fontSize: '1.1rem' }}>Marketplace Profile <span style={{ color: 'var(--success-color)' }}>✔</span></h3>
            </div>
            <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.8rem', fontWeight: 'bold', marginBottom: '0.5rem' }}>
              <span>COMPLETENESS</span>
              <span style={{ color: 'var(--success-color)' }}>85%</span>
            </div>
            <div style={{ height: '6px', background: '#EAEAEA', borderRadius: '3px', marginBottom: '1.5rem' }}>
              <div style={{ height: '100%', width: '85%', background: 'var(--success-color)', borderRadius: '3px' }}></div>
            </div>
            
            <div style={{ background: '#F4F7F9', padding: '0.8rem 1rem', borderRadius: 'var(--border-radius-sm)', display: 'flex', justifyContent: 'space-between', marginBottom: '0.5rem' }}>
              <span style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>✉️ New Inquiries</span>
              <span style={{ background: 'var(--warning-color)', color: 'white', padding: '2px 6px', borderRadius: '10px', fontSize: '0.75rem', fontWeight: 'bold' }}>4</span>
            </div>
            <div style={{ background: '#F4F7F9', padding: '0.8rem 1rem', borderRadius: 'var(--border-radius-sm)', display: 'flex', justifyContent: 'space-between', marginBottom: '1.5rem' }}>
              <span style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>👁️ Profile Views</span>
              <span style={{ color: 'var(--text-secondary)' }}>1.2k</span>
            </div>
            <button style={{ width: '100%', padding: '0.75rem', background: 'white', border: '1px solid #CCC', borderRadius: 'var(--border-radius-sm)', fontWeight: 'bold', cursor: 'pointer' }}>Update Profile</button>
          </div>

          {/* Research Metrics */}
          <div className="glass-panel" style={{ padding: '1.5rem', background: '#EAE1CE' }}>
            <h3 style={{ fontSize: '1.1rem', marginBottom: '1.5rem' }}>Research Metrics</h3>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '2rem' }}>
              <div>
                <div style={{ fontSize: '0.75rem', fontWeight: 'bold', color: 'var(--text-secondary)', marginBottom: '0.25rem' }}>THIS MONTH</div>
                <div style={{ fontSize: '2rem', fontWeight: 'bold' }}>142</div>
                <div style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>Queries Run</div>
              </div>
              <div>
                <div style={{ fontSize: '0.75rem', fontWeight: 'bold', color: 'var(--text-secondary)', marginBottom: '0.25rem' }}>SAVED CASES</div>
                <div style={{ fontSize: '2rem', fontWeight: 'bold' }}>28</div>
                <div style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>Active Files</div>
              </div>
            </div>
            <div style={{ fontSize: '0.85rem', fontWeight: 'bold', display: 'flex', justifyContent: 'space-between' }}>
              <span>AI Efficiency +12%</span>
              <span>↗</span>
            </div>
          </div>
        </div>

        {/* Middle Column */}
        <div style={{ flex: 1.5, display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
          {/* Active Drafts */}
          <div className="glass-panel" style={{ padding: '1.5rem', background: 'white' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1.5rem' }}>
              <h3 style={{ fontSize: '1.1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}><span>📄</span> Active Drafts</h3>
              <a href="#" style={{ color: 'var(--success-color)', fontSize: '0.85rem', fontWeight: 'bold' }}>View All</a>
            </div>
            
            <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', paddingBottom: '1rem', borderBottom: '1px solid #F0F0F0', marginBottom: '1rem' }}>
              <div style={{ width: '40px', height: '40px', background: 'var(--neutral-color)', borderRadius: 'var(--border-radius-sm)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>✍️</div>
              <div style={{ flex: 1 }}>
                <h4 style={{ fontSize: '1rem', marginBottom: '0.2rem' }}>Writ Petition - S.K. vs State</h4>
                <div style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>Last edited: 2 hours ago • Section 482 CrPC</div>
              </div>
              <span style={{ background: 'var(--secondary-color)', color: 'white', padding: '4px 8px', borderRadius: '12px', fontSize: '0.75rem', fontWeight: 'bold' }}>65% Prepared</span>
            </div>

            <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
              <div style={{ width: '40px', height: '40px', background: '#F0F0F0', borderRadius: 'var(--border-radius-sm)', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>📄</div>
              <div style={{ flex: 1 }}>
                <h4 style={{ fontSize: '1rem', marginBottom: '0.2rem' }}>Bail Application - Crime 102/2024</h4>
                <div style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>Last edited: Yesterday • NDPS Act</div>
              </div>
              <span style={{ background: '#EAE1CE', color: '#5C5544', padding: '4px 8px', borderRadius: '12px', fontSize: '0.75rem', fontWeight: 'bold' }}>Review Required</span>
            </div>
          </div>

          {/* Saved Cases */}
          <div className="glass-panel" style={{ padding: '1.5rem', background: 'white' }}>
            <h3 style={{ fontSize: '1.1rem', marginBottom: '1.5rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}><span>📁</span> Saved Cases</h3>
            
            <div style={{ borderLeft: '3px solid var(--success-color)', paddingLeft: '1rem', marginBottom: '1.5rem' }}>
              <div style={{ fontSize: '0.75rem', color: 'var(--text-secondary)', marginBottom: '0.25rem' }}>SUPREME COURT</div>
              <h4 style={{ fontSize: '1rem', marginBottom: '0.25rem' }}>M.C. Mehta vs. Union of India</h4>
              <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', fontStyle: 'italic' }}>Absolute Liability Principle in Env. Law</p>
            </div>
            
            <div style={{ borderLeft: '3px solid #CCC', paddingLeft: '1rem' }}>
              <div style={{ fontSize: '0.75rem', color: 'var(--text-secondary)', marginBottom: '0.25rem' }}>DELHI HIGH COURT</div>
              <h4 style={{ fontSize: '1rem', marginBottom: '0.25rem' }}>X vs. Y (Family Dispute)</h4>
              <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', fontStyle: 'italic' }}>Section 125 Maintenance Rights</p>
            </div>
          </div>
        </div>

        {/* Right Column */}
        <div style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
          {/* Recent History */}
          <div className="glass-panel" style={{ padding: '1.5rem', background: 'white', height: '100%' }}>
            <h3 style={{ fontSize: '1.1rem', marginBottom: '1.5rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}><span>⏱️</span> Recent History</h3>
            
            <div style={{ display: 'flex', gap: '0.75rem', marginBottom: '1.5rem' }}>
              <span style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>🔍</span>
              <div>
                <h4 style={{ fontSize: '0.9rem', marginBottom: '0.25rem' }}>"Adverse possession against government"</h4>
                <div style={{ fontSize: '0.75rem', color: 'var(--text-secondary)' }}>Today, 10:24 AM</div>
              </div>
            </div>
            
            <div style={{ display: 'flex', gap: '0.75rem', marginBottom: '1.5rem' }}>
              <span style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>🔍</span>
              <div>
                <h4 style={{ fontSize: '0.9rem', marginBottom: '0.25rem' }}>"Validity of e-signatures in contracts"</h4>
                <div style={{ fontSize: '0.75rem', color: 'var(--text-secondary)' }}>Yesterday, 04:15 PM</div>
              </div>
            </div>

            <div style={{ display: 'flex', gap: '0.75rem' }}>
              <span style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>🔍</span>
              <div>
                <h4 style={{ fontSize: '0.9rem', marginBottom: '0.25rem' }}>"Doctrine of Res Judicata arbitration"</h4>
                <div style={{ fontSize: '0.75rem', color: 'var(--text-secondary)' }}>Oct 24, 2024</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Case Strategy Recommendation (Bottom Panel) */}
      <div className="glass-panel" style={{ marginTop: '1.5rem', padding: '1.5rem 2rem', background: 'var(--neutral-color)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div style={{ maxWidth: '800px' }}>
          <h3 style={{ fontSize: '1.3rem', marginBottom: '0.5rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>Lex AI: Case Strategy Recommendation</h3>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem' }}>
            Based on your recent search for "Adverse Possession," I've identified 3 relevant precedents from the last 6 months that might change your strategy for Case #204. Would you like to review the summary?
          </p>
        </div>
        <button className="btn-primary" style={{ background: '#0D2B23', color: 'white', display: 'flex', alignItems: 'center', gap: '0.5rem', padding: '0.75rem 1.5rem' }}>
          ✨ Review Insights
        </button>
      </div>
    </div>
  );
}
