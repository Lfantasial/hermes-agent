# SESSION-STATE.md

**Updated:** 2026-04-02T04:09:00+09:00
**Status:** active

## Current focus
- Memory baseline: `claude-mem` for semantic recall, file memory as auditable source of truth, proactive heartbeat for low-noise continuity.
- Current task: keep local session-state aligned with current cron health and active priorities.
- Cron health: 6/8 jobs healthy, 2 jobs with issues (daily-github-backup push failure, periodic-memory-maintenance edit failure)

## Active tasks
- [ ] Resolve daily-github-backup push failure: GitHub token expired or permission denied (403) to NousResearch/hermes-agent.git (last failure: 2026-04-02 04:00 KST)
- [x] Validate heartbeat state-file update path (manual verification completed)
- [x] Reconfirm `github-repo-daily-briefing` cron health after the 2026-03-11 09:00 KST failure
- [x] Investigate and resolve workspace-heartbeat job timeout (resolved 2026-03-16T15:26)
- [x] Confirm `workspace-heartbeat` timeout condition is cleared (confirmed at 12:00 KST)
- [x] Refresh stale follow-up items in local state files when cron health changes
- [x] Migrate 6 failing cron jobs from openai-codex to zai/glm-4.7 due to OAuth token refresh failures (2026-03-29)
- [x] Distill recent memory files into MEMORY.md during periodic memory maintenance (2026-03-29)

## Decisions
- `claude-mem` remains the primary semantic memory layer
- `MEMORY.md` and `memory/YYYY-MM-DD.md` remain the durable file-memory system of record
- Proactive automation should be quiet by default and only escalate meaningful findings
- GLM 4.7 (zai/glm-4.7) is now the primary model for cron jobs after mass OAuth failures

## Risks / watch items
- **HIGH**: daily-github-backup cannot push to GitHub (Permission denied 403) — local commits succeed but remote sync broken
- The proactive loop was previously only partially implemented
- Avoid storing secrets, tokens, cookies, or raw PII in any memory layer
- Prevent drift between semantic memory and file memory by treating file memory as policy/audit SoT

## Next actions
- Keep heartbeat quiet-by-default while tracking cron failures or state drift in local files
- Continue monitoring for any new security issues or operational anomalies
