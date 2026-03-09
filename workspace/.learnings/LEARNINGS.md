# LEARNINGS.md

## [LRN-20260309-001] correction

**Logged**: 2026-03-09T21:17:00+09:00
**Priority**: high
**Status**: pending
**Area**: docs

### Summary
Sam already uses claude-mem for memory; do not position simplemem-skill as the primary memory layer.

### Details
In the OpenClaw operating profile discussion, memory-related recommendations emphasized simplemem-skill. Sam clarified that claude-mem is already in use. Future recommendations should treat claude-mem as the primary memory system and frame other memory skills as optional/complementary only if they add distinct value.

### Suggested Action
Revise future OpenClaw profile guidance to replace simplemem-skill with claude-mem in the memory layer.

### Metadata
- Source: conversation
- Related Files: /home/lfant/.openclaw/workspace/MEMORY.md
- Tags: correction, memory, claude-mem, openclaw

---
## [LRN-20260309-002] correction

**Logged**: 2026-03-09T22:52:00+09:00
**Priority**: high
**Status**: pending
**Area**: infra

### Summary
Repeated heartbeat cron timeouts are likely not model-related; treat them as scheduler/execution-path issues first.

### Details
Sam pointed out that the issue is probably not the model. Observed evidence supports this: isolated heartbeat runs timed out under multiple model/thinking settings, including GLM with thinking off. This suggests the root cause is more likely cron execution mode, scheduler ack/completion handling, or system-event routing rather than the chosen model.

### Suggested Action
When diagnosing future heartbeat cron failures, prioritize execution architecture and scheduler behavior over model changes.

### Metadata
- Source: conversation
- Related Files: /home/lfant/.openclaw/workspace/SESSION-STATE.md
- Tags: correction, cron, heartbeat, scheduler, model

---
