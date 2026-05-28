"use client";

import { useState } from 'react';

export default function AIAssistant() {
  const [messages, setMessages] = useState([{ role: 'ai', content: 'Hello! I am the Lex India AI Assistant. Please describe your legal situation, and I will analyze the relevant laws and precedents for you.' }]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const sendMessage = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMsg = input;
    setMessages(prev => [...prev, { role: 'user', content: userMsg }]);
    setInput('');
    setIsLoading(true);

    try {
      const res = await fetch('http://localhost:8000/api/v1/ai/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userMsg })
      });
      const data = await res.json();
      
      setMessages(prev => [...prev, { role: 'ai', content: data.response, data }]);
    } catch (error) {
      console.error(error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '800px', margin: '0 auto', padding: '2rem' }}>
      <h1 style={{ fontSize: '2rem', marginBottom: '1rem', fontFamily: 'var(--font-playfair)' }}>AI Legal Assistant</h1>
      
      <div className="glass-panel" style={{ background: 'white', minHeight: '600px', display: 'flex', flexDirection: 'column' }}>
        <div style={{ flex: 1, padding: '1.5rem', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          {messages.map((msg, i) => (
            <div key={i} style={{ alignSelf: msg.role === 'user' ? 'flex-end' : 'flex-start', maxWidth: '80%' }}>
              <div style={{ 
                background: msg.role === 'user' ? 'var(--surface-dark)' : '#F8F9FA', 
                color: msg.role === 'user' ? 'white' : 'var(--text-primary)',
                padding: '1rem', borderRadius: 'var(--border-radius-md)',
                border: msg.role === 'ai' ? '1px solid #EAEAEA' : 'none'
              }}>
                {msg.content}
                
                {msg.data && (
                  <div style={{ marginTop: '1rem', paddingTop: '1rem', borderTop: '1px solid #CCC' }}>
                    <div style={{ marginBottom: '0.5rem' }}><strong>Severity:</strong> {msg.data.severity}</div>
                    <div style={{ marginBottom: '0.5rem' }}><strong>Applicable Sections:</strong> {msg.data.applicableSections?.join(', ')}</div>
                    <div><strong>Next Steps:</strong>
                      <ul style={{ paddingLeft: '1.5rem', marginTop: '0.5rem' }}>
                        {msg.data.nextSteps?.map((step, idx) => <li key={idx}>{step}</li>)}
                      </ul>
                    </div>
                  </div>
                )}
              </div>
              
              {msg.role === 'ai' && (
                <div style={{ fontSize: '0.75rem', color: 'var(--warning-color)', marginTop: '0.5rem', fontStyle: 'italic', background: '#FFF3F3', padding: '0.5rem', borderRadius: '4px' }}>
                  ⚠️ {msg.data?.disclaimer || 'This is AI-generated legal information, not legal advice. Consult a licensed advocate.'}
                </div>
              )}
            </div>
          ))}
          {isLoading && <div style={{ alignSelf: 'flex-start', background: '#F8F9FA', padding: '1rem', borderRadius: 'var(--border-radius-md)' }}>Analyzing...</div>}
        </div>
        
        <form onSubmit={sendMessage} style={{ padding: '1.5rem', borderTop: '1px solid #EAEAEA', display: 'flex', gap: '1rem', background: 'var(--bg-color)' }}>
          <input 
            type="text" 
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Describe your legal issue..." 
            style={{ flex: 1, padding: '1rem', borderRadius: 'var(--border-radius-sm)', border: '1px solid #CCC', outline: 'none' }} 
            disabled={isLoading}
          />
          <button type="submit" className="btn-primary" disabled={isLoading}>Send</button>
        </form>
      </div>
    </div>
  );
}
