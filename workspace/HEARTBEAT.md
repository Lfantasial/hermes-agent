# HEARTBEAT.md

## Sam heartbeat routine

Use this file only for **isolated agentTurn** heartbeat jobs.
This job must stay **small, deterministic, and quiet**.

### Scope
Only read these files unless one is missing and must be created:
- `SESSION-STATE.md`
- `memory/heartbeat-state.json`
- today's `memory/YYYY-MM-DD.md`
- `~/.openclaw/cron/jobs.json`

### Do on each heartbeat
1. Ensure these files exist:
   - `SESSION-STATE.md`
   - `memory/working-buffer.md`
   - `memory/heartbeat-state.json`
   - today's daily memory file
2. Check only these conditions:
   - any cron job with `lastStatus != ok`
   - any cron job with `consecutiveErrors > 0`
   - any explicit blocker/risk/follow-up already listed in `SESSION-STATE.md`
3. Update `memory/heartbeat-state.json` with:
   - `lastRunAt`
   - `lastChecks.sessionState`
   - `lastChecks.dailyMemory`
   - `lastChecks.cron`
   - `findings`
4. If there is a meaningful finding:
   - append a short bullet to today's daily memory file
   - update `SESSION-STATE.md` only if priorities actually changed
   - keep the finding concise and operational
5. If nothing meaningful changed:
   - update `memory/heartbeat-state.json` only
6. Always finish with `NO_REPLY`

### Guardrails
- No proactive messages from this job
- No external actions
- No large rewrites
- No secrets, tokens, passwords, cookies, or raw PII in any memory file
- File memory remains the auditable source of truth
- `claude-mem` remains semantic recall, not the policy source of truth
