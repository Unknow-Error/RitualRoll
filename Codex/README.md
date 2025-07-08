# RitualRoll


**RitualRoll** es una plataforma web diseñada para jugar partidas de rol en el universo de *World of Darkness* (WoD), compatible con ediciones como **20th Anniversary**. Este proyecto busca combinar la flexibilidad del juego presencial con las ventajas de una experiencia digital colaborativa.


## ✨ Características clave

- 🎭 **Soporte para fichas WoD**: Edita, guarda y reutiliza hojas de personaje compatibles con PDFs interactivos.
- 🎲 **Sistema de dados personalizado**: Tiradas basadas en el sistema d10 de WoD, con reglas de éxitos, fracasos y especialidades.
- 🗺️ **Mapa interactivo**: Usa imágenes de fondo con rejillas rectangulares o hexagonales, y coloca tokens para representar personajes y objetos.
- 📄 **Compatibilidad con PDFs interactivos**: Importa fichas ya creadas y exporta nuevas versiones con los cambios realizados.

## 🚧 Estado actual

> En desarrollo (prototipo)

Se está trabajando en:
- Modelo de ficha unificado.
- Motor de dados como clase exportable.
- Visualización y carga de PDFs interactivos.
- Integración inicial de chat y mapa con tokens.


## 🛠️ Tecnologías utilizadas

- **Frontend**:  
  - [React](https://reactjs.org/) – Librería de UI moderna (MIT License)  
  - [TailwindCSS](https://tailwindcss.com/) – Framework de estilos utilitario (MIT)  
  - [Konva.js](https://konvajs.org/) – Canvas interactivo para mapas y tokens (MIT)  
  - [Socket.io-client](https://socket.io/) – Comunicación en tiempo real (MIT)

- **Backend**:  
  - [FastAPI](https://fastapi.tiangolo.com/) – Framework backend moderno en Python (MIT)  

- **Manejo de PDFs interactivos**:  
  - [pdf-lib](https://pdf-lib.js.org/) – Lectura/modificación de formularios PDF (MIT, Node.js)  
  - [pdfrw](https://github.com/pmaupin/pdfrw) – Lectura/escritura de campos PDF (MIT, Python)

- **Comunicación en tiempo real**:  
  - [Socket.io](https://socket.io/) – WebSockets simples y robustos (MIT)

- **Almacenamiento de archivos (audio, imágenes, PDFs)**:  
  - [Supabase Storage](https://supabase.com/) – Open source alternativa a Firebase (PostgreSQL + S3 compatible)  
  - **O bien**: almacenamiento local en disco (`/uploads/`, útil para testing/desarrollo)

- **Base de datos**:  
  - [PostgreSQL](https://www.postgresql.org/) – Base de datos relacional potente y libre (PostgreSQL License)  

---

Pruebas:
source venv/bin/activate
cd /home/Nephelim/Documentos/Programacion/VSCodium-Projects/RitualRoll/Grimorio/Grimorio-FastAPI/RitualAPI
uvicorn ritualAPI:app --reload
http://127.0.0.1:8000/docs#

---

## Estructura del proyecto:

```bash
RitualRoll/
├── 📜 Grimorio/               # 📖 Backend: lógica oculta, invocaciones API, controladores
│   ├── Grimorio-FastAPI/              # Módulos del backend (e.g., Dados, Chat, PDF, Mapas)
│   │   ├── dados/             # Lógica de dados y mecánicas
│   │   ├── chat/             # WebSockets para comunicación
│   │   ├── pdfs/             # Lectura y escritura de PDFs interactivos
│   │   └── tokens/           # Tokens, imágenes y avatares
│   ├── Sigilos-NEST/         # Controladores REST o WebSocket (como routes o gateways)
│   ├── Artifacts/            # Servicios, utilidades compartidas (helpers)
│   ├── Sanctum/              # Configuración global del servidor (NestJS/FastAPI)
│   └── main.ts               # Punto de entrada del servidor

├── 🧱 Cripta/          # 🗄️ Base de datos y migraciones (la “cripta” de datos)
│   ├── runes.sql             # Scripts SQL iniciales
│   ├── schema.prisma         # (opcional) Prisma u ORM equivalente
│   └── migrations/           # Migraciones de cambios

├── 🌒 Velo/                   # 🌐 Frontend: la “capa visible” del ritual
│   ├── sigils/               # Componentes reutilizables (hojas, botones de tiradas, etc.)
│   ├── glyphs/               # Páginas (react-router o Next.js pages)
│   ├── familiars/            # Hooks personalizados
│   ├── echoes/               # Contextos globales (estado de usuario, partida, etc.)
│   ├── styles/               # Tailwind, fuentes, assets visuales
│   ├── public/               # Archivos estáticos (favicon, sonidos, imágenes)
│   └── index.tsx             # Punto de entrada

├── 🧿 Reliquias/                 # 📁 Archivos subidos (tokens, música, imágenes, PDFs)
│   ├── uploads/              # Lo que los jugadores suben
│   └── generated/            # PDFs y recursos generados

├── 📖 Codex/                  # 📚 Documentación y metadata del proyecto
│   ├── README.md
│   ├── ROADMAP.md
│   └── rituals.schema.json   # Esquemas JSON para fichas, tiradas, etc.

├── 🛠️ Alchemy/                # ⚗️ Configuración y scripts de desarrollo
│   ├── docker-compose.yml
│   ├── .env
│   ├── .eslintrc, .prettierrc
│   └── setup.sh              # Script para preparar entorno

└── package.json / pyproject.toml / etc.
```

## 🔮 Objetivos futuros

- Soporte completo para *Vampire*, *Mage*, *Werewolf* y demás líneas de WoD.
- FastAPI para las partes que requieren:

     Procesamiento de PDFs (con pdfrw, reportlab, etc.)

     Exportación de hojas como XML o JSON

    Lógica avanzada de IA o cálculos mágicos raros (por ejemplo, decisiones automáticas de escenas)

     Análisis de audio (si hacés algo con música o sincronización)

Y usás NestJS para:

     API principal REST para usuarios, partidas, fichas

     WebSockets (chat, dados, mapa en tiempo real)

     Autenticación (JWT, OAuth)

     Push notifications y comunicación en vivo con los jugadores

## 📜 Licencia

Este proyecto está bajo la licencia MIT. No incluye contenido oficial de White Wolf o Paradox Interactive, sólo herramientas que permiten jugar con reglas compatibles.
