from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Dict, List


def _tokenize(value: str) -> List[str]:
    return re.findall(r"[a-z0-9]+", value.lower())


def _load_section_map() -> Dict[str, Dict[str, str]]:
    root = Path(__file__).resolve().parents[3]
    mapping_path = root / "data" / "legal" / "section_maps" / "ipc_to_bns.json"
    if not mapping_path.exists():
        return {}

    with mapping_path.open("r", encoding="utf-8") as handle:
        raw_map = json.load(handle)

    normalized: Dict[str, Dict[str, str]] = {}
    for ipc_key, payload in raw_map.items():
        section_number = ipc_key.split("_")[-1]
        normalized[section_number] = {
            "legacy_section": ipc_key,
            "bns_section": payload.get("bns_section", ""),
            "title": payload.get("title", ""),
            "description": payload.get("description", ""),
        }
    return normalized


SECTION_MAP = _load_section_map()

LEGAL_CORPUS: List[Dict[str, Any]] = [
    {
        "id": "statute-bns-101",
        "title": "Bharatiya Nyaya Sanhita Section 101",
        "summary": "Maps legacy murder offences into the Bharatiya Nyaya Sanhita regime and is typically used to orient charge translation work from IPC to BNS.",
        "citation": "Illustrative statute brief",
        "source": "statute",
        "court": "Legislative",
        "topic": "Criminal law transition",
        "keywords": ["murder", "302", "101", "bns", "ipc", "charge", "criminal"],
        "content": "Use this section when translating IPC 302-era research into the BNS framework for charging notes, prosecution briefs, and police workflow updates.",
        "recommended_actions": [
            "Map every legacy IPC reference to its BNS successor before filing updated notes.",
            "Confirm whether subordinate rules or state circulars have changed operational practice.",
        ],
    },
    {
        "id": "statute-dpdp-2023",
        "title": "Digital Personal Data Protection Act, 2023",
        "summary": "A core framework for consent, notice, breach response, and fiduciary accountability in digital public services and enterprise systems.",
        "citation": "Act overview",
        "source": "statute",
        "court": "Legislative",
        "topic": "Digital governance",
        "keywords": ["privacy", "data", "dpdp", "consent", "breach", "government", "portal"],
        "content": "Use this as the baseline lens for privacy-by-design, purpose limitation, data minimisation, and breach-readiness in citizen-facing digital systems.",
        "recommended_actions": [
            "Maintain a consent and notice inventory for all user flows.",
            "Document breach escalation, retention, and grievance redressal steps.",
        ],
    },
    {
        "id": "judgment-puttaswamy",
        "title": "K. S. Puttaswamy privacy principles",
        "summary": "A leading constitutional privacy anchor that is commonly used when evaluating proportionality, necessity, and data governance safeguards.",
        "citation": "Constitution Bench privacy doctrine",
        "source": "judgment",
        "court": "Supreme Court of India",
        "topic": "Constitutional privacy",
        "keywords": ["privacy", "constitutional", "data", "surveillance", "proportionality"],
        "content": "Useful for framing whether a state action has a legitimate aim, lawful basis, rational connection, and proportionate safeguards.",
        "recommended_actions": [
            "Show clear purpose limitation and documented safeguards.",
            "Record how the least intrusive viable option was selected.",
        ],
    },
    {
        "id": "judgment-lalita-kumari",
        "title": "Lalita Kumari FIR registration principles",
        "summary": "Commonly referenced for police registration duties, threshold assessment, and the limited role of preliminary inquiry in select categories.",
        "citation": "FIR registration guidance",
        "source": "judgment",
        "court": "Supreme Court of India",
        "topic": "Police procedure",
        "keywords": ["fir", "police", "complaint", "registration", "criminal", "procedure"],
        "content": "Use this as a process anchor where the issue is whether information discloses a cognizable offence and what follow-up timeline is expected.",
        "recommended_actions": [
            "Separate intake triage from merits assessment.",
            "Preserve a documented decision trail for every complaint received.",
        ],
    },
    {
        "id": "judgment-maneka-gandhi",
        "title": "Maneka Gandhi due process principles",
        "summary": "Frequently used to test administrative fairness, arbitrariness, and the need for a just, fair, and reasonable state process.",
        "citation": "Administrative fairness doctrine",
        "source": "judgment",
        "court": "Supreme Court of India",
        "topic": "Administrative law",
        "keywords": ["hearing", "notice", "administrative", "natural justice", "fairness", "licence"],
        "content": "Helpful when building show-cause, hearing, notice, and speaking-order flows in public administration systems.",
        "recommended_actions": [
            "Ensure notice and hearing rights are explicit in the workflow.",
            "Capture speaking-order reasons in a reviewable format.",
        ],
    },
    {
        "id": "playbook-government-procurement",
        "title": "Government procurement diligence playbook",
        "summary": "A practical operating note for tender review, vendor due diligence, data handling obligations, and auditability in public procurement programs.",
        "citation": "Internal operating playbook",
        "source": "playbook",
        "court": "LexIndia demo",
        "topic": "Public sector operations",
        "keywords": ["tender", "procurement", "vendor", "compliance", "audit", "government"],
        "content": "Useful for steering RFP reviews, red-flagging indemnity gaps, and aligning contract clauses with public-sector accountability expectations.",
        "recommended_actions": [
            "Run a clause matrix before procurement sign-off.",
            "Track vendor data flows and audit rights in one workspace.",
        ],
    },
]

