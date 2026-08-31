# ADR-001 — SPA modulaire offline-first

- **Statut** : Accepté
- **Date** : 2026-08
- **Décideurs** : Équipe SYCAM-PUB

## Contexte
Les utilisateurs cibles (Cameroun / Afrique) travaillent souvent hors ligne ou sur mobile (Termux, Chrome). Un monolithe serveur-only bloque l’adoption.

## Décision
SYCAM-PUB est une **SPA** : un `index.html` + modules `sycam-vXXX-*.js` versionnés. Chaque version ajoute une capacité sans casser les précédentes (`SycamV190`, `SycamV191`, …).

## Conséquences
- **+** Fonctionne sans backend au démarrage
- **+** Livraison par ZIP incrémental
- **−** Risque de duplication si les modules ne se enregistrent pas dans un registre
- **Mitigation** : Health Registry + Architecture Linter (V204)
