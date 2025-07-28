import axios from 'axios';

// Define a base URL for the API to avoid repetition
const API_BASE_URL = 'http://localhost:8000/api/v1';

// Create an axios instance for making API calls
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// --- Type Interfaces ---

interface UserCredentials {
  username: string;
  password: string;
}

// Assuming the backend returns user details including an ID on login/signup
interface User {
  id: string;
  username: string;
  // access_token might be returned on login
  access_token?: string;
  token_type?: string;
}

interface ChatResponse {
  reply: string;
  // other properties from backend...
}

interface HistoryMessage {
  id: string;
  prompt: string;
  response: string;
  created_at: string;
}

// --- API Functions ---

/**
 * Handles user signup.
 * The prompt specified 'localhost:8000/api/v1/users/login' for both, which is ambiguous.
 * Assuming a standard RESTful endpoint for signup.
 * @param credentials - The user's username and password.
 * @returns The created user's data.
 */
export async function signup(credentials: UserCredentials): Promise<User> {
  const response = await apiClient.post<User>('/users/signup', credentials);
  return response.data;
}

/**
 * Handles user login.
 * @param credentials - The user's username and password.
 * @returns The logged-in user's data, likely including a token.
 */
export async function login(credentials: UserCredentials): Promise<User> {
  // FastAPI's OAuth2PasswordRequestForm expects form data, not JSON.
  const params = new URLSearchParams();
  params.append('username', credentials.username);
  params.append('password', credentials.password);

  const response = await apiClient.post<User>('/users/login', params, {
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  });
  return response.data;
}

/**
 * Sends a chat prompt to the backend.
 * @param prompt - The user's message/prompt.
 * @returns The chatbot's reply.
 */
export async function sendChatPrompt(prompt: string): Promise<ChatResponse> {
  const response = await apiClient.post<ChatResponse>('/user-queries', { prompt });
  return response.data;
}

/**
 * Fetches the chat history for a given user.
 * @param userId - The ID of the user.
 * @returns An array of past chat messages.
 */
export async function getChatHistory(userId: string): Promise<HistoryMessage[]> {
  const response = await apiClient.get<HistoryMessage[]>(`/user-queries?user_id=${userId}`);
  return response.data;
}