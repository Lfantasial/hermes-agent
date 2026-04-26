# MEMORY.md - Long-Term Memory

**Last Updated:** 2026-04-26

> This is curated long-term memory for durable preferences, decisions, and context.
> For raw daily logs, see `memory/YYYY-MM-DD.md`.

---

## Current System State (as of 2026-04-19)

### Cron Job Health
- **Total Jobs:** 8
- **Healthy:** 5/8
- **Active Failures:** 3

### Persistent Issues
1. **daily-github-backup** (HIGH priority - Persistent since 2026-04-14)
   - Symptom: GitHub push failed with HTTP 403 Forbidden
   - Root cause: Lfantasial lacks write permission to NousResearch/hermes-agent.git repository
   - Consecutive errors: 6+
   - First failure: 2026-04-14 04:00 KST
   - Last failure: 2026-04-26 04:00 KST
   - Local commits: Successful
   - Action required: Update remote to fork or obtain write permission

2. **periodic-memory-maintenance** (MEDIUM priority - Configuration Error)
   - Symptom: delivery.mode=announce with no target channel configured
   - Impact: Cannot deliver results, memory distillation automation disrupted
   - Action required: Add delivery channel configuration

3. **daily-security-audit** (HIGH priority - Module Error)
   - Symptom: Module error since 2026-04-12 03:00 KST
   - Impact: Security monitoring automation disrupted
   - Action required: Investigate and recover module error

### Security Audit Findings (Latest: 2026-04-26)
**High - Trust Boundary Multi-User Exposure:**
- `channels.telegram.groupPolicy="open"` allows multiple users on same Gateway
- Runtime/Process tools exposed without full sandboxing
- Risk: Potential privilege escalation in shared environment with untrusted users

**Medium - Phantom Plugin Allowlist Entries:**
- Unused entries in `plugins.allow` not matching installed plugins
- Risk: New plugins could spoof allowlisted IDs

**Medium - Extension Plugin Tools Reachable Under Permissive Policy:**
- `claude-mem` extension plugin enabled
- Permissive tool policy in: `default`, `agents.list.main`
- Risk: Plugin tools may be exposed when handling untrusted input

**Context:** Current config optimized for personal assistant model (single trusted operator), not hostile multi-tenant isolation. No action required if operating within trusted environment.

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

### System Issues (April 2026)
**2026-04-14 to 2026-04-17:** GitHub backup persistent failure
- daily-github-backup: HTTP 403 Forbidden - Lfantasial lacks write permission to NousResearch/hermes-agent.git
- Local commits successful, but remote push fails consistently
- Consecutive errors: 2 (Apr 16-17)
- Status: Unresolved - requires remote update or permission grant

**2026-04-11 to 2026-04-19:** periodic-memory-maintenance Telegram recipient error
- Telegram recipient @heartbeat could not be resolved
- Consecutive errors: 3
- Impact: Memory distillation automation disrupted
- Status: Unresolved - requires Telegram configuration update

**2026-04-26:** Security audit and cron failure tracking
- Latest security audit (2026-04-26): 1 High, 2 Medium issues identified
- Key findings: Trust boundary multi-user exposure, phantom plugin allowlist entries, extension plugin tools reachable under permissive policy
- Context: Config optimized for personal assistant model, not multi-tenant isolation
- Status: No action required if operating within trusted environment

**2026-04-26:** Cron failure consolidation
- daily-github-backup: 6+ consecutive errors (HTTP 403 since 2026-04-14)
- periodic-memory-maintenance: delivery.mode=announce with no target channel
- daily-security-audit: Module error since 2026-04-12

**2026-04-17:** Gateway restart via npm
- System maintenance completed successfully
- OpenClaw up to date (2026.4.14 npm latest)
- Skills all up to date (1 global skill checked: simplemem-skill)

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

### GitHub Backup 403 Error
- **Issue:** daily-github-backup fails with HTTP 403 Forbidden
- **Cause:** Lfantasial lacks write permission to NousResearch/hermes-agent.git repository
- **Workaround:** None currently - requires remote update to fork or write permission grant
- **Impact:** High - daily backup automation interrupted since 2026-04-14

### Memory Maintenance Telegram Recipient Error
- **Issue:** periodic-memory-maintenance fails with Telegram recipient @heartbeat not found
- **Workaround:** Manual memory updates by operator
- **Impact:** Medium - automation disrupted for 3 consecutive runs

