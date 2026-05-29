LEXINDIA | Product Requirements Document | Confidential 

**LEXINDIA** 

*AI-Powered Legal Assistance & Case Intelligence Platform* Product Requirements Document | v1.0 | 2025 

| Document Status  | Draft – Internal Review |
| :---- | :---- |
| **Target Market**  | India (pan-India rollout) |
| **Document Owner**  | Product Team |
| **Classification**  | Confidential |

v1.0 – 2025 | Internal & ConfidentialPage  
Lex India | Product Requirements Document | Confidential **Table of Contents** 

v1.0 – 2025 | Internal & ConfidentialPage  
Lex India | Product Requirements Document | Confidential 

**1\. Executive Summary** 

Lex India is a B2C and B2B legal technology platform purpose-built for India. It combines a structured repository of court judgments with large-language-model intelligence to help ordinary citizens understand their legal rights, identify applicable laws, surface comparable case precedents, and auto-generate standard legal documents—without requiring immediate professional assistance. 

For legal professionals, Lex India accelerates case research, surfaces precedent patterns, and provides an optional marketplace channel for new client acquisition. 

| Mission Statement  Democratize access to legal knowledge across India by removing cost, language, and literacy barriers—while preserving the integrity and accuracy that legal information demands. |
| :---- |

**1.1 Key Metrics & Success Criteria** 

| Metric  | 12-Month Target |
| :---- | :---- |
| Registered users (citizens)  | 250,000+ |
| Monthly active users  | 80,000+ |
| Cases in database  | 500,000+ |
| Document drafts generated  | 100,000+ |
| Lawyer profiles listed  | 5,000+ |
| AI answer accuracy (audited)  | \>88% |
| User satisfaction (NPS)  | \>45 |

v1.0 – 2025 | Internal & ConfidentialPage  
Lex India | Product Requirements Document | Confidential 

**2\. Problem Statement** 

**2.1 Current State of Legal Access in India** 

India has over 45 million pending court cases as of 2024\. Legal illiteracy is pervasive: most citizens do not know which IPC section or civil statute applies to their situation, cannot read verbatim judgment text, and cannot afford a lawyer for basic queries. The gap in access to justice is not merely financial—it is informational. 

| Pain Point  | Who Is Affected  | Severity |
| :---- | :---- | :---- |
| Legal language is inaccessible to common citizens | Citizens (85%+ of population)  | Critical |
| Case research is slow and  fragmented | Lawyers & law students  | High |
| Unawareness of applicable laws  | Citizens filing FIRs / complaints  | Critical |
| Cost of drafting basic documents  | Low-income individuals  | High |
| No reliable precedent lookup tool  | Junior advocates  | High |
| Geographic barrier to quality lawyers | Tier 2/3 cities & rural areas  | Critical |

**2.2 Market Opportunity** 

• India has \~1.5 million enrolled advocates (Bar Council of India, 2023\) • \~800 million internet users—smartphone penetration growing fast in Tier 2/3 cities • Legal tech market in India estimated at USD 650 million (2024), growing at \~22% CAGR • Indian Kanoon, eCourts, and SCI databases exist but offer no AI summarization or case analysis 

v1.0 – 2025 | Internal & ConfidentialPage  
Lex India | Product Requirements Document | Confidential 

**3\. Product Vision & Goals** 

**3.1 Vision** 

To be India's most trusted AI legal companion—bridging the gap between complex legal systems and everyday citizens, while empowering legal professionals with cutting-edge research intelligence. 

**3.2 Product Goals** 

1\. Enable citizens to understand their legal situation in plain language within 5 minutes of describing it 

2\. Reduce lawyer dependency for basic tasks (document drafting, law identification) by 60% 

3\. Provide lawyers with a 10x faster case research workflow 

4\. Create a financially sustainable platform through freemium, subscription, and marketplace models 

5\. Achieve multilingual support across 10 Indian languages within 18 months 

**3.3 Non-Goals (v1.0)** 

