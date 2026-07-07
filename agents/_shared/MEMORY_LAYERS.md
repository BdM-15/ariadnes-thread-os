# Memory layers (Ariadne Thread)

| Layer | Location | Use for |
|-------|----------|---------|
| **Capture SSOT** | `knowledge/` + `VAULT_RETRIEVE.md` | Pursuits, entities, competitors, trusted claims |
| **Party artifacts** | `agents/<agent>/content/` | Long-form deliverables (Content tab) |
| **Board** | `scripts/board_add_task.py` / `board.db` | Actionable tasks |
| **Hermes continuity** | **Built-in** `%HERMES_HOME%/memories/MEMORY.md` + `USER.md` **and** Mnemosyne (`provider: mnemosyne`) | Nous stack: built-in injects every turn; provider augments + mirrors writes |
| **Not for intel** | Mnemosyne / chat memory | BOA status, due dates, pricing — always vault + evidence |

**Nous default:** `memory_enabled: true`, `user_profile_enabled: true`, `provider: mnemosyne`. Mnemosyne-only (both flags false) is optional Mnemosyne vendor mode, not Hermes default.