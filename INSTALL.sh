#!/data/data/com.termux/files/usr/bin/bash
# SYCAM-PUB V155 — installation Termux / Linux
set -e
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT/frontend"
echo "========================================"
echo " SYCAM-PUB V155 — Google + Innovation"
echo "========================================"
echo "Dossier: $ROOT/frontend"
echo ""
echo "1) Serveur local sur le port 8080..."
echo "2) Ouvrez Chrome: http://127.0.0.1:8080"
echo "3) Si ancienne page: vider le cache du site"
echo "4) Menu → Actualités → Actualiser Google"
echo "5) Menu → Bibliothèque → + Dépôt HAL"
echo "========================================"
# stop old server on 8080 if any
(pkill -f "python3 -m http.server 8080" 2>/dev/null) || true
python3 -m http.server 8080
