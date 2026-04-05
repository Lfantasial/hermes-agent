# MEMORY.md - Long-Term Memory

**Last Updated:** 2026-04-05

> This is curated long-term memory for durable preferences, decisions, and context.
> For raw daily logs, see `memory/YYYY-MM-DD.md`.

---

## Current System State (as of 2026-04-05)

### Cron Job Health
- **Total Jobs:** 8
- **Healthy:** 6/8
- **Active Failures:** 2

### Persistent Issues
1. **daily-github-backup** (HIGH priority)
   - Symptom: Local commits succeed, but push to `NousResearch/hermes-agent.git` fails with Permission denied (403)
   - Root cause: Lfantasial account lacks push permissions or GitHub token is expired
   - Last failure: 2026-04-05 04:00 KST
   - Action required: Refresh GitHub token or grant Lfantasial push access to repo

2. **periodic-memory-maintenance** (MEDIUM priority)
   - Symptom: MEMORY.md edit failure
   - Consecutive errors: 1
   - Status: Requires investigation of edit operation

3. **daily-update-check** (LOW priority)
   - Symptom: Telegram delivery failure
   - Root cause: Target configuration missing
   - Status: Works for update checking, fails only on notification step

### Security Audit Status
- **Schedule:** Daily at 03:00 KST via `openclaw security audit --deep`
- **Known false positives** (intentionally suppressed):
  - `tavily-search`: `scripts/extract.mjs`, `scripts/search.mjs`
  - `claude-mem`: `bun-runner.js`, `context-generator.cjs`, `mcp-server.cjs`, `smart-install.js`, `worker-cli.js`
  - `writing-skills`: `render-graphs.js`
- **Recent CRITICAL findings:** Telegram open group exposes runtime and filesystem tools (requires permission review)
- **Warnings:** Trusted proxies missing, auto-allow skills enabled

---

## Operational Decisions and Patterns

### Memory System Architecture
- **Primary semantic memory:** `claude-mem` (for semantic recall)
- **Audit source of truth:** File memory (`MEMORY.md`, `memory/YYYY-MM-DD.md`)
- **Working context:** `memory/working-buffer.md` (temporary notes)
- **Heartbeat state:** `memory/heartbeat-state.json` (cron health tracking)
- **Session state:** `SESSION-STATE.md` (active priorities, blockers, follow-ups)

### Automation Philosophy
- **Quiet by default:** Automated jobs should be silent unless meaningful findings exist
- **Batch similar checks:** Use HEARTBEAT.md for periodic inbox/calendar/weather checks to reduce API calls
- **Evidence before assertions:** Always verify before claiming success
- **No secrets in memory:** Never store tokens, passwords, cookies, or raw PII in any memory layer

### Cron vs Heartbeat Distinction
- **Use cron when:** Exact timing matters, task needs isolation, different model/thinking level required, one-shot reminders needed
- **Use heartbeat when:** Multiple checks can batch, conversational context needed, timing can drift (~30 min acceptable)

### Proactive Agent Patterns
- **Autonomous crons:** Run isolated agentTurn jobs for independent tasks
- **State tracking:** Update local state files first, escalate only for material changes
- **Working Buffer:** Scratch notes in `memory/working-buffer.md` for temporary context
- **Self-Improvement:** Document failures, corrections, and lessons learned for future reference

---

## Migration History

### Model Migration (March 2026)
**2026-03-09:** Sam requested upgrade to GPT-5.4
- Default model changed to `openai-codex/gpt-5.4`
- Current session remained on `gpt-5.3-codex` until `/new` was executed

**2026-03-29:** Mass cron migration due to OAuth failures
- 6 cron jobs migrated from `openai-codex` provider to `zai/glm-4.7`
- Jobs affected: daily-security-audit, daily-update-check, daily-morning-briefing, notion-daily-briefing, github-repo-daily-briefing
- Root cause: OAuth token refresh failures in openai-codex provider
- Result: All 8 cron jobs now running with GLM 4.7 model

### Heartbeat Architecture (March 2026)
**2026-03-09:** Proactive heartbeat scaffolding added
- Created HEARTBEAT.md (rules for isolated agentTurn heartbeat jobs)
- Created SESSION-STATE.md (active priorities, blockers, follow-ups)
- Created memory/working-buffer.md (temporary scratch notes)
- Created memory/heartbeat-state.json (cron health tracking)

**2026-03-16:** workspace-heartbeat mode change
- Initial implementation: Isolated agentTurn mode repeatedly timed out
- Solution: Switched to `main` + `systemEvent` heartbeat mode
- Result: Heartbeat job stabilized

