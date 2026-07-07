# Mnemosyne + built-in memory (Nous stack) — idempotent
$ErrorActionPreference = "Stop"
Write-Host "=== Install ===" -ForegroundColor Cyan
python -m pip install -U mnemosyne-hermes
Write-Host "=== Provider ===" -ForegroundColor Cyan
hermes config set memory.provider mnemosyne
hermes memory setup mnemosyne
Write-Host "=== Nous stack: keep built-in + Mnemosyne ===" -ForegroundColor Cyan
hermes config set memory.memory_enabled true
hermes config set memory.user_profile_enabled true
Write-Host "=== Restart gateway ===" -ForegroundColor Cyan
hermes gateway restart
Write-Host "=== Verify ===" -ForegroundColor Cyan
hermes memory status
hermes mnemosyne stats
Write-Host "Start /new in desktop chat to load full stack." -ForegroundColor Green