• Lex India will NOT provide legally binding advice or replace a licensed advocate • Lex India will NOT represent users in court or file documents on their behalf • Lex India will NOT integrate real-time live case tracking in v1.0 

• Lex India will NOT support non-Indian legal jurisdictions in the initial release v1.0 – 2025 | Internal & ConfidentialPage

Lex India | Product Requirements Document | Confidential 

**4\. Target Users & Personas** 

**4.1 Persona 1 – The Distressed Citizen** 

| Attribute  | Details |
| :---- | :---- |
| Name  | Ravi Sharma, 38, Nagpur |
| Situation  | Landlord illegally evicted him; does not know his rights |
| Tech literacy  | Moderate – uses WhatsApp, YouTube, basic apps |
| Goal  | Understand if the landlord acted illegally and what he can do |
| Pain  | Cannot afford Rs 5,000+ for an initial legal consultation |
| Success | Finds applicable law, understands next steps, downloads a complaint letter |

**4.2 Persona 2 – The Junior Advocate** 

| Attribute  | Details |
| :---- | :---- |
| Name  | Priya Menon, 27, Chennai – 2 years PQE |
| Situation | Preparing arguments for a cheque bounce case; needs fast precedent lookup |
| Tech literacy  | High – uses Google Scholar, eCourts |
| Goal  | Find NI Act Section 138 cases with similar facts and strong outcomes |
| Pain  | Manually reading through 50+ judgments is time-consuming |
| Success | Gets 10 summarized precedents with outcome metadata in under 3 minutes |

**4.3 Persona 3 – The Law Student** 

| Attribute  | Details |
| :---- | :---- |
| Name  | Arjun Kaur, 21, Chandigarh – 3rd year LLB |
| Situation  | Writing a moot court memorial on cyber defamation |
| Tech literacy  | High |
| Goal  | Analyze a corpus of IT Act cases and understand judicial trends |
| Pain  | College library access is limited; full-text databases are expensive |

v1.0 – 2025 | Internal & ConfidentialPage  
Lex India | Product Requirements Document | Confidential 

| Success  | Gets summarized cases, outcome statistics, and key ratios at no cost |
| :---- | :---- |

v1.0 – 2025 | Internal & ConfidentialPage  
Lex India | Product Requirements Document | Confidential 

**5\. Feature Specifications** 

**5.1 Feature 1 – Case Database & AI Summarization** 

**Description** 

A searchable, structured repository of Indian court judgments from the Supreme Court, all High Courts, and select District Courts. Each judgment is processed by an NLP pipeline that extracts key metadata and generates a plain-language summary. 

**Functional Requirements** 

• Ingest judgments via eCourts API, Indian Kanoon API, and SCI public feeds • Extract metadata: case number, court, bench, date, acts cited, sections cited, outcome, key parties 

• AI-generated summary: 3-sentence plain-language verdict explanation • Extended AI summary: 200-word structured analysis (facts, issue, held, ratio) • Filters: court tier, case type, year range, act/section, outcome 

• Full-text search with semantic search capability 

• Case bookmarking and export (PDF/DOCX) for registered users 

**Acceptance Criteria** 

• Summary generated within 4 seconds of page load 

• Accuracy of extracted sections validated against ground truth at \>93% • Database grows by minimum 10,000 new judgments per month 

**5.2 Feature 2 – AI Legal Assistant (Case Analyzer)** 

**Description** 

Users describe their situation in natural language (English or regional language). The AI identifies applicable legal acts and sections, classifies case severity and category, and recommends next steps—all with appropriate disclaimers. 

**Functional Requirements** 

• Multi-turn conversational interface (chat UI) 

• Intent detection: criminal, civil, family, property, consumer, cyber, labour • Named entity recognition: parties, dates, amounts, locations 

• Output: list of applicable sections with plain-language explanations 

• Severity classification: cognizable/non-cognizable, bailable/non-bailable v1.0 – 2025 | Internal & ConfidentialPage  
Lex India | Product Requirements Document | Confidential 