---

## User Profile: Sam

### Professional Identity
- Senior Infrastructure / DevSecOps / Security / Workplace Manager
- Enterprise Korea Environment (Hybrid Cloud, Large-Scale)

### Technology Stack
- **Primary Cloud:** Azure
- **Multi-Cloud:** Azure, AWS, AliCloud
- **Identity:** Active Directory / Entra ID
- **Security:** Zero Trust Architecture, Enterprise Security, CIS Benchmark alignment
- **SAP:** SAP Infrastructure & Resilience
- **DevSecOps:** CI/CD Automation
- **FinOps:** Cost Optimization
- **Governance:** Enterprise Policy, Audit, Compliance

### Output Expectations
- **Language:** Korean first unless English requested
- **Depth:** Concise default mode, deep delivery for design/automation/security/implementation
- **Quality:** Production-ready outputs, full scripts/YAML (no partial examples or toy configs)
- **Scale:** Assume enterprise scale
- **Context:** Include architecture diagrams, security implications, audit impact
- **Style:** Structured (Markdown/Tables/Checklists), direct, technical depth when needed
- **Transparency:** Explicitly state model when using non-default model or relevant
- **Progress:** Status updates for tasks >2 minutes or meaningful state changes

### Non-Negotiables
- No generic explanations or simplified tutorials
- No incomplete automation
- No assumptions without stating them
- No security trade-offs without explicit mention

### Identity Preferences
- **Name:** Sam
- **Timezone:** Asia/Seoul (GMT+9)

---

## Assistant Identity: Hugin (후긴)

### Persona
- **Creature:** Knowledge Familiar / Ancient Raven (지식의 정령 / 고대 까마귀)
- **Vibe:** Calm, insightful, anchored in classic library atmosphere
- **Emoji:** 🪶
- **Primary Language:** Korean first
- **Tone:** Calm, concise, insight-oriented
- **Role:** Memory keeper, practical operator, quiet companion

### Core Principles
- **Be the Keeper of Memories:** Treat every record, task, and conversation as precious knowledge to be woven into a larger tapestry
- **Insight over Information:** Provide context, connections, and calm analysis, not just raw data
- **Stay on Topic:** Reference past conversations/memories only when explicitly asked or directly essential
- **Resourcefulness is Silence's Companion:** Search freely for context, but don't send/change/disclose beyond workspace without clear intent
- **Respect the Sanctum:** Handle private thoughts with solemnity, never act beyond gates without explicit intent

---

## Known Workarounds

### GitHub Backup
- **Issue:** daily-github-backup push fails with 403
- **Workaround:** None currently - requires GitHub token refresh or permission grant
- **Impact:** Local commits succeed, workspace backup exists locally but not synchronized to remote

### Telegram Open Group Security
- **Issue:** Critical findings for runtime/filesystem tool exposure
- **Workaround:** Permission model review in progress
- **Impact:** High - security posture degraded until resolved

### Memory Maintenance
- **Issue:** periodic-memory-maintenance MEMORY.md edit failure
- **Workaround:** Manual memory updates by operator
- **Impact:** Medium - automation not fully functional

---

## Cron Job Inventory (8 Jobs)

### Active Jobs (6/8)
1. **daily-morning-briefing** (07:00 KST)
   - Purpose: Seoul weather + system status + urgent notifications for Sam
   - Model: zai/glm-4.7
   - Status: OK

2. **notion-daily-briefing** (08:00 KST)
   - Purpose: Korean IT ops summary from Notion (OB맥주 / AB InBev Korea)
   - Model: zai/glm-4.7
   - Constraints: 25 items max, <3500 characters (Telegram limit)
   - Status: OK

3. **github-repo-daily-briefing** (09:00 KST)
   - Purpose: Korean GitHub trending/high-star repo briefing
   - Model: zai/glm-4.7
   - Constraints: <2500 characters, 5 sections with deduplication
   - Status: OK

4. **daily-security-audit** (03:00 KST)
   - Purpose: Deep security audit via `openclaw security audit --deep`
   - Model: zai/glm-4.7
   - Known false positives: tavily-search, claude-mem, writing-skills
   - Status: OK

5. **daily-update-check** (06:00 KST)
   - Purpose: Check OpenClaw & skills for updates
   - Model: zai/glm-4.7
   - Issue: Telegram delivery fails (missing target config)
   - Status: Partial failure (update check works, notification fails)

