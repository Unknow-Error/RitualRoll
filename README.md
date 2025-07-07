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

---

## Estructura del proyecto:

```bash
RitualRoll/
├── 📜 Grimorio/               # 📖 Backend: lógica oculta, invocaciones API, controladores
│   ├── Circles/              # Módulos del backend (e.g., Dados, Chat, PDF, Mapas)
│   │   ├── dice/             # Lógica de dados y mecánicas
│   │   ├── chat/             # WebSockets para comunicación
│   │   ├── pdfs/             # Lectura y escritura de PDFs interactivos
│   │   └── tokens/           # Tokens, imágenes y avatares
│   ├── Encantamientos/         # Controladores REST o WebSocket (como routes o gateways)
│   ├── Sigilos/               # Modelos (schemas, DTOs)
│   ├── Artifacts/            # Servicios, utilidades compartidas (helpers)
│   ├── Sanctum/              # Configuración global del servidor (NestJS/FastAPI)
│   └── main.ts               # Punto de entrada del servidor

├── 🧱 ObsidianVault/          # 🗄️ Base de datos y migraciones (la “cripta” de datos)
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

├── 🧿 Relics/                 # 📁 Archivos subidos (tokens, música, imágenes, PDFs)
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


## 📜 Licencia

Este proyecto está bajo la licencia MIT. No incluye contenido oficial de White Wolf o Paradox Interactive, sólo herramientas que permiten jugar con reglas compatibles.
