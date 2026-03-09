# Working Buffer (Danger Zone Log)

**Status:** INACTIVE
**Started:** 2026-03-09T22:38:04+09:00
**Activation Rule:** Start appending every exchange only when session context exceeds 60% or compaction risk is detected.

---

## Notes
- Keep this file empty during normal operation.
- When activated, append both the human message and a 1-2 sentence agent summary for each exchange.
- After compaction/recovery, extract durable facts into `SESSION-STATE.md` or daily memory and then reset this file.