• Recommended next steps: file FIR, send legal notice, approach consumer forum, etc. • Mandatory disclaimer displayed before and after every AI response 

• Conversation history saved for registered users 

| Disclaimer Requirement (Mandatory)  Every AI response MUST include: 'This is AI-generated legal information, not legal advice. For your specific situation, consult a licensed advocate. Laws may have changed; verify before acting.' |
| :---- |

**5.3 Feature 3 – Similar Case Finder** 

**Description** 

Given a user's case description or a case ID, the system retrieves semantically similar cases from the database and presents outcome statistics, common evidence patterns, and win/loss rates. 

**Functional Requirements** 

• Semantic similarity search using vector embeddings (cosine similarity) • Returns top 10 similar cases ranked by similarity score 

• Each result shows: case citation, court, year, summary, outcome, similarity % • Aggregate stats: outcome distribution (plaintiff/defendant win %), average disposal time • Evidence patterns: most cited evidence types in similar cases 

• 'Cases like mine' saved to user profile for reference 

**5.4 Feature 4 – Legal Document Generator** 

**Description** 

A template-driven, AI-assisted document generation module that produces ready-to-submit legal documents based on user inputs. 

**Supported Documents (v1.0)** 

• Affidavit (general purpose) 

• FIR draft / complaint to police 

• Consumer complaint (NCDRC / State Commission) 

• Demand / legal notice letter 

• Bail application (for informational purposes only) 

• Rent agreement termination notice 

• RTI application 

v1.0 – 2025 | Internal & ConfidentialPage  
NYAYA.AI | Product Requirements Document | Confidential 

**Functional Requirements** 

• Guided form: user fills contextual fields; AI pre-fills boilerplate 

• Real-time preview as user types 

• Download as PDF and DOCX 

• Notarization guide included as footer note where applicable 

• Jurisdiction-specific formatting (stamp paper value, court heading) 

**5.5 Feature 5 – Lawyer Marketplace (Phase 2\)** 

**Description** 

An opt-in directory of licensed advocates with location, specialization, fee range, and a booking/contact mechanism. 

**Functional Requirements** 

• Lawyer self-registration with Bar Council enrollment number verification • Profile: photo, experience, specializations, fee range, languages spoken, client reviews • Search: by city/PIN, specialization, fee, language 

• Contact: in-app message or WhatsApp redirect 

• Appointment booking with calendar integration (Phase 2B) 

• Lawyer rating and review system (post-consultation) 

v1.0 – 2025 | Internal & ConfidentialPage  
NYAYA.AI | Product Requirements Document | Confidential 

**6\. Identified Loopholes & Mitigations** 

The following section documents critical risks, loopholes, and architectural gaps identified during product analysis—along with specific mitigation strategies for each. 

**6.1 Legal & Regulatory Loopholes** 

| LOOPHOLE L-01: AI Advice vs. Legal Practice  The Advocates Act, 1961 prohibits non-advocates from practicing law. If Lex India's AI responses are construed as 'legal advice' or 'legal practice,' the platform could face regulatory action from Bar Council of India.  |
| :---- |

| Mitigation Element  | Detail |
| :---- | :---- |
| Persistent disclaimers | Every AI output screen must display a non-dismissible disclaimer. Disclaimer must be in the user's selected language. |
| Terms of Service clause | Explicit user acceptance that Lex India provides 'legal information,' not 'legal advice'—and that the user will consult an advocate for binding decisions.  |
| Output framing | AI responses phrased as: 'Based on similar cases...' or 'Section X may be relevant...' — never 'You should file...' or 'You will win...' |
| Legal opinion from counsel | Obtain a formal opinion from a senior advocate / firm before public launch confirming the platform does not constitute legal practice. |

| LOOPHOLE L-02: AI Hallucination & Inaccurate Legal Sections  LLMs are known to 'hallucinate' citations, section numbers, and case outcomes. A citizen acting on an incorrect IPC section could file a wrong complaint or miss a limitation period. |
| :---- |

