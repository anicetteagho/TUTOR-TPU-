#!/bin/sh
# SYCAM-PUB — démarrage local
cd "$(dirname "$0")"
echo "SYCAM-PUB $(cat VERSION 2>/dev/null)"
echo "Serveur http://127.0.0.1:8000"
echo "Codespaces : ouvrez l'onglet Ports → 8000"
python3 -m http.server 8000
