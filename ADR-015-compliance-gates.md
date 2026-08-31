# ADR-015 — Gates de conformité sur NEXUS & Bridge

- **Statut** : Accepté
- **Date** : 2026-08-30

## Contexte
V212 fournit mandat + ledger. Les écritures L2/L3 de V210 (`execute`) et V211 (`applyAction`) doivent passer par `SycamV212.requestAction`.

## Décision
V213 enveloppe :

1. `SycamV210.execute` → gate avant connecteur
2. `SycamV211.applyAction` → gate avant écriture Resource Bus / notes / pubs
3. Skip si mandat absent → message MANDATE_REQUIRED
4. Skip si utilisateur refuse → pas d’écriture

## Non-objectifs
Pas de NotificationListener Android dans cette version.
