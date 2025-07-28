import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Power Bot',
  description: 'AI Chatbot powered by Next.js, DaisyUI, and Tailwind',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" data-theme="light">
      <body className="min-h-screen bg-base-200">
        {children}
      </body>
    </html>
  );
}