| Mitigation Element  | Detail |
| :---- | :---- |
| Retrieval-Augmented  Generation (RAG) | AI must only cite sections and cases retrieved from the verified internal database—not hallucinate from parametric memory. |
| Source citation with links | Every cited section or case must link to its verified source (eCourts, SCI, or internal DB record). |
| Confidence scoring | If model confidence \< threshold (e.g., 0.75), display a 'Low Confidence' badge and recommend professional consultation. |
| Human review queue | Flag responses with novel or unusual legal interpretations for review by a legal consultant. |

v1.0 – 2025 | Internal & ConfidentialPage  
Lex India | Product Requirements Document | Confidential 

| User feedback loop | Thumbs up/down on every AI response; negative feedback auto-escalates to review. |
| :---- | :---- |

| LOOPHOLE L-03: Data Copyright & Licensing of Judgments  Court judgments in India are generally public documents, but third-party legal databases (e.g., SCC Online, Manupatra) hold copyright in their curated databases. Scraping or reproducing their content violates IP law. |
| :---- |

| Mitigation Element  | Detail |
| :---- | :---- |
| Primary source only | Source exclusively from eCourts API, National Judicial Data Grid (NJDG), SCI public portal, and official High Court websites—not commercial databases. |
| Attribution & linking | Store case metadata and summaries only; link out to official sources for full text. Do not store verbatim reproductions of commercially curated content. |
| Legal review of data pipeline  | Have IP counsel audit the ingestion pipeline before launch. |
| Licensing agreements | If commercial DB access is needed, negotiate a formal API/data licensing agreement. |

| LOOPHOLE L-04: Generated Documents Used Without Legal Review Users may submit AI-generated affidavits or FIR drafts directly to courts or police stations without understanding that they may contain errors, incorrect jurisdiction, or inapplicable clauses—exposing them to legal harm. |
| :---- |

| Mitigation Element  | Detail |
| :---- | :---- |
| Mandatory document  disclaimer | Every generated document must carry a watermark and footer: 'Draft generated by Nyaya.AI for reference only. Review with a licensed advocate before submission.' |
| 'Review with Lawyer' CTA | Post-generation, prominently offer 'Connect with a Lawyer to Review This Document'—linking to the marketplace. |
| Field validation | Validate critical fields (court name, jurisdiction, section numbers) against a reference database before allowing download. |
| Limitation on high-risk docs | Certain documents (e.g., bail applications) should only be generated as 'educational reference' with prominent warnings against direct submission. |

| LOOPHOLE L-05: Personal Data & Privacy (DPDP Act 2023\) |
| :---- |

v1.0 – 2025 | Internal & ConfidentialPage  
Lex India | Product Requirements Document | Confidential 

| Users will share sensitive personal information—names, addresses, case facts, potentially involving third parties. The Digital Personal Data Protection Act, 2023 imposes strict obligations. |
| :---- |

| Mitigation Element  | Detail |
| :---- | :---- |
| DPDP-compliant consent flow | Explicit, granular consent before data collection. Separate consent for analytics vs. service delivery vs. marketing. |
| Data minimization | Collect only what is necessary to deliver the requested feature. Do not store full case descriptions longer than session unless user opts in. |
| Right to erasure | User can delete account and all associated data from  settings—fulfilled within 72 hours. |
| Third-party data | If user mentions third parties (accused, employer, landlord), do not store those names in persistent logs tied to the user profile. |
| DPO appointment | Appoint a Data Protection Officer before launch and publish a DPDP-compliant Privacy Notice. |

| LOOPHOLE L-06: Lawyer Verification & Fraudulent Listings  The marketplace could be misused by fake lawyers, suspended advocates, or non-advocates posing as legal professionals—causing direct harm to vulnerable users. |
| :---- |

