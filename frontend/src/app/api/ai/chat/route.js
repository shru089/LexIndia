import { NextResponse } from 'next/server';

export async function POST(req) {
  try {
    const { message } = await req.json();
    
    // Simulated AI processing delay
    await new Promise(resolve => setTimeout(resolve, 1500));
    
    return NextResponse.json({
      response: `Based on your description: "${message}", I have analyzed the situation against the Indian legal framework. This appears to fall under Sections 420 (Cheating) and 406 (Criminal Breach of Trust) of the Indian Penal Code (IPC).`,
      severity: 'Cognizable, Non-Bailable',
      applicableSections: ['IPC Sec 420', 'IPC Sec 406'],
      nextSteps: [
        'File an FIR at your local police station.',
        'Collect all documentary evidence (emails, receipts, contracts).',
        'Send a formal legal notice demanding restitution.'
      ],
      disclaimer: 'This is AI-generated legal information, not legal advice. For your specific situation, consult a licensed advocate. Laws may have changed; verify before acting.'
    });
  } catch (error) {
    return NextResponse.json({ error: 'Failed to process request' }, { status: 500 });
  }
}
