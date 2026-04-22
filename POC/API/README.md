# API

API Node.js / Express pour recevoir et lire l'altitude et l'orientation de l'avion.

## Installation
```bash
npm install
```

## Lancement
```bash
node server.js
```

## URL
- API : http://localhost:5000

## Routes
- `GET /` : test API
- `POST /api/avion` : enregistrer altitude + orientation
- `GET /api/avion` : récupérer la dernière position
- `GET /api/avion/update?altitude=...&orientation=...` : enregistrer via GET
