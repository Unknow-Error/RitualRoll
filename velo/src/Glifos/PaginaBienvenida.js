"use client"

import React, { useState } from 'react';
import { registerUser, loginUser } from '../api'; // Importa las funciones de la API

const PaginaBienvenida = ({ onLoginSuccess }) => {
  const [isRegistering, setIsRegistering] = useState(false);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [username, setUsername] = useState('');
  const [avatarUrl, setAvatarUrl] = useState('');
  const [bio, setBio] = useState('');
  const [timezone, setTimezone] = useState('');
  const [language, setLanguage] = useState('');
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage('');
    setError('');

    try {
      if (isRegistering) {
        const userData = { email, password, username, avatar_url: avatarUrl, bio, timezone, language };
        const result = await registerUser(userData);
        setMessage(`Usuario ${result.username} registrado con éxito! Ahora puedes iniciar sesión.`);
        // Limpiar formulario o cambiar a modo login
        setEmail('');
        setPassword('');
        setUsername('');
        setAvatarUrl('');
        setBio('');
        setTimezone('');
        setLanguage('');
        setIsRegistering(false);
      } else {
        const result = await loginUser({ email, password });
        setMessage(`Bienvenido, ${result.username}!`);
        // Llama a la función de éxito de login pasada por props
        onLoginSuccess(result);
      }
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center p-4">
      <div className="card w-full max-w-md">
        <h2 className="text-3xl font-bold text-dark-gothic-accent text-center mb-6">
          {isRegistering ? 'Registro de Condenado' : 'Inicio de Sesión'}
        </h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-dark-gothic-text text-sm font-bold mb-2" htmlFor="email">
              Email
            </label>
            <input
              type="email"
              id="email"
              className="input-field"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div>
            <label className="block text-dark-gothic-text text-sm font-bold mb-2" htmlFor="password">
              Contraseña
            </label>
            <input
              type="password"
              id="password"
              className="input-field"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>

          {isRegistering && (
            <>
              <div>
                <label className="block text-dark-gothic-text text-sm font-bold mb-2" htmlFor="username">
                  Nombre de Usuario
                </label>
                <input
                  type="text"
                  id="username"
                  className="input-field"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  required
                />
              </div>
              <div>
                <label className="block text-dark-gothic-text text-sm font-bold mb-2" htmlFor="avatarUrl">
                  URL del Avatar (Opcional)
                </label>
                <input
                  type="text"
                  id="avatarUrl"
                  className="input-field"
                  value={avatarUrl}
                  onChange={(e) => setAvatarUrl(e.target.value)}
                />
              </div>
              <div>
                <label className="block text-dark-gothic-text text-sm font-bold mb-2" htmlFor="bio">
                  Biografía (Opcional)
                </label>
                <textarea
                  id="bio"
                  className="input-field"
                  value={bio}
                  onChange={(e) => setBio(e.target.value)}
                  rows="3"
                ></textarea>
              </div>
              <div>
                <label className="block text-dark-gothic-text text-sm font-bold mb-2" htmlFor="timezone">
                  Zona Horaria (Opcional)
                </label>
                <input
                  type="text"
                  id="timezone"
                  className="input-field"
                  value={timezone}
                  onChange={(e) => setTimezone(e.target.value)}
                />
              </div>
              <div>
                <label className="block text-dark-gothic-text text-sm font-bold mb-2" htmlFor="language">
                  Idioma (Opcional)
                </label>
                <input
                  type="text"
                  id="language"
                  className="input-field"
                  value={language}
                  onChange={(e) => setLanguage(e.target.value)}
                />
              </div>
            </>
          )}

          <button type="submit" className="btn-primary w-full">
            {isRegistering ? 'Registrar' : 'Iniciar Sesión'}
          </button>
        </form>

        {message && <p className="text-green-400 text-center mt-4">{message}</p>}
        {error && <p className="error-message text-center mt-4">{error}</p>}

        <button
          onClick={() => setIsRegistering(!isRegistering)}
          className="text-dark-gothic-accent hover:underline mt-4 block mx-auto"
        >
          {isRegistering ? '¿Ya tienes cuenta? Inicia Sesión' : '¿No tienes cuenta? Regístrate'}
        </button>
      </div>
    </div>
  );
};

export default PaginaBienvenida;