| Mitigation Element  | Detail |
| :---- | :---- |
| Bar Council enrollment  verification | Verify enrollment number against state Bar Council rolls via API (where available) or manual check before profile goes live. |
| Document upload  | Require upload of Bar Council enrollment certificate \+ ID proof. |
| Suspension flag | Cross-reference against disciplinary proceedings list (published by Bar Council of India). |
| User reporting | In-app 'Report this Lawyer' button; three reports trigger temporary suspension and manual review. |
| Liability disclaimer | T\&C must clearly state Lex India is a directory platform and not responsible for the conduct of listed advocates.  |

| LOOPHOLE L-07: Misuse by Litigants Against Third Parties  Users could weaponize the platform—generating false FIR drafts, harassment notices, or misusing case lookup to stalk or intimidate. |
| :---- |

| Mitigation Element  | Detail |
| :---- | :---- |

v1.0 – 2025 | Internal & ConfidentialPage  
Lex India | Product Requirements Document | Confidential 

| Abuse detection | Monitor for patterns: multiple FIR drafts against same third party, bulk notice generation, adversarial query patterns. |
| :---- | :---- |
| Rate limiting | Limit document generation to 5 documents per user per day (free tier); paid tiers with higher limits require KYC. |
| Document logging | Log all generated documents tied to user account for law enforcement access upon valid legal order. |
| Prohibited use policy | T\&C explicitly prohibit use for harassment, false complaints, or intimidation—with account termination as penalty. |

| LOOPHOLE L-08: Outdated Legal Information  Indian laws are amended frequently (e.g., BNS replacing IPC in 2024). An AI trained on pre-amendment data could cite repealed sections—causing users to rely on defunct law. |
| :---- |

| Mitigation Element  | Detail |
| :---- | :---- |
| Legal database versioning | Each legal section in the knowledge base is tagged with effective\_from and effective\_to dates. |
| Real-time legislative feeds | Subscribe to PRS India, MoLJ notifications, and Gazette feeds for amendment alerts. |
| Model fine-tuning cadence | Quarterly RAG knowledge base refresh; major amendments trigger an out-of-cycle update within 30 days. |
| 'Law updated' badge | Display a warning badge on any result referencing a section amended in the last 180 days. |

v1.0 – 2025 | Internal & ConfidentialPage  
Lex India | Product Requirements Document | Confidential 

**7\. Technical Architecture** 

**7.1 High-Level System Components** 

| Component  | Technology / Approach |
| :---- | :---- |
| Mobile App  | Flutter (iOS \+ Android, single codebase) |
| Web App  | React.js \+ Next.js (SSR for SEO on case pages) |
| Backend API  | Python FastAPI (async, high performance) |
| Authentication  | Firebase Auth / Supabase (OTP-based for India) |
| Primary Database  | PostgreSQL (structured case metadata, user data) |
| Vector Database  | Qdrant or Weaviate (semantic similarity search) |
| AI / NLP Engine | RAG pipeline: LLM (GPT-4o / Llama 3 fine-tuned) \+ embedding model |
| Document Generation  | Jinja2 templates \+ python-docx / WeasyPrint for PDF |
| File Storage  | AWS S3 / Cloudflare R2 (judgments, generated docs) |
| Search  | Elasticsearch (full-text) \+ vector search hybrid |
| Queue / Jobs  | Celery \+ Redis (ingestion pipeline, async jobs) |
| CDN  | Cloudflare (static assets, DDoS protection) |
| Hosting  | AWS (Mumbai region ap-south-1 for data residency compliance) |
| Monitoring  | Datadog / Grafana \+ Sentry for error tracking |

**7.2 AI Pipeline Architecture** 

• Ingestion: Crawl/API fetch → clean HTML/PDF → extract text → chunk (512 tokens) → embed → store in vector DB 

• RAG Query Flow: User query → intent classifier → embed query → vector search (top-k=20) → rerank → pass to LLM with retrieved context → stream response • Document Generation: User form input → template selection → LLM fill-in for narrative sections → validation → PDF/DOCX render 

