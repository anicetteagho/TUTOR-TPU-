# ADR-010 — Universal Workflow Engine

- **Statut** : Accepté
- **Date** : 2026-08-30

## Contexte
JARVIS (V209) doit exécuter des **enchaînements** d’actions, pas des appels isolés. Chaque étape doit rester gouvernée (V205 cert, V206 security, V207 plan/gate).

## Décision
Un moteur de workflows :

1. Définitions versionnées (id, steps[], confirm policy)
2. Instances persistées (`sycam_workflows_v208`)
3. États : `pending | running | await_confirm | completed | failed | cancelled`
4. Chaque step appelle `SycamV207.invoke` (capability gate)
5. Steps sensibles : confirmation utilisateur obligatoire

## Conséquences
Base d’exécution réelle pour JARVIS APEX sans agent UI aveugle.
