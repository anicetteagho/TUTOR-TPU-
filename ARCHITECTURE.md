# SYCAM-PUB V146 — Architecture & Audit V145

## Ordre respecté
Audit → carte canonique → façade stockage → diagnostics → pas de refonte destructive.

## A. Modules existants (V145 → V146)
41 modules V145 + 3 modules consolidation :
- sycam-registry.js (routes canoniques)
- sycam-storage.js (façade LS/IDB)
- sycam-diagnostics.js (tests honnêtes)

## B. Pages / surfaces (panels DOM)
~274 ids `vNNN-*` historiques (accumulation V107–V145).
Surfaces unifiées prioritaires : home, explore, new, events, lab, dashboard, messages, notifications, profile, jarvis, backup, qa.

## C. Fonctionnalités
Réseau/social local, publications, explorer types, compositeur, messages, notifs, labo, events, Jarvis local, ORCID UI, citations, score, offline/sync queue, backup full, IDB, PWA shell, QA open-tests, community/institutions panel, backend Node optionnel.

## D. Doublons (conservés volontairement en V146)
| Legacy | Unifié | Pourquoi conservé |
|--------|--------|-------------------|
| sycam-events.js | events-ui.js | V141 gardes + ordre scripts ; suppression brutale risquée |
| sycam-lab.js | lab-ui.js | idem |
| sycam-dashboard.js | dashboard-ui.js | idem |
| sycam-notifs.js | notifications.js | API parallèle encore référencée |
| sycam-backup.js | backup-full.js | full étend base sans la supprimer |

**Doublons « supprimés » en V146 :** 0 fichiers (politique no-break).  
**Doublons documentés / préférés via Registry :** 5 paires.

## E. Conflits connus
- Assignations multiples `SycamRouter` / `SycamEvents` / `SycamLab` / `SycamDashboard` (atténués V141–V145).
- FAB historiques multiples (harden masque une partie).

## F. Fonctions peu ou pas reliées
- Certaines routes admin/watch/news sans moteur réseau réel.
- Firebase runtime : mentions code/config, **NON_TESTE** hors appareil.

## G. Risques
- Monolithe index.html ~2,1 Mo.
- localStorage + IDB : dual-read edge cases si migration incomplète.
- Service Worker cache peut servir ancienne version.

## H. Dépendances
Router hooks chaînés → Harden → BootFix ; IDB avant modules données ; Backup-full après Backup + IDB.

## I. Architecture actuelle
SPA Termux → modules JS globaux `Sycam*` → stockage LS/IDB → backup JSON → API Node optionnelle.

## J. Architecture recommandée (cible progressive)
1. Registry routes (fait V146)
2. Storage facade (fait V146)
3. Diagnostics honnêtes (fait V146)
4. Prochaine : FeedEngine unique, retirer legacy quand status() 100% + QA open verte
5. Ensuite seulement dataset/software pages dédiées

## Règle
Une fonctionnalité = une destination Registry. Jarvis reste transversal (ouvre routes), pas une 2e nav.
