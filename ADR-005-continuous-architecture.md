# ADR-005 — Continuous Architecture (Observatories)

- **Statut** : Accepté
- **Date** : 2026-08-30

## Contexte
Après stabilisation fonctionnelle (V190–V203), ajouter des features sans **observabilité** augmente la dette et masque les régressions.

## Décision
Mettre en place un **Mission Control** et des observatoires :

1. Health Registry des modules `SycamV*`
2. Graphe de dépendances runtime
3. Linter d’architecture (règles SPA)
4. Tableau de dette technique (heuristiques)
5. ADR obligatoires pour décisions structurantes

## Non-objectifs (pour l’instant)
Ne pas imposer Prisma/Redis/EventBus tant que le plan de données reste localStorage-first (ADR-002).

## Conséquences
Le développement devient : construire → exécuter → mesurer → corriger → re-mesurer.
