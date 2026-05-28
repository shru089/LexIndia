# Lex India Frontend

This frontend is the public-facing Next.js application for **Lex India**, an India-first legal intelligence platform being shaped around two clear product journeys:

- **Citizens** who need legal language explained in plain terms before they escalate to a lawyer
- **Advocates** who need faster research, structured precedent discovery, and drafting support

The current codebase is intentionally being rebuilt away from a generic legal-tech demo into a more trustworthy legal product surface with stronger information architecture, clearer disclaimers, and role-specific workflows.

## What This App Covers

The active frontend currently includes the first pass of the new product structure:

- `/`
  Landing page with the new Lex India positioning
- `/citizen`
  Citizen home and guided entry points
- `/citizen/analyze`
  Intake flow for describing a matter or uploading a notice
- `/citizen/result`
  Plain-language result view with legal context, urgency, and lawyer handoff
- `/citizen/documents`
  Safer citizen-facing drafting entry points
- `/research`
  Legal research shell for case-law exploration
- `/lawyers`
  Verified lawyer marketplace direction
- `/lawyer`
  Advocate-facing dashboard direction
- `/lawyer/workspace`
  Research and drafting workspace shell
- `/about-trust`
  Product trust, methodology, and boundary-setting page

Some legacy routes still exist in the app and should be folded into the newer structure as the rebuild continues.

## Stack

- **Framework:** Next.js 16 (App Router)
- **Runtime:** React 19
- **Styling:** Global CSS with shared layout primitives
- **Module resolution:** `@/*` alias mapped to `src/*`

## Local Development

### 1. Install dependencies

```bash
npm install
```

### 2. Create local environment values

Use the checked-in [`.env.example`](./.env.example) as the reference for your local environment.

### 3. Start the dev server

```bash
npm run dev
```

The frontend runs on:

```text
http://localhost:3000
```

## Important Dev Note

This project currently uses:

```bash
next dev --webpack
```

for local development.

That is intentional. Turbopack was causing intermittent dev-only manifest and CSS asset failures in this workspace, especially on the landing page. Production builds still work correctly, but Webpack is the more stable choice here while the frontend is being actively restructured.

## Environment Variables

The frontend is designed to support both mock-first UI work and backend-connected development.

The key variables currently expected are:

- `NEXT_PUBLIC_APP_URL`
  Base URL for the frontend application
- `NEXT_PUBLIC_API_BASE_URL`
  Backend API base URL used when the frontend is wired to FastAPI
- `NEXT_PUBLIC_ENABLE_MOCK_DATA`
  Allows the frontend to run against staged/mock data during UI rebuild work
- `NEXT_PUBLIC_DEFAULT_LANGUAGE`
  Default explanation language for the citizen flow
- `NEXT_PUBLIC_SUPPORT_EMAIL`
  Support or contact email displayed in UI/help flows

## Project Layout

```text
frontend/
├─ public/
├─ src/
│  ├─ app/
│  ├─ components/
│  │  ├─ layout/
│  │  └─ shared/
│  └─ lib/
│     ├─ constants/
│     └─ mock/
├─ .env.example
├─ next.config.mjs
├─ package.json
└─ README.md
```

## Working Principles For This Frontend

The frontend should keep reflecting the actual product constraints:

- Explain legal issues before recommending actions
- Distinguish clearly between **legal information** and **legal advice**
- Surface trust signals near outputs, not buried in footers
- Keep citizen experiences plain-language and low-friction
- Keep advocate experiences denser and more operational
- Prefer realistic, source-aware product framing over inflated dashboard filler

## Deployment Notes

This app is deployed via Vercel. If a deployment fails, check these first:

1. `package.json` scripts
2. environment variables configured in Vercel
3. unresolved imports or route-level syntax issues
4. stale legacy pages still referencing old assumptions

If a local page builds successfully but behaves inconsistently only in `next dev`, restart the dev server and clear `.next/` before investigating the application code itself.

## Current Priority Areas

The frontend is still mid-rebuild. The next meaningful work items are:

1. remove or fold legacy routes into the new IA
2. deepen the citizen analyze/result workflow
3. strengthen research and case-detail UX
4. upgrade the advocate workspace from shell to usable workflow

## Team Note

This README is intentionally specific to the current state of Lex India rather than a generic Next.js starter. If the product direction changes, update this file alongside the route structure and environment contract instead of letting it drift.
