# ADR-011 — JARVIS NEXUS APEX (orchestration légère)

- **Statut** : Accepté
- **Date** : 2026-08-30

## Contexte
SYCAM-PUB doit unifier outils et IA **sans** hébergement/GPU lourds, **sans** clés API dans le navigateur, **sans** contourner OAuth.

## Décision
JARVIS est l’**orchestrateur** ; les IA (Gemini, locale…) et services (HAL, SYCAM) sont des **nœuds de capacités**.

Couches livrées en V209 (client-first) :

1. **SYCAM CONNECT** — statut des fournisseurs + consentement
2. **Capability Mesh** — providers → capabilities
3. **Consent Broker** — niveaux lecture / préparation / action externe
4. **AI Provider Router** — local d’abord ; cloud seulement si connecté + autorisé
5. **Plan → Workflow (V208) → Gate (V207)** — exécution gouvernée

## Interdits
- Clés API dans `index.html`
- Contournement mots de passe / sessions
- Promesse d’IA cloud « illimitée gratuite »

## Évolution
Quand un backend `/api/jarvis` existe, le Router envoie au serveur (secrets côté serveur) sans changer le contrat client.