• Similarity Search: Case description → embed → cosine similarity against case embeddings → return ranked matches with metadata 

**7.3 Data Residency & Compliance** 

• All user PII and generated documents stored exclusively in AWS ap-south-1 (Mumbai) v1.0 – 2025 | Internal & ConfidentialPage  
Lex India | Product Requirements Document | Confidential 

• LLM inference may use external APIs (OpenAI / Anthropic) — ensure DPA / data processing agreements in place 

• Option to use self-hosted open-source LLM (Llama 3 / Mistral) for highest-sensitivity queries 

v1.0 – 2025 | Internal & ConfidentialPage  
Lex India | Product Requirements Document | Confidential 

**8\. Business Model** 

**8.1 Revenue Streams** 

| Tier  | Price (INR/month)  | Features |
| :---- | :---- | :---- |
| Free  | 0  | 5 queries/day, 3 doc drafts/month, basic case search |
| Citizen Pro  | 199  | Unlimited queries, 20 doc  drafts/month, PDF export, saved cases |
| Advocate  | 799  | All Pro features \+ advanced precedent analytics, bulk export, API access |
| Law Firm  | Custom (3,000+)  | Team accounts, white-label docs, dedicated support, SLA |
| Marketplace Commission  | 10–15% of consultation fee  | Earned when a lawyer gets a client booking through the  platform |
| B2B / Institution  | Custom  | Universities, NGOs, legal aid organizations—bulk licensing |

**8.2 Unit Economics (Year 1 Projections)** 

| Metric  | Estimate |
| :---- | :---- |
| Free users (Year 1\)  | 200,000 |
| Paid conversion rate  | 4% |
| Avg. paid ARPU/month  | Rs. 280 |
| MRR at end of Year 1  | Rs. 22.4 lakh (\~USD 27K) |
| Marketplace GMV (Year 1\)  | Rs. 40 lakh |
| Platform take rate  | 12% |
| Marketplace revenue  | Rs. 4.8 lakh |

v1.0 – 2025 | Internal & ConfidentialPage  
Lex India | Product Requirements Document | Confidential 

**9\. Product Roadmap** 

**9.1 Phase 1 – Foundation (Months 1–4)** 

• Core case database with 100,000+ Supreme Court and High Court judgments • AI Legal Assistant (English) – intent detection, section identification • Basic document generator: affidavit, FIR draft, legal notice 

• Web app (responsive) \+ basic Android app 

• User accounts, saved searches, document history 

• Legal disclaimer framework and T\&C 

**9.2 Phase 2 – Growth (Months 5–9)** 

• Similar Case Finder with semantic search and outcome analytics • Lawyer Marketplace (directory \+ contact) 

• 3 regional languages: Hindi, Tamil, Marathi 

• iOS app \+ performance optimization 

• Paid subscription tiers launch 

• Bar Council enrollment verification for lawyers 

**9.3 Phase 3 – Scale (Months 10–18)** 

• eCourts API integration for real-time case status (where available) • 10 Indian languages total 

• Lawyer booking & appointment system 

• Advanced analytics dashboard for law firms 

• Legal aid organization partnerships (free access tier) 

• WhatsApp chatbot integration for non-smartphone users 

v1.0 – 2025 | Internal & ConfidentialPage  
Lex India | Product Requirements Document | Confidential 

**10\. Risks & Mitigation Summary** 

| Risk  | Likelihood  | Mitigation |
| ----- | :---- | :---- |
| Bar Council regulatory challenge  | Medium  | Pre-launch legal opinion; strict 'information not advice' framing |
| AI accuracy below acceptable threshold | High (early)  | RAG architecture; human review queue; confidence badges |
| Data copyright claims from legal DBs | Medium  | Source only from official  government/court portals |
| Low user trust in AI for legal matters | High  | Transparent sourcing; lawyer endorsements; beta with legal NGOs |
| Low lawyer marketplace adoption  | Medium  | Early advocate outreach; free listing for first 6 months |
| DPDP compliance breach  | Low  | DPO \+ legal audit; data  minimization by design |
| Competitive response (Indian Kanoon, Vakil Search) | High  | Superior AI UX; regional  languages; document generation USP |
| Misuse for harassment/false FIRs  | Medium  | Rate limiting; abuse detection; document watermarking |
| Outdated legal information  post-amendment | High  | Legislative feed monitoring;  versioned knowledge base |