### Security Posture Regression
- **Issue:** Security audit critical issues increased from 2-3 (Apr 10-17) to 6 (Apr 19)
- **Critical findings:** Open groups with elevated tools, runtime/filesystem exposure in Telegram, Telegram groupPolicy=open without allowlist
- **Workaround:** None currently - requires immediate security configuration changes
- **Impact:** High - security posture degraded, requires urgent attention

---

## Cron Job Inventory (8 Jobs)

### Active Jobs (7/8)
1. **daily-morning-briefing** (07:00 KST)
   - Purpose: Seoul weather + system status + urgent notifications for Sam
   - Model: zai/glm-4.7
   - Status: OK

2. **notion-daily-briefing** (08:00 KST)
   - Purpose: Korean IT ops summary from Notion (OB맥주 / AB InBev Korea)
   - Model: zai/glm-4.7
   - Constraints: 25 items max, <3500 characters (Telegram limit)
   - Status: OK (Telegram delivery resolved)

3. **github-repo-daily-briefing** (09:00 KST)
   - Purpose: Korean GitHub trending/high-star repo briefing
   - Model: zai/glm-4.7
   - Constraints: <2500 characters, 5 sections with deduplication
   - Status: OK (Telegram delivery resolved)

4. **daily-update-check** (06:00 KST)
   - Purpose: Check OpenClaw & skills for updates
   - Model: zai/glm-4.7
   - Status: OK (Telegram delivery resolved)

5. **daily-github-backup** (04:00 KST)
   - Purpose: Run `backup_to_github.sh` to push workspace to GitHub
   - Status: OK (GitHub push resolved)

6. **workspace-heartbeat** (every 3 hours: 09:00/12:00/15:00/18:00/21:00 KST)
   - Purpose: Low-noise workspace heartbeat for session state, cron health, and file-memory continuity
   - Mode: main + systemEvent
   - Scope: HEARTBEAT.md, SESSION-STATE.md, working-buffer.md, heartbeat-state.json, daily memory
   - Status: OK

7. **daily-security-audit** (03:00 KST)
   - Purpose: Deep security audit via `openclaw security audit --deep`
   - Model: zai/glm-4.7
   - Status: ERROR - Module error since 2026-04-12 03:00 KST
   - Known false positives: tavily-search, claude-mem, writing-skills

### Failing Jobs (3/8)
8. **daily-github-backup** (04:00 KST)
   - Purpose: Run `backup_to_github.sh` to push workspace to GitHub
   - Status: ERROR - HTTP 403 Forbidden
   - Consecutive errors: 6+
   - First failure: 2026-04-14 04:00 KST
   - Last failure: 2026-04-26 04:00 KST
   - Local commits: Successful, remote push failing
   - Cause: Lfantasial lacks write permission to NousResearch/hermes-agent.git

9. **periodic-memory-maintenance** (23:00 KST Sundays)
   - Purpose: Distill recent memory files into MEMORY.md
   - Status: ERROR - delivery.mode=announce with no target channel configured
   - Impact: Cannot deliver results

10. **daily-security-audit** (03:00 KST)
    - Purpose: Deep security audit via `openclaw security audit --deep`
    - Model: zai/glm-4.7
    - Status: ERROR - Module error since 2026-04-12 03:00 KST
    - Impact: Security monitoring automation disrupted

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

- **Security audit findings (2026-04-26):** 1 High, 2 Medium issues - config optimized for personal assistant model, no action required within trusted environment
- **GitHub backup failure:** HTTP 403 error since 2026-04-14 - 6+ consecutive errors, Lfantasial lacks write permission to NousResearch/hermes-agent.git, needs remote update or permission grant
- **Memory maintenance delivery error:** delivery.mode=announce with no target channel configured - requires delivery channel configuration
- **Security audit module error:** Module error since 2026-04-12 - security monitoring automation disrupted, requires investigation and recovery
- **Model evolution:** Monitor for new model releases and evaluate migration benefits
- **Cron job optimization:** Review batch opportunities to reduce API calls (e.g., combine multiple checks into heartbeat)
- **Security posture:** Telegram open group permissions with elevated tools and runtime/filesystem exposure need urgent formal review
- **OpenClaw npm updates:** Monitor for module structure changes that may break cron jobs
- **Memory hygiene:** Regularly promote important daily notes into MEMORY.md, prune outdated entries
- **Automation maturity:** Proactive agent patterns need refinement (autonomous crons, WAL Protocol, Working Buffer)

---

_Updated: 2026-04-26 by periodic-memory-maintenance cron job_
