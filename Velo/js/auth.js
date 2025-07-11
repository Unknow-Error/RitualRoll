// Handles login and registration using /cripta/inicio and /cripta/registro

document.addEventListener("DOMContentLoaded", () => {
  const loginForm = document.getElementById("login-form");
  const registerForm = document.getElementById("register-form");
  const message = document.getElementById("message");

  // LOGIN
  if (loginForm) {
    loginForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;
      try {
        const res = await fetch("http://127.0.0.1:8000/cripta/inicio", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email, password }),
        });
        if (!res.ok) {
          message.innerText = "Credenciales inválidas.";
          return;
        }
        const user = await res.json();
        // Store user id/token for session (simulate JWT for now)
        localStorage.setItem("user", JSON.stringify(user));
        window.location.href = "sessions.html";
      } catch (err) {
        message.innerText = "Error: " + err.message;
      }
    });
  }

  // REGISTER
  if (registerForm) {
    registerForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const email = document.getElementById("reg-email").value;
      const password = document.getElementById("reg-password").value;
      const nombreUsuario = document.getElementById("reg-username").value;
      try {
        const res = await fetch("http://127.0.0.1:8000/cripta/registro", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email, password, nombreUsuario }),
        });
        if (!res.ok) {
          const msg = await res.text();
          message.innerText = "Registro fallido: " + msg;
          return;
        }
        message.innerText = "Registro exitoso. Ahora puedes iniciar sesión.";
        registerForm.reset();
      } catch (err) {
        message.innerText = "Error: " + err.message;
      }
    });
  }
});