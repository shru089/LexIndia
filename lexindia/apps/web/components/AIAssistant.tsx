'use client';
import React, { useState, useRef, useEffect } from 'react';
import styles from './AIAssistant.module.css';

type Message = {
  role: 'user' | 'assistant';
  text: string;
};

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL ?? 'http://localhost:8000';

const AIAssistant = () => {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState<Message[]>([
    { role: 'assistant', text: 'Welcome, Counsel. How can I assist with your research today?' },
  ]);
  const [loading, setLoading] = useState(false);
  const [isOpen, setIsOpen] = useState(true);
  const bottomRef = useRef<HTMLDivElement>(null);

  // Auto-scroll to latest message
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSubmit = async () => {
    const trimmed = input.trim();
    if (!trimmed || loading) return;

    const userMsg: Message = { role: 'user', text: trimmed };
    setMessages((prev) => [...prev, userMsg]);
    setInput('');
    setLoading(true);

    try {
      const res = await fetch(
        `${API_BASE_URL}/api/v1/research/analyze?scenario=${encodeURIComponent(trimmed)}`,
        { method: 'POST' }
      );
      if (!res.ok) throw new Error('API error');
      const data = await res.json();
      setMessages((prev) => [
        ...prev,
        { role: 'assistant', text: data.analysis ?? 'Analysis complete.' },
      ]);
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          text: 'I am currently offline. Please ensure the API service is running.',
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') handleSubmit();
  };

  if (!isOpen) {
    return (
      <button
        className={styles.toggleButton}
        onClick={() => setIsOpen(true)}
        aria-label="Open AI Research Associate"
        title="Open AI Assistant"
      >
        AI
      </button>
    );
  }

  return (
    <div className={`${styles.assistant} glass`} role="complementary" aria-label="AI Research Associate">
      <div className={styles.header}>
        <div className={styles.indicator} aria-hidden="true" />
        <span>AI Research Associate</span>
        <button
          className={styles.closeButton}
          onClick={() => setIsOpen(false)}
          aria-label="Close AI Assistant"
        >
          ×
        </button>
      </div>

      <div className={styles.messageList} aria-live="polite">
        {messages.map((msg, i) => (
          <div
            key={i}
            className={msg.role === 'user' ? styles.userMessage : styles.assistantMessage}
          >
            {msg.text}
          </div>
        ))}
        {loading && (
          <div className={styles.assistantMessage}>
            <span className={styles.typingDot} />
            <span className={styles.typingDot} />
            <span className={styles.typingDot} />
          </div>
        )}
        <div ref={bottomRef} />
      </div>

      <div className={styles.inputArea}>
        <input
          type="text"
          placeholder="Ask LexIndia..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          disabled={loading}
          aria-label="Message input"
        />
        <button
          className={styles.sendButton}
          onClick={handleSubmit}
          disabled={loading || !input.trim()}
          aria-label="Send message"
        >
          ↑
        </button>
      </div>
    </div>
  );
};

export default AIAssistant;
