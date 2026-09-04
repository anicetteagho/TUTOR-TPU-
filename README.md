# SYCAM-PUB v232 — prêt à lancer

Pack **minimal** : uniquement les fichiers de la version mobile améliorée.

## Codespaces / github.dev (votre cas)

1. Supprimez ou ignorez les anciens `index.v14x.backup.html`.
2. Copiez **tout le contenu** de ce dossier `sycam-pub/` à la **racine** du dépôt
   (ou gardez le dossier et ouvrez `sycam-pub/index.html` via le serveur).
3. Terminal Codespaces :
```bash
cd sycam-pub   # si vous gardez le sous-dossier
python3 -m http.server 8000
```
4. Onglet **Ports** → port **8000** → icône globe / « Open in Browser ».

Ne lancez **pas** l’ancien index trop long : le bon fichier fait ~50 lignes et charge `assets/js/sycam-v*.js`.

## Termux / téléphone

```bash
unzip -o SYCAM-PUB-LAUNCH-V232.zip
cd sycam-pub
python -m http.server 8080
```
Chrome → `http://127.0.0.1:8080`

## Fonctions

| Zone | Action |
|------|--------|
| Accueil | Tuiles carrées + stories |
| Actualités | Écran dédié (tuile 📰) + HAL |
| Explorer | Recherche HAL live |
| Publier | Article / Dataset / PDF / Vidéo |
| Réseau | Messages locaux |
| Plus | Hub complet + Santé QA |
| Démo | Bouton violet « Démo 5 min » |

## Version

`232.0.0-clean-hal`