v1.0 – 2025 | Internal & ConfidentialPage  
Lex India | Product Requirements Document | Confidential 

**11\. KPIs & Success Metrics** 

**11.1 Acquisition** 

• Monthly new user registrations 

• Cost per acquisition (CPA) by channel 

• Organic search traffic (SEO on case summary pages) 

**11.2 Engagement** 

• Daily / Monthly active users (DAU/MAU ratio target: \>25%) • Avg. queries per session 

• Document drafts generated per month 

• Session duration 

**11.3 Quality** 

• AI section identification accuracy (audited quarterly against expert review) • User feedback score per response (thumbs up/down ratio) • Support tickets related to AI errors 

**11.4 Business** 

• Free-to-paid conversion rate 

• Monthly Recurring Revenue (MRR) 

• Marketplace consultation bookings 

• Lawyer activation rate (profiles going live within 14 days of signup) v1.0 – 2025 | Internal & ConfidentialPage  
Lex India | Product Requirements Document | Confidential 

**12\. Appendix** 

**12.1 Key Indian Laws in Scope (v1.0)** 

• Bharatiya Nyaya Sanhita (BNS) 2023 – replacing IPC 

• Bharatiya Nagarik Suraksha Sanhita (BNSS) 2023 – replacing CrPC • Code of Civil Procedure (CPC), 1908 

• Hindu Marriage Act / Special Marriage Act 

• Transfer of Property Act, 1882 

• Consumer Protection Act, 2019 

• Information Technology Act, 2000 (as amended) 

• Negotiable Instruments Act, 1881 (Section 138\) 

• Right to Information Act, 2005 

• Protection of Women from Domestic Violence Act, 2005 

• Prevention of Corruption Act, 1988 

• Motor Vehicles Act, 1988 

**12.2 Competitive Landscape** 

| Platform  | Strengths  | Nyaya.AI Advantage |
| :---- | ----- | :---- |
| Indian Kanoon  | Largest case DB, free,  well-indexed | AI summarization, document gen, multilingual UX |
| Vakil Search  | Lawyer marketplace, established  | Case intelligence \+ docs \+  marketplace in one |
| LawRato  | Lawyer Q\&A, high traffic  | AI-first, self-service, no need to wait for a lawyer |
| SCC Online / Manupatra  | Comprehensive, trusted by  advocates | Free tier, citizen UX, vernacular languages |
| DoNotPay (US)  | Consumer AI legal app  | India-specific, local law  knowledge, local languages |

**12.3 Glossary** 

| Term  | Definition |
| :---- | :---- |
| RAG | Retrieval-Augmented Generation: AI technique that retrieves relevant documents before generating a response |
| IPC / BNS  | Indian Penal Code (now replaced by Bharatiya Nyaya Sanhita) |
| CrPC / BNSS | Code of Criminal Procedure (replaced by Bharatiya Nagarik Suraksha Sanhita) |

v1.0 – 2025 | Internal & ConfidentialPage  
Lex India | Product Requirements Document | Confidential 

| NLP | Natural Language Processing: AI technology for understanding human text |
| :---- | :---- |
| DPDP Act | Digital Personal Data Protection Act, 2023 – India's primary data privacy law |
| DXA  | Document units used in Word/DOCX format (1440 DXA \= 1 inch) |
| PQE  | Post-Qualification Experience (years of practice after enrollment) |
| NJDG  | National Judicial Data Grid – government portal for court data |

*End of Document | Lex India PRD v1.0 | Confidential* 

v1.0 – 2025 | Internal & ConfidentialPage