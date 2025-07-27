'use client';
import { useState } from 'react';

interface Message {
  text: string;
  sender: 'user' | 'bot';
}

export default function ChatPage() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');

  const handleSend = async () => {
    if (input.trim()) {
      const newMessages: Message[] = [...messages, { text: input, sender: 'user' }];
      setMessages(newMessages);
      setInput('');

      // Replace with your actual API call
      const botResponse = await new Promise<string>((resolve) =>
        setTimeout(() => resolve(`This is a dummy response to: ${input}`), 1000)
      );

      setMessages([...newMessages, { text: botResponse, sender: 'bot' }]);
    }
  };

  return (
    <div className="flex flex-col h-screen">
      <div className="navbar bg-base-100">
        <div className="flex-1">
          <a className="btn btn-ghost text-xl">Power Bot</a>
        </div>
        <div className="flex-none">
          <div className="dropdown dropdown-end">
            <button className="btn">Recent Chats</button>
            <ul tabIndex={0} className="menu dropdown-content z-[1] p-2 shadow bg-base-100 rounded-box w-52 mt-4">
              <li><a>Chat 1</a></li>
              <li><a>Chat 2</a></li>
            </ul>
          </div>
        </div>
      </div>
      <div className="flex-1 overflow-y-auto p-4">
        <div className="chat-container space-y-4">
          {messages.map((msg, index) => (
            <div key={index} className={`chat ${msg.sender === 'user' ? 'chat-end' : 'chat-start'}`}>
              <div className="chat-bubble">{msg.text}</div>
            </div>
          ))}
        </div>
      </div>
      <div className="p-4 bg-base-100">
        <div className="input-group">
          <input
            type="text"
            placeholder="Type your message..."
            className="input input-bordered w-full"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSend()}
          />
          <button className="btn btn-primary" onClick={handleSend}>Send</button>
        </div>
      </div>
    </div>
  );
}
