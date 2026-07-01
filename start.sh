#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
export ARIADNE_ROOT="$(pwd)"
URL="http://127.0.0.1:51763/"

echo "Starting Ariadne Mission Control on ${URL}"

if command -v python >/dev/null 2>&1; then
  PY=python
elif command -v python3 >/dev/null 2>&1; then
  PY=python3
else
  echo "Python not found on PATH" >&2
  exit 1
fi

open_browser() {
  if command -v cmd.exe >/dev/null 2>&1; then
    cmd.exe /c start "" "${URL}" 2>/dev/null || true
  elif command -v explorer.exe >/dev/null 2>&1; then
    explorer.exe "${URL}" 2>/dev/null || true
  fi
}

api_ok() {
  curl -sf "${URL}api/snapshot" >/dev/null 2>&1
}

clear_stale_port() {
  if ! command -v netstat >/dev/null 2>&1; then
    return 0
  fi
  local pids
  pids=$(netstat -ano 2>/dev/null | grep ':51763' | grep LISTENING | awk '{print $NF}' | sort -u || true)
  for pid in $pids; do
    if [ -n "${pid}" ] && [ "${pid}" != "0" ]; then
      taskkill //F //PID "${pid}" 2>/dev/null || true
    fi
  done
}

if api_ok; then
  echo "Mission Control already running at ${URL}"
  open_browser
  exit 0
fi

if netstat -ano 2>/dev/null | grep -q ':51763.*LISTENING'; then
  echo "Port 51763 is busy but API did not respond — clearing stale listeners..." >&2
  clear_stale_port
  sleep 1
fi

"$PY" server.py &
SERVER_PID=$!

cleanup() {
  kill "${SERVER_PID}" 2>/dev/null || true
}
trap cleanup EXIT INT TERM

for _ in $(seq 1 40); do
  if api_ok; then
    break
  fi
  if ! kill -0 "${SERVER_PID}" 2>/dev/null; then
    echo "server.py exited before becoming ready (often: port 51763 already in use)." >&2
    echo "Try: bash start.sh   (reuses an existing instance) or close other listeners on 51763." >&2
    exit 1
  fi
  sleep 0.25
done

if ! api_ok; then
  echo "Mission Control did not respond on ${URL}" >&2
  exit 1
fi

open_browser
wait "${SERVER_PID}"