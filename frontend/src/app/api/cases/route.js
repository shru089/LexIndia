import { NextResponse } from 'next/server';

export async function GET(req) {
  const { searchParams } = new URL(req.url);
  const query = searchParams.get('q') || '';
  
  // Simulated DB query delay
  await new Promise(resolve => setTimeout(resolve, 800));

  const mockDatabase = [
    { id: '1', title: 'Kesavananda Bharati Sripadagalvaru and Ors. v. State of Kerala and Anr.', year: 1973, court: 'Supreme Court of India', citation: '(1973) 4 SCC 225' },
    { id: '2', title: 'M.C. Mehta vs. Union of India', year: 1986, court: 'Supreme Court of India', citation: '1987 AIR 1086' },
    { id: '3', title: 'State of Maharashtra vs. Digital Entities', year: 2024, court: 'Supreme Court of India', citation: 'Case ID: 442/2023' },
    { id: '4', title: 'In Re: Intellectual Property in AI-Generated Content', year: 2024, court: 'Delhi High Court', citation: 'Case ID: 891/2024' }
  ];

  const results = query 
    ? mockDatabase.filter(caseItem => caseItem.title.toLowerCase().includes(query.toLowerCase()))
    : mockDatabase;

  return NextResponse.json({ results });
}
