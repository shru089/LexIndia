export const citizenCategories = [
  {
    id: "property",
    label: "Property / landlord issue",
    urgency: "Time-sensitive if there is a notice deadline or threatened lockout.",
    example:
      "My landlord is trying to force me out without returning the deposit, and I received a notice I do not fully understand.",
    evidence: [
      "Rent agreement or tenancy proof",
      "Payment receipts or bank transfer proof",
      "Notice copy and envelope / delivery details",
      "Chats, emails, or call records with the landlord",
    ],
  },
  {
    id: "consumer",
    label: "Consumer complaint",
    urgency: "Medium. Preserve invoices, promises, and refund timelines early.",
    example:
      "A seller took payment for a service but stopped responding and never delivered what was promised.",
    evidence: [
      "Invoice, receipt, or payment transaction",
      "Screenshots of promises, ads, or product details",
      "Refund requests and customer support responses",
      "Delivery or non-delivery proof",
    ],
  },
  {
    id: "family",
    label: "Family matter",
    urgency: "Varies widely. Sensitive cases should move to human review quickly.",
    example:
      "I need to understand my options around maintenance and repeated threats after separation.",
    evidence: [
      "Marriage or relationship documents where relevant",
      "Messages showing threats, demands, or non-support",
      "Financial dependence records",
      "Any existing complaint, FIR, or court paper",
    ],
  },
  {
    id: "employment",
    label: "Employment dispute",
    urgency: "High when salary, termination, or deadlines are involved.",
    example:
      "My employer terminated me suddenly and has not paid dues that were verbally promised.",
    evidence: [
      "Offer letter or employment contract",
      "Salary slips or bank statements",
      "Termination email or HR communication",
      "Performance records and written assurances",
    ],
  },
  {
    id: "cyber",
    label: "Cyber fraud or online harm",
    urgency: "Potentially immediate. Quick reporting can matter a lot.",
    example:
      "Someone tricked me into a payment transfer through a fake support message and I want to know what to do next.",
    evidence: [
      "Transaction ID or payment screenshot",
      "Phone number, website, or profile used by the fraudster",
      "Chats, call recordings, or emails",
      "Any complaint already filed on cyber portals or with police",
    ],
  },
];

export const citizenLanguages = [
  { id: "english", label: "English" },
  { id: "hindi", label: "Hindi" },
  { id: "marathi", label: "Marathi" },
];

export const citizenResult = {
  title: "Likely tenancy and deposit dispute with notice pressure",
  summary:
    "The notice appears to be about possession and money, and the practical question is whether the landlord is following the correct legal process before asking you to vacate or surrender rights. In plain terms, you should avoid reacting emotionally, preserve the paper trail, and understand whether the notice is only a pressure tactic or a real step in a legal sequence.",
  urgency: {
    level: "Medium to high",
    note: "If the notice mentions a short deadline, threat of lockout, or immediate surrender, a lawyer review should happen quickly.",
  },
  laws: [
    {
      heading: "Tenancy / rent law may control the eviction process",
      detail:
        "Depending on the state and the type of premises, the landlord may need to follow a specific legal route rather than informal pressure or self-help eviction.",
    },
    {
      heading: "The contract and deposit terms matter",
      detail:
        "The lease, renewal terms, and deposit clause may shape what notice period and refund obligations apply.",
    },
    {
      heading: "Threats, unlawful entry, or property seizure can raise separate issues",
      detail:
        "If the landlord threatens force, blocks access, or interferes with your belongings, the matter can move beyond a simple civil disagreement.",
    },
  ],
  actions: [
    "Collect the lease, payment records, and the exact notice copy in one place.",
    "Do not surrender originals or sign new papers until you understand the implications.",
    "If there is a deadline, consider a lawyer-reviewed response instead of ignoring the notice.",
  ],
  terms: [
    {
      label: "Possession",
      meaning:
        "Who actually controls or occupies the property, even if ownership is separate.",
    },
    {
      label: "Notice period",
      meaning:
        "The time a party claims must pass before they can take the next legal or contractual step.",
    },
    {
      label: "Security deposit",
      meaning:
        "Money held as protection against dues or damage, which often becomes a central dispute point.",
    },
  ],
  similarCases: [
    {
      title: "Tenant challenged informal eviction pressure before lawful proceedings",
      takeaway: "Court focused on due process and documentary proof of tenancy terms.",
    },
    {
      title: "Deposit dispute tied to premature possession demand",
      takeaway: "Outcome turned heavily on written agreement terms and payment records.",
    },
    {
      title: "Threat-based landlord conduct escalated beyond contract disagreement",
      takeaway: "Unsafe conduct changed the remedy strategy and increased urgency.",
    },
  ],
  sources: [
    "State rent and tenancy framework",
    "Contract terms in the lease / rent agreement",
    "Any police complaint, message history, or delivery record tied to the notice",
  ],
  disclaimer:
    "This is AI-generated legal information, not legal advice. For your specific situation, consult a licensed advocate. Laws may have changed; verify before acting.",
};

export const citizenDocuments = [
  {
    title: "Affidavit",
    risk: "Low to medium risk",
    use: "Statement-based declarations where facts need to be set out clearly.",
  },
  {
    title: "Complaint to police",
    risk: "Medium risk",
    use: "Useful for structured incident narration, but facts must be reviewed carefully.",
  },
  {
    title: "Consumer complaint",
    risk: "Medium risk",
    use: "Helpful when payment, service deficiency, or unfair trade issues are documented.",
  },
  {
    title: "Legal notice",
    risk: "Medium to high risk",
    use: "Should usually be reviewed by a lawyer before sending when rights or money are at stake.",
  },
  {
    title: "RTI application",
    risk: "Low risk",
    use: "Good candidate for guided generation with clear public authority targeting.",
  },
  {
    title: "Rent termination notice",
    risk: "Medium risk",
    use: "Works best when the tenancy terms and local law position are understood first.",
  },
];
