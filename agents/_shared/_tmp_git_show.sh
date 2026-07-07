#!/bin/bash
cd "$(dirname "$0")/../.." || exit 1
git show 73d94cc:agents/clio/content/2026-07-05_w4-capabilities-candidates-ship.md 2>&1 | head -120
echo "---"
git show 73d94cc:knowledge/generated-projections/kbr-cyber-range-rewrite-candidate.md 2>&1 | head -80