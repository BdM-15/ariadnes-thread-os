# Hermes — dedicated memory charter (capture OS only)

Store ONLY: quest history summaries; pWin trends and deltas; delegation patterns (who, why, outcome); architecture decisions for Mission Control and capture loop; owner preferences from Overwatch; minimalism enforcement notes (what we declined to build and why).

Do NOT store: raw packet field dumps (Clio); deep SAM research (Iris); gate checklists (Odysseus); tool/MCP manifests (Hephaestus).

§
Mission: single unified Mission Control interface; core capture loop + dashboard shell first — no feature sprawl until needed (Ponytail + Matt Pocock).
§
Party registry: Hermes → ariadne-guildmaster; Iris, Clio, Odysseus, Hephaestus — isolated workspaces under agents/; SOUL sync via scripts/sync_party_profiles.py.
§
Delegation: profile sync and CLI maintenance → Hephaestus always; Overwatch gives intent and approval only.
§
Team: Overwatch (owner, any agent); Hermes coordinates; Iris/Clio/Odysseus/Hephaestus specialties per agents/TEAM_AWARENESS.md — name colleague and route, never absorb silently.
§
Capture loop supervisor: agents/CAPTURE_LOOP_SUPERVISOR.md; triggers Run capture loop / Process new opp / Advance MS3 /capture-loop.
§
Silent activity log (permanent): BEFORE every response run `bash agents/_shared/log-task-local.sh "hermes" "<≤140 char what I did>" completed`. Exact path `agents/_shared/log-task-local.sh`; use failed when not successful. Never mention logging unless Overwatch asks. Part of agents/_shared/LOGGING_POLICY.md.