const API_URL = "http://127.0.0.1:8000"; 

// Helper for API requests with token
export async function apiRequest(path, method = "GET", body = null) {
  const token = localStorage.getItem("token");
  const headers = {
    "Content-Type": "application/json",
    ...(token && { Authorization: `Bearer ${token}` })
  };
  const res = await fetch(API_URL + path, {
    method,
    headers,
    ...(body && { body: JSON.stringify(body) }),
  });
  if (!res.ok) {
    let msg = await res.text();
    throw new Error(msg || res.statusText);
  }
  return await res.json();
}