# ADR-002 — Plan de données localStorage

- **Statut** : Accepté
- **Date** : 2026-08

## Contexte
Pas de Postgres/Prisma obligatoire pour la phase terrain. Firebase Storage inaccessible (quota Blaze).

## Décision
Clés préfixées `sycam_*` dans `localStorage` (posts, deposits, citations, profile, caches HAL…). Export/import JSON pour sauvegarde.

## Conséquences
- **+** Zéro infra pour démo et labo
- **−** Limite ~5 Mo ; pas multi-appareil natif
- **Évolution** : API Railway/Neon optionnelle derrière le même contrat de données
