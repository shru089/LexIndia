'use client';

import React, { useEffect, useRef, useState } from 'react';

import styles from './AIAssistant.module.css';

type Message = {
  role: 'user' | 'assistant';
  text: string;
};

type AnalysisResponse = {
  analysis?: {
    headline?: string;
    summary?: string;
    risk_level?: string;
    recommended_actions?: string[];
    authorities?: Array<{ title?: string; source?: string }>;
    disclaimer?: string;
  };
};

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? 'http://localhost:8000';

const STARTER_MESSAGE =
  'Ask for a legal briefing, a workflow recommendation, or a statute translation and I will return a structured research note.';

const formatAssistantReply = (payload: AnalysisResponse) => {
  const analysis = payload.analysis;
  if (!analysis) {
    return 'A structured analysis is not available right now. Please try again.';
  }

  const lines = [
    analysis.headline ?? 'Structured legal information brief',
    '',
    analysis.summary ?? 'No summary was returned.',
    '',
    `Risk level: ${analysis.risk_level ?? 'Moderate'}`,
  ];

  if (analysis.recommended_actions?.length) {
    lines.push('', 'Recommended actions:');
    analysis.recommended_actions.forEach((action) => {
      lines.push(`- ${action}`);
    });
  }

  if (analysis.authorities?.length) {
    lines.push('', 'Authorities:');
    analysis.authorities.forEach((authority) => {
      lines.push(`- ${authority.title ?? 'Authority'} (${authority.source ?? 'research'})`);
    });
  }

  if (analysis.disclaimer) {
    lines.push('', analysis.disclaimer);
  }

  return lines.join('\n');
};

const AIAssistant = () => {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState<Message[]>([
    { role: 'assistant', text: STARTER_MESSAGE },
  ]);
  const [loading, setLoading] = useState(false);
  const [isOpen, setIsOpen] = useState(true);
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSubmit = async () => {
    const trimmed = input.trim();
    if (!trimmed || loading) return;

    setMessages((previous) => [...previous, { role: 'user', text: trimmed }]);
    setInput('');
    setLoading(true);

    try {
      const response = await fetch(`${API_BASE_URL}/api/v1/research/analyze`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ scenario: trimmed }),
      });

      if (!response.ok) {
        throw new Error(`API error ${response.status}`);
      }

      const data = (await response.json()) as AnalysisResponse;
      setMessages((previous) => [
        ...previous,
        { role: 'assistant', text: formatAssistantReply(data) },
      ]);
    } catch (assistantError) {
      console.error('Assistant request failed:', assistantError);
      setMessages((previous) => [
        ...previous,
        {
          role: 'assistant',
          text: 'The assistant could not reach the API. Verify the backend is running and try again.',
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (event: React.KeyboardEvent<HTMLInputElement>) => {
    if (event.key === 'Enter') {
      void handleSubmit();
    }
  };

  if (!isOpen) {
    return (
      <button
        className={styles.toggleButton}
        onClick={() => setIsOpen(true)}
        aria-label="Open LexIndia research assistant"
        title="Open LexIndia research assistant"
      >
        AI
      </button>
    );
  }

  return (
    <div className={`${styles.assistant} glass`} role="complementary" aria-label="LexIndia research assistant">
      <div className={styles.header}>
        <div className={styles.indicator} aria-hidden="true" />
        <span>Research assistant</span>
        <button
          className={styles.closeButton}
          onClick={() => setIsOpen(false)}
          aria-label="Close research assistant"
        >
          x
        </button>
      </div>

      <div className={styles.messageList} aria-live="polite">
        {messages.map((message, index) => (
          <div
            key={`${message.role}-${index}`}
            className={message.role === 'user' ? styles.userMessage : styles.assistantMessage}
          >
            {message.text}
          </div>
        ))}

        {loading ? (
          <div className={styles.assistantMessage}>
            <span className={styles.typingDot} />
            <span className={styles.typingDot} />
            <span className={styles.typingDot} />
          </div>
        ) : null}

        <div ref={bottomRef} />
      </div>

      <div className={styles.inputArea}>
        <input
          type="text"
          placeholder="Ask for a legal briefing..."
          value={input}
          onChange={(event) => setInput(event.target.value)}
          onKeyDown={handleKeyDown}
          disabled={loading}
          aria-label="Assistant message input"
        />
        <button
          className={styles.sendButton}
          onClick={() => void handleSubmit()}
          disabled={loading || !input.trim()}
          aria-label="Send message"
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default AIAssistant;
