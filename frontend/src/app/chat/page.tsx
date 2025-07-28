'use client';
import React, { useEffect, useState } from 'react';
import { sendChatPrompt, getChatHistory } from '../../lib/api';

interface Message {
  sender: 'user' | 'ai';
  text: string;
}

interface HistoryMessage {
  id: string;
  prompt: string;
  response: string;
  created_at: string;
}

// Dummy userId for demo; replace with real user auth/session
const userId = 'demo-user-id';

export default function ChatPage() {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState<HistoryMessage[]>([]);
  const [showHistory, setShowHistory] = useState(false);

  useEffect(() => {
    // Load previous chats on mount
    getChatHistory(userId)
      .then(setHistory)
      .catch(() => setHistory([]));
  }, []);

  const handleSend = async () => {
    if (!input.trim()) return;
    const userMsg: Message = { sender: 'user', text: input };
    setMessages((msgs) => [...msgs, userMsg]);
    setLoading(true);
    try {
      const res = await sendChatPrompt(input);
      setMessages((msgs) => [...msgs, { sender: 'ai', text: res.reply }]);
      setInput('');
      // Optionally refresh history
      getChatHistory(userId).then(setHistory);
    } catch (e) {
      setMessages((msgs) => [...msgs, { sender: 'ai', text: 'Error: Could not get response.' }]);
    } finally {
      setLoading(false);
    }
  };

  const handleHistoryClick = (item: HistoryMessage) => {
    setMessages([
      { sender: 'user', text: item.prompt },
      { sender: 'ai', text: item.response },
    ]);
    setShowHistory(false);
  };

  return (
    <div className="flex h-screen">
      {/* Sidebar for previous chats */}
      <div className={`transition-all duration-200 bg-base-200 p-4 w-72 border-r border-base-300 ${showHistory ? '' : 'hidden md:block'}`}>
        <div className="flex items-center justify-between mb-4">
          <span className="font-bold text-lg">Previous Chats</span>
          <button className="btn btn-xs btn-ghost md:hidden" onClick={() => setShowHistory(false)}>✕</button>
        </div>
        <ul className="menu menu-vertical gap-2">
          {history.length === 0 && <li className="text-sm text-base-content/50">No previous chats</li>}
          {history.map((item) => (
            <li key={item.id}>
              <button className="btn btn-ghost btn-sm w-full text-left whitespace-normal" onClick={() => handleHistoryClick(item)}>
                <div className="font-semibold truncate">{item.prompt}</div>
                <div className="text-xs text-base-content/60 truncate">{item.response}</div>
              </button>
            </li>
          ))}
        </ul>
      </div>

      {/* Main chat area */}
      <div className="flex flex-col flex-1 h-full">
        <div className="navbar bg-base-100 border-b border-base-300">
          <div className="flex-1">
            <span className="btn btn-ghost text-xl">Power Bot</span>
          </div>
          <div className="flex-none">
            <button className="btn btn-outline md:hidden" onClick={() => setShowHistory((v) => !v)}>
              Previous Chats
            </button>
          </div>
        </div>
        <div className="flex-1 overflow-y-auto p-4 bg-base-200">
          <div className="chat-container space-y-4 max-w-2xl mx-auto">
            {messages.length === 0 && (
              <div className="text-center text-base-content/50">Start a conversation!</div>
            )}
            {messages.map((msg, index) => (
              <div key={index} className={`chat ${msg.sender === 'user' ? 'chat-end' : 'chat-start'}`}>
                <div className={`chat-bubble ${msg.sender === 'user' ? 'bg-primary text-primary-content' : 'bg-base-100 text-base-content'}`}>{msg.text}</div>
              </div>
            ))}
            {loading && (
              <div className="chat chat-start">
                <div className="chat-bubble bg-base-100 text-base-content opacity-60">Thinking...</div>
              </div>
            )}
          </div>
        </div>
        <div className="p-4 bg-base-100 border-t border-base-300">
          <div className="flex gap-2">
            <input
              type="text"
              placeholder="Type your message..."
              className="input input-bordered w-full"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && handleSend()}
              disabled={loading}
            />
            <button className="btn btn-primary" onClick={handleSend} disabled={loading || !input.trim()}>
              {loading ? <span className="loading loading-spinner"></span> : 'Send'}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