COURT_UPDATES: List[Dict[str, str]] = [
    {
        "bench": "Supreme Court",
        "matter": "Data governance readiness review",
        "stage": "Policy note hearing prep",
        "next_event": "Bench memo due in 48 hours",
    },
    {
        "bench": "Delhi High Court",
        "matter": "Public procurement clause dispute",
        "stage": "Written submissions under review",
        "next_event": "Risk note update requested",
    },
    {
        "bench": "Bombay High Court",
        "matter": "Commercial contract breach analysis",
        "stage": "Research bundle compilation",
        "next_event": "Authorities shortlist pending",
    },
]

WORKFLOW_TEMPLATES: List[Dict[str, Any]] = [
    {
        "id": "wf-research-memo",
        "name": "Research Memo",
        "stage": "Ready",
        "sla": "Same day",
        "summary": "Turns a question into issues, authorities, risk posture, and next actions.",
    },
    {
        "id": "wf-doc-compare",
        "name": "Clause Comparison",
        "stage": "Ready",
        "sla": "Under 30 min",
        "summary": "Highlights conflicts, financial deltas, and missing protections across drafts.",
    },
    {
        "id": "wf-fir-triage",
        "name": "FIR Triage",
        "stage": "Pilot",
        "sla": "2 hour target",
        "summary": "Supports intake teams with issue spotting, intake notes, and escalation cues.",
    },
]

DOCUMENT_CAPABILITIES: List[Dict[str, str]] = [
    {
        "name": "Brief Generation",
        "status": "Operational",
        "description": "Creates executive, legal, and action-oriented summaries from raw material.",
    },
    {
        "name": "Clause Comparison",
        "status": "Operational",
        "description": "Flags inconsistencies, timeline shifts, monetary deltas, and missing clauses.",
    },
    {
        "name": "OCR Intake",
        "status": "Demo-ready",
        "description": "Provides a stable extraction placeholder for scanned filings and annexures.",
    },
]


def section_matches(query: str) -> List[Dict[str, str]]:
    matches: List[Dict[str, str]] = []
    for token in _tokenize(query):
        if token in SECTION_MAP:
            payload = SECTION_MAP[token]
            matches.append(
                {
                    "query_section": token,
                    "legacy_section": payload["legacy_section"],
                    "bns_section": payload["bns_section"],
                    "title": payload["title"],
                    "description": payload["description"],
                }
            )
    return matches


