# Mnemosyne + built-in memory (Nous stack)

**Date:** 2026-07-05 (updated)  
**Mode:** Built-in MEMORY/USER **+** Mnemosyne provider (additive per Hermes docs).

## Config

```yaml
memory:
  memory_enabled: true
  user_profile_enabled: true
  provider: mnemosyne
```

## On-disk built-in (preserved)

- `%HERMES_HOME%/memories/MEMORY.md` (~2204 bytes)
- `%HERMES_HOME%/memories/USER.md` (~1299 bytes)

## Verify after `/new`

1. `hermes memory status` → Built-in always active + mnemosyne ← active  
2. System prompt should include **MEMORY** and **USER** blocks **and** Mnemosyne prefetch/context.  
3. `hermes mnemosyne stats` → working memories present.  
4. Ask: *What is my default prime?* → **KBR** (from USER).  
5. Ask: *EAGLE MS1 pWin test phrase?* → **EAGLE-MS1-pWin-2026-07-05** (Mnemosyne).

## Setup script

`scripts/setup_mnemosyne_hermes.ps1` (keeps both flags true)