# ADR-004 — Intégration HAL (lecture + import)

- **Statut** : Accepté

## Décision
Consommer `api.archives-ouvertes.fr` en **lecture** (CORS), cache local, import vers `sycam_deposits` + ID SYCAM. Pas d’écriture HAL tant que les comptes institutionnels ne sont pas ouverts.

## Conséquences
Enrichit le corpus camerounais/africain sans attendre une fédération complète.