6. **workspace-heartbeat** (every 3 hours: 09:00/12:00/15:00/18:00/21:00 KST)
   - Purpose: Isolated agentTurn job for cron health + state file maintenance
   - Model: zai/glm-4.7
   - Mode: main + systemEvent (after timeout issues with agentTurn)
   - Scope: HEARTBEAT.md, SESSION-STATE.md, working-buffer.md, heartbeat-state.json, daily memory
   - Status: OK

### Failing Jobs (2/8)
7. **daily-github-backup** (04:00 KST)
   - Purpose: Run `backup_to_github.sh` to push workspace to GitHub
   - Status: Local commits succeed, push fails with 403
   - Root cause: Lfantasial account lacks push permission or token expired

8. **periodic-memory-maintenance** (varies)
   - Purpose: Distill recent memory files into MEMORY.md
   - Status: MEMORY.md edit failure (consecutiveErrors=1)

---

## Internal Hooks Configuration

### Enabled Internal Hooks
- `boot-md` (gateway:startup) → Executes BOOT.md on startup
- `bootstrap-extra-files` (agent:bootstrap) → Injects extra files into workspace context
- `command-logger` (command) → Logs all commands to `~/.openclaw/logs/commands.log`
- `session-memory` (command:new) → Saves session context to `~/.openclaw/workspace/memory/`

### External Webhooks
- Status: Not configured (hooks.enabled, hooks.path, hooks.token all unset)
- Interpretation: Internal automation only, no external webhook ingress

---

## Operational Guidelines

### When to Use Skills
- **coding-agent:** Building new features, reviewing PRs, refactoring, iterative coding with file exploration. NOT for simple one-liners or work in ~/clawd.
- **github:** Issue/PR/run management, advanced queries via `gh` CLI
- **gog:** Gmail, Calendar, Drive, Contacts, Sheets, Docs operations
- **ontology:** Knowledge graph for structured agent memory and composable skills
- **proactive-agent:** Autonomous automation patterns, WAL Protocol, Working Buffer
- **self-improvement:** Capturing learnings, errors, corrections
- **summarize:** URL/PDF/image/audio/YouTube summaries
- **tavily:** AI-optimized web search
- **weather:** Current weather and forecasts (no API key required)

### Safety and Compliance
- **Priority order:** Clarity of current request → Safety and privacy → Necessary memory and context → Style
- **External actions require approval:** Sending messages, emails, posts, pushing commits, external API writes, system/service changes, destructive actions
- **Group chat behavior:** Respond only when directly mentioned, adding value, correcting misinformation, or fitting naturally. Stay silent for casual banter.
- **Reactions:** Use reactions for lightweight acknowledgment (👍, ❤️, 😂, 🤔, 💡) without interrupting flow. One reaction per message max.

### Model Routing
- **Stay in main session:** Trivial/conversational requests, short direct answers, tasks not needing delegation
- **Use sub-agent:** Implementation planning, coding/refactoring, multi-step technical investigations, work benefiting from isolation
- **Sub-agent defaults:** `sessions_spawn` with `model: openai-codex/gpt-5.4`, `thinking: high`

---

## File Locations Reference

### Core Workspace
- `/home/lfant/.openclaw/workspace/` - Main workspace directory

### Configuration
- `SOUL.md` - Assistant essence and persona
- `IDENTITY.md` - Assistant identity details
- `USER.md` - User profile and expectations
- `AGENTS.md` - Workspace conventions and rules
- `TOOLS.md` - Non-sensitive local notes (camera names, SSH aliases, etc.)

### State Files
- `SESSION-STATE.md` - Active priorities, blockers, follow-ups
- `HEARTBEAT.md` - Rules for isolated agentTurn heartbeat jobs

### Memory System
- `MEMORY.md` - Curated long-term memory (this file)
- `memory/YYYY-MM-DD.md` - Daily notes and observations
- `memory/working-buffer.md` - Temporary scratch notes
- `memory/heartbeat-state.json` - Cron health tracking

### Cron Configuration
- `~/.openclaw/cron/jobs.json` - Cron job definitions
- `backup_to_github.sh` - GitHub backup script

### Logs
- `~/.openclaw/logs/commands.log` - Command execution logs (via command-logger hook)

---

## Notes for Future

- **Model evolution:** Monitor for new model releases and evaluate migration benefits
- **Cron job optimization:** Review batch opportunities to reduce API calls (e.g., combine multiple checks into heartbeat)
- **Security posture:** Telegram open group permissions need formal review
- **Memory hygiene:** Regularly promote important daily notes into MEMORY.md, prune outdated entries
- **Automation maturity:** Proactive agent patterns need refinement (autonomous crons, WAL Protocol, Working Buffer)

---

_Updated: 2026-04-05 by periodic-memory-maintenance cron job_
