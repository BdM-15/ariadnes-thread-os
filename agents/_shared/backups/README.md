# Mission Control backups (Ponytail discipline)

**Owner:** the **agent party** — not Overwatch. **Hephaestus** runs `backup-mission-control.sh` before editing `index.html` / `server.py`; **Hermes** enforces the rule when coordinating dashboard work. Overwatch provides intent/approval only and does **not** run backup or maintenance commands.

Before **any** change to project-root `index.html` or `server.py`:

1. Run from repo root:
   ```bash
   bash agents/_shared/backup-mission-control.sh
   ```
   Or pass an explicit version: `bash agents/_shared/backup-mission-control.sh 1.1`

2. Then edit `index.html` / `server.py`.

3. After a meaningful change set, bump `agents/_shared/MC_VERSION.txt` and the nav badge in `index.html` (e.g. v1.1).

## Naming

- `index_v{version}_{YYYY-MM-DDThh-mm}.html`
- `server_v{version}_{YYYY-MM-DDThh-mm}.py`

Version uses dots in the filename (e.g. `1.0` → `v1.0` in the name).

Never skip backups — even small edits.