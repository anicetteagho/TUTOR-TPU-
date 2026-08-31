# ADR-013 — Local Data Bridge

- **Statut** : Accepté
- **Date** : 2026-08-30

## Contexte
Unifier les données de l’utilisateur **sans** scraping furtif ni contournement OAuth. Stratégie : l’utilisateur apporte ses fichiers (exports officiels) ; SYCAM les traite **en local** ; les actions sensibles demandent un **OK**.

## Décision
V211 `SycamV211` :

1. Import fichier (JSON, CSV, TXT, MD, PDF texte brut si collé, ZIP listing)
2. Détection de type + parsing local
3. Proposition d’actions (ressources NEXUS, notes, publications brouillon)
4. Consentement explicite avant écriture
5. Audit local

## Interdits
Stealth browser, login auto comptes tiers, contournement captcha/bot.
