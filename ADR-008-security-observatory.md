# ADR-008 — Security Observatory

- **Statut** : Accepté
- **Date** : 2026-08-30

## Contexte
Avant auth serveur / JWT / MFA, le frontend offline stocke des données locales. Il faut **observer** les risques : permissions déclarées, clés sensibles, secrets accidentels, politiques de storage.

## Décision
Un **Security Observatory** (V206) scanne au runtime :

1. Permissions déclarées dans les manifests (V205)
2. Clés `localStorage` suspectes (token, password, secret, apiKey…)
3. Respect du préfixe `sycam_`
4. Absence de `localStorage.clear` / eval dans les modules chargés
5. Score Security + liste d’actions correctives

## Non-objectifs (phase actuelle)
Ne pas implémenter JWT/OAuth complet tant que le plan de données reste local (ADR-002). Préparer le terrain pour V207–V209.
