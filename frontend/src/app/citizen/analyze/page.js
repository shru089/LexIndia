import Link from "next/link";
import {
  citizenCategories,
  citizenLanguages,
} from "@/lib/mock/citizen";

export default function CitizenAnalyzePage() {
  const selectedCategory = citizenCategories[0];

  return (
    <div className="section-stack">
      <section>
        <div className="section-head">
          <div>
            <span className="kicker">Citizen intake</span>
            <h1>Upload a legal paper or describe what happened.</h1>
            <p>
              This should feel like a guided legal intake, not a blank text box.
              The user needs help framing the problem, knowing what evidence
              matters, and understanding what the AI will return.
            </p>
          </div>
        </div>

        <div className="intake-grid">
          <div className="surface-card">
            <div className="badge-row">
              <span className="badge">Describe issue</span>
              <span className="badge">Upload notice</span>
              <span className="badge">Scan and simplify</span>
            </div>
            <div className="form-stack">
              <div className="field">
                <label>Issue category</label>
                <select defaultValue={selectedCategory.id}>
                  {citizenCategories.map((category) => (
                    <option key={category.id} value={category.id}>
                      {category.label}
                    </option>
                  ))}
                </select>
              </div>
              <div className="field">
                <label>Describe the issue in simple language</label>
                <textarea defaultValue={selectedCategory.example} />
              </div>
              <div className="split-grid split-grid-compact">
                <div className="field">
                  <label>When did this start?</label>
                  <input defaultValue="Received the notice this week" />
                </div>
                <div className="field">
                  <label>Where is this happening?</label>
                  <input defaultValue="Nagpur, Maharashtra" />
                </div>
              </div>
              <div className="field">
                <label>Preferred explanation language</label>
                <select defaultValue="english">
                  {citizenLanguages.map((language) => (
                    <option key={language.id} value={language.id}>
                      {language.label}
                    </option>
                  ))}
                </select>
              </div>
              <div className="field">
                <label>What outcome do you need right now?</label>
                <input defaultValue="Understand whether the notice is valid and what I should prepare before responding." />
              </div>
              <div className="route-bar">
                <Link href="/citizen/result" className="btn-primary">
                  Analyze this issue
                </Link>
                <Link href="/lawyers" className="btn-ghost">
                  Skip to lawyer discovery
                </Link>
              </div>
            </div>
          </div>

          <div className="surface-card">
            <div className="upload-box">
              <span className="kicker">Upload lane</span>
              <strong>Drop notice, complaint, or scanned legal paper here</strong>
              <p className="muted">
                In the full product this should accept image, PDF, and copied
                text so the RAG flow can extract technical legal language and
                explain it in plain terms.
              </p>
            </div>
            <div className="result-block slim-block">
              <span className="kicker">What the AI should return</span>
              <ul>
                <li>Plain-language explanation of the notice or dispute</li>
                <li>Likely laws and sections that may matter</li>
                <li>Urgency signal and evidence checklist</li>
                <li>Similar case patterns and lawyer handoff option</li>
              </ul>
            </div>
            <div className="result-block slim-block">
              <span className="kicker">Evidence checklist for this category</span>
              <ul>
                {selectedCategory.evidence.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            </div>
            <div className="badge-row">
              <span className="badge">Plain-language summary</span>
              <span className="badge">Relevant laws</span>
              <span className="badge alert">Not legal advice</span>
            </div>
            <p className="muted">
              {selectedCategory.urgency}
            </p>
          </div>
        </div>
      </section>
    </div>
  );
}
