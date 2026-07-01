#!/usr/bin/env bash
# Backup index.html and server.py before Mission Control edits.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
BACKUP_DIR="$ROOT/agents/_shared/backups"
VER_FILE="$ROOT/agents/_shared/MC_VERSION.txt"
VER="${1:-$(tr -d '\r\n' < "$VER_FILE" 2>/dev/null || echo 1.0)}"
TS="$(date +%Y-%m-%dT%H-%M)"
mkdir -p "$BACKUP_DIR"
cp "$ROOT/index.html" "$BACKUP_DIR/index_v${VER}_${TS}.html"
cp "$ROOT/server.py" "$BACKUP_DIR/server_v${VER}_${TS}.py"
echo "Backed up to $BACKUP_DIR"
echo "  index_v${VER}_${TS}.html"
echo "  server_v${VER}_${TS}.py"