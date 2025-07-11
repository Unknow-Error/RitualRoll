// Placeholder: You need a backend endpoint for "sessions" to make this functional.
import { apiRequest } from "./api.js";

document.addEventListener("DOMContentLoaded", () => {
  // Dummy session list for demonstration
  const sessionList = document.getElementById("session-list");
  if (sessionList) {
    sessionList.innerHTML = `
      <div><b>Demo Session</b> - <button onclick="window.location.href='session.html?id=demo'">Join</button></div>
    `;
  }

  document.getElementById("logout-btn").onclick = () => {
    localStorage.removeItem("user");
    window.location.href = "index.html";
  };
});