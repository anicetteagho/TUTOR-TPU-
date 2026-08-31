# ADR-009 — AI / JARVIS Observatory

- **Statut** : Accepté
- **Date** : 2026-08-30

## Contexte
JARVIS APEX ne doit pas manipuler librement l’UI. Il doit passer par des **capabilities certifiées** (V205) et respecter le **score sécurité** (V206).

## Décision
V207 introduit un observatoire IA qui :

1. Journalise les intentions / appels (localStorage)
2. Résout une intention vers des capabilities (`publication.create`, `hal.search`, …)
3. Refuse l’exécution si le module n’est pas CERTIFIED ou si Security score < seuil
4. Mesure latence, succès, refus, mode offline/mock

## Non-objectifs
Pas encore d’appel LLM réel obligatoire : le pipeline et la gouvernance d’abord (V208 Workflow, V209 APEX).
