// Assumes /socket.io/socket.io.js is loaded

export function connectSocket(sessionId, onMessage) {
  const token = localStorage.getItem("token");
  const socket = io("http://localhost:8000", {
    query: { session_id: sessionId },
    auth: { token }
  });
  socket.on("chat_message", onMessage);
  return socket;
}