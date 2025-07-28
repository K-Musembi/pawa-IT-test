import Link from 'next/link';

export default function HomePage() {
  return (
    <>
      <div className="hero min-h-screen bg-base-200">
        <div className="hero-content text-center">
          <div className="max-w-md">
            <h1 className="text-5xl font-bold">power bot</h1>
            <p className="py-6">Provident cupiditate voluptatem et in. Quaerat fugiat ut assumenda excepturi exercitationem quasi. In deleniti eaque aut repudiandae et a id nisi.</p>
            <Link href="/login" className="btn btn-primary">Start Chat</Link>
          </div>
        </div>
      </div>
      <div className="container mx-auto my-12 px-4">
        <h2 className="text-4xl font-bold text-center mb-8">About Power Bot</h2>
        <div className="card lg:card-side bg-base-100 shadow-xl">
          <div className="card-body">
            <h3 className="card-title">Intelligent Conversations</h3>
            <p>Power Bot is a state-of-the-art chatbot designed to provide you with seamless and intelligent conversations. Built with a powerful FastAPI backend and a responsive Next.js frontend.</p>
            <h3 className="card-title mt-4">Features</h3>
            <ul className="list-disc list-inside">
              <li>Real-time chat with AI</li>
              <li>Secure user authentication</li>
              <li>Chat history tracking</li>
              <li>Styled with the beautiful DaisyUI component library</li>
            </ul>
            <div className="card-actions justify-end">
              <Link href="/signup" className="btn btn-secondary">Get Started</Link>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
