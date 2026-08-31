# ADR-007 — Certification des modules

- **Statut** : Accepté
- **Date** : 2026-08-30

## Contexte
Sans contrat explicite, un module peut modifier silencieusement le comportement d’un autre (régression UX, dette cachée). JARVIS APEX aura besoin d’un **Capability Registry** fiable.

## Décision
Tout module `sycam-vXXX` doit exposer un **manifest** :

```json
{
  "id": "sycam-v205",
  "version": "205.0.0",
  "requires": ["sycam-v204"],
  "provides": ["plugin.certification"],
  "modifies": [],
  "routes": ["mission"],
  "storage": [],
  "events": [],
  "permissions": []
}
```

Pipeline de certification : Structure, Version, Registry, ADR, Dependencies, Forbidden imports, Navigation, API contract, Storage policy → **CERTIFIED** ou **REJECTED**.

## Règle d’or
`modifies` non vide exige une justification ADR. Aucune modification silencieuse.
