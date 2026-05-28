export default function SectionCard({ title, kicker, description, children }) {
  return (
    <article className="surface-card">
      {kicker ? <span className="kicker">{kicker}</span> : null}
      <strong>{title}</strong>
      {description ? <p className="muted">{description}</p> : null}
      {children}
    </article>
  );
}
