export default function DisclaimerBanner() {
  return (
    <div style={{
      background: 'var(--warning-color)', color: '#fff', textAlign: 'center',
      padding: '0.75rem 1rem', fontSize: '0.875rem', fontWeight: 600,
      position: 'sticky', top: '70px', zIndex: 99
    }}>
      ⚠️ This platform provides AI-generated legal information, not legal advice. For your specific situation, consult a licensed advocate. Laws may have changed; verify before acting.
    </div>
  );
}
