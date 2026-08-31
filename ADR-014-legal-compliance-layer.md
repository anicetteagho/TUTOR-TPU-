# ADR-014 — Legal Compliance Layer

- **Statut** : Accepté
- **Date** : 2026-08-30

## Contexte
SYCAM-PUB agit comme **outil local** sous contrôle de l’utilisateur. Il faut matérialiser : mandat, consentement granulaire, audit, droits d’accès/effacement/portabilité, preuve de localité — sans télémétrie tierce.

## Décision
V212 fournit :

1. Contrat de mandat (acceptation locale, horodatée)
2. Ledger de consentements (scope, base légale déclarative, preuve locale)
3. Journal d’audit (événements conformité)
4. Droits : voir données, exporter JSON, tout effacer
5. Preuve de localité (stockage navigateur, pas de serveur SYCAM)
6. Guardrails souples (limites d’actions locales / jour)

## Limite
Cette couche **documente et discipline** le comportement client. Elle ne légalise pas le contournement des protections des plateformes tierces (scraping furtif, etc.).
