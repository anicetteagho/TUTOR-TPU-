# ADR-012 — Logiciel SYCAM NEXUS

- **Statut** : Accepté
- **Date** : 2026-08-30

## Contexte
V209 a posé JARVIS comme orchestrateur. Il faut un **logiciel NEXUS** dédié : mesh de capacités, connecteurs, bus de ressources, centre de consentement — sans recopier Google/YouTube/Facebook.

## Décision
Livrer `SycamV210` (NEXUS Software) :

1. **Capability Mesh** — registry unifié capability → providers
2. **Connectors** — adaptateurs (sycam, hal, local-ai, stubs OAuth)
3. **Resource Bus** — modèle `sycam:resource:*` commun
4. **Consent Center** — UI + historique niveaux 1/2/3
5. **Personal Capability Graph** — ce que l’utilisateur peut faire *maintenant*
6. **Execute path** — `Nexus.execute(capability, payload)` → connecteur → résultat normalisé

## Contraintes
Offline-first · pas de clé API dans le client · OAuth réel = backend futur · pas de contournement.