def search_demo_corpus(query: str, limit: int = 10) -> List[Dict[str, Any]]:
    tokens = set(_tokenize(query))
    matches = section_matches(query)
    results: List[Dict[str, Any]] = []

    for entry in LEGAL_CORPUS:
        haystack_tokens = set(
            _tokenize(
                " ".join(
                    [
                        entry.get("title", ""),
                        entry.get("summary", ""),
                        entry.get("content", ""),
                        " ".join(entry.get("keywords", [])),
                    ]
                )
            )
        )
        overlap = len(tokens & haystack_tokens)
        keyword_bonus = sum(2 for keyword in entry.get("keywords", []) if keyword.lower() in query.lower())
        score = overlap * 4 + keyword_bonus
        if entry["source"] == "statute" and matches:
            score += 3
        if score <= 0:
            continue

        results.append(
            {
                "id": entry["id"],
                "title": entry["title"],
                "summary": entry["summary"],
                "citation": entry["citation"],
                "source": entry["source"],
                "topic": entry["topic"],
                "court": entry["court"],
                "recommended_actions": entry["recommended_actions"],
                "score": float(score),
            }
        )

    if matches:
        for match in matches:
            results.append(
                {
                    "id": f"section-map-{match['query_section']}",
                    "title": f"IPC {match['query_section']} -> BNS {match['bns_section']}",
                    "summary": match["description"],
                    "citation": match["title"],
                    "source": "section-map",
                    "topic": "Statute translation",
                    "court": "Legislative",
                    "recommended_actions": [
                        "Update research notes to reference the BNS section alongside the legacy IPC section.",
                        "Validate whether any subordinate procedure changed with the new code framework.",
                    ],
                    "score": 99.0,
                }
            )

    ranked = sorted(results, key=lambda item: item.get("score", 0.0), reverse=True)
    return ranked[:limit]


def build_analysis(query: str, context: List[Dict[str, Any]]) -> Dict[str, Any]:
    authorities = context[:3]
    query_lower = query.lower()

    if any(term in query_lower for term in ["arrest", "fir", "complaint", "police"]):
        risk_level = "High"
        summary = "The scenario appears to touch criminal procedure or police intake, so process discipline and timeline control matter immediately."
    elif any(term in query_lower for term in ["data", "privacy", "portal", "breach", "consent"]):
        risk_level = "Moderate"
        summary = "The scenario engages public-sector data governance concerns, so the strongest posture is lawful basis, minimisation, and auditable safeguards."
    else:
        risk_level = "Moderate"
        summary = "The scenario looks suitable for a structured memo that separates issues, authorities, evidence gaps, and immediate next actions."

    recommended_actions = [
        "Frame the question as issues, facts currently known, and facts still missing.",
        "Attach the strongest 2-3 authorities before moving into advocacy or policy drafting.",
        "Record the operational owner, deadline, and review checkpoint for the next action.",
    ]

    for item in authorities:
        for action in item.get("recommended_actions", []):
            if action not in recommended_actions:
                recommended_actions.append(action)
            if len(recommended_actions) >= 5:
                break
        if len(recommended_actions) >= 5:
            break

    return {
        "headline": "Structured legal information brief",
        "summary": summary,
        "risk_level": risk_level,
        "recommended_actions": recommended_actions[:5],
        "authorities": [
            {
                "title": item["title"],
                "source": item["source"],
                "citation": item.get("citation"),
                "topic": item.get("topic"),
            }
            for item in authorities
        ],
        "suggested_queries": [
            f"{query} compliance checklist",
            f"{query} leading authorities",
            f"{query} drafting risks",
        ],
        "disclaimer": "This is legal information for research and workflow support, not legal advice.",
    }


def get_briefing_payload() -> Dict[str, Any]:
    return {
        "mission": {
            "title": "Public-sector legal intelligence, built for operational confidence.",
            "summary": "LexIndia combines legal research, statute translation, document review, and workflow visibility in one controlled workspace.",
        },
        "metrics": [
            {"label": "Research workflows", "value": "12", "detail": "Ready or pilot templates"},
            {"label": "Tracked legal domains", "value": "6", "detail": "Constitutional, criminal, data, procurement, contracts, admin"},
            {"label": "Operational posture", "value": "Demo-ready", "detail": "Works with or without external AI infrastructure"},
        ],
        "workflow_queue": WORKFLOW_TEMPLATES,
        "court_updates": COURT_UPDATES,
        "document_capabilities": DOCUMENT_CAPABILITIES,
        "section_map_highlights": list(SECTION_MAP.values())[:3],
    }
