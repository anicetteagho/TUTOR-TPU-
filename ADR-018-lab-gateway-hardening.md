# ADR-018 — Durcissement Labo + Passerelle

- **Statut** : Accepté
- **Date** : 2026-08-30

## Contexte
Le pack Labo prêt (V214) et la passerelle Jarvis (V215) doivent être reliés : score institutionnel = modules + conformité + **santé API** + **absence de secrets dans le client**.

## Décision
V216 :

1. Scan client : motifs de clés (`AIza`, `sk-`, `api_key=`) dans scripts inline / localStorage sycam
2. Health check optionnel de la passerelle
3. Extension checklist / score lab
4. Rapport unique `security+gateway+lab`

## Non-objectifs
Pas d’app Android. Pas de stockage de secrets côté client.
