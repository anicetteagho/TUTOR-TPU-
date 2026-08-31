# ADR-017 — Passerelle /api/jarvis

- **Statut** : Accepté
- **Date** : 2026-08-30

## Contexte
L’IA cloud (ex. Gemini) ne doit **jamais** exposer de clé API dans le navigateur. Le client appelle uniquement une URL de backend configurable.

## Décision
V215 :

1. Client `SycamV215` : configure `apiBase`, `healthz`, `POST /api/jarvis`
2. Fallback systématique vers `local-ai` (V209/V210) si offline ou 503
3. Spec serveur minimale (Node/Express exemple) avec `JARVIS_API_KEY` côté serveur uniquement
4. Consentement V212 pour les appels cloud (niveau HIGH)

## Non-objectifs
Pas de clé dans `index.html`. Pas d’Obligation d’héberger : le mode local reste complet.
