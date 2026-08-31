# ADR-019 — Rattachement appareil à la demande

- **Statut** : Accepté
- **Date** : 2026-08-30

## Contexte
SYCAM-PUB doit pouvoir **faire partie de l’appareil** quand l’utilisateur le demande : backend Termux local (`127.0.0.1`), mode installé (PWA), pont notifications futur — sans être un service invasif permanent ni un scraper.

## Décision
V217 `SycamV217` :

1. Découverte de backends locaux (ports connus)
2. **Attach / Detach** explicite (consentement V212)
3. Bascule `SycamV215` API base vers `http://127.0.0.1:PORT`
4. Guide Termux (install one-liner documenté)
5. Stub `/ingest` contract pour future UI native

## Non-objectifs
Pas de Playwright furtif, pas d’AccessibilityService, pas d’APK Kotlin dans ce ZIP.
