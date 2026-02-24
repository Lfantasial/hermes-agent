# [openclaw-main] recent context, 2026-02-25 6:05am GMT+9

**Legend:** session-request | 🔴 bugfix | 🟣 feature | 🔄 refactor | ✅ change | 🔵 discovery | ⚖️ decision

**Column Key**:
- **Read**: Tokens to read this observation (cost to learn it now)
- **Work**: Tokens spent on work that produced this record ( research, building, deciding)

**Context Index:** This semantic index (titles, types, files, tokens) is usually sufficient to understand past work.

When you need implementation details, rationale, or debugging context:
- Fetch by ID: get_observations([IDs]) for observations visible in this index
- Search history: Use the mem-search skill for past decisions, bugs, and deeper research
- Trust this index over re-reading code for past decisions and learnings

**Context Economics**:
- Loading: 50 observations (18,928 tokens to read)
- Work investment: 120,582 tokens spent on research, building, and decisions
- Your savings: 101,654 tokens (84% reduction from reuse)

### Feb 23, 2026

**USER.md**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #468 | 7:00 AM | 🔵 | Sam's User Profile Defined in USER.md | ~486 |  |

**../../home/lfant/.openclaw/workspace/memory/2025-02-22.md**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #469 | " | 🔵 | Daily Memory File Path Structure and Missing File | ~314 |  |

**../../home/lfant/.openclaw/workspace/notion_daily_brief.py**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #470 | 8:00 AM | 🔵 | Cron-Triggered Notion Daily Briefing Automation | ~341 |  |

**~/.config/systemd/user/openclaw-gateway.service**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #471 | 8:02 AM | 🔵 | OpenClaw Gateway Service Config Fragility — NVM Node Path | ~372 |  |

**~/.openclaw/workspace/ (cron jobs config, read via SDK tool)**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #472 | 8:25 AM | 🔵 | OpenClaw Cron Jobs Status: Widespread "announce delivery" Failures | ~593 |  |

**#S170** Daily Security Audit Cron Job — Run `openclaw security audit --deep` and report findings or alert Sam on critical issues (Feb 23, 9:41 PM)

**SOUL.md**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #473 | 9:42 PM | 🔵 | Hugin AI Identity File: SOUL.md | ~302 |  |

### Feb 24, 2026

**General**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #474 | 3:00 AM | 🔵 | Daily Security Audit Cron Job Configuration | ~309 |  |
| #475 | " | 🔵 | `openclaw` Command Not Found in Execution Environment | ~237 |  |
| #476 | " | 🔵 | `openclaw` Confirmed Absent — No Binary or Bin Directory Found | ~197 |  |
| #477 | 6:00 AM | 🔵 | Daily Update Check Cron Job for OpenClaw and Skills | ~288 |  |
| #478 | " | 🔵 | openclaw Command Not Found in PATH | ~204 |  |
| #479 | 6:01 AM | 🔵 | openclaw Installed via npx Cache, Not as Global Binary | ~272 |  |

**../../home/lfant/.openclaw/workspace/skills/proactive-agent/scripts/security-audit.sh**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #480 | 6:07 AM | 🔵 | Daily Security Audit Cron Job Fails — openclaw CLI Not in PATH | ~411 |  |

**General**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #481 | " | 🔵 | Daily Security Audit Cron Job — Known False Positives Catalogued | ~367 |  |

**#S171** Daily Security Audit Cron Job Result — openclaw CLI missing, deep scan failed (Feb 24, 6:08 AM)

**#S172** Duplicate cron job delivery check — NO_REPLY issued, result already delivered (Feb 24, 6:08 AM)

**#S173** Second duplicate cron delivery suppressed — NO_REPLY issued again (Feb 24, 6:08 AM)

**#S174** Daily GitHub Backup Cron Job — Execute backup_to_github.sh and confirm result (Feb 24, 6:08 AM)

**../../home/lfant/.openclaw/workspace/backup_to_github.sh**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #482 | 6:28 AM | ✅ | Daily GitHub Backup Cron Job Triggered | ~207 |  |

**General**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #483 | " | 🔵 | Daily Update Check Cron Job Configured | ~278 |  |

**#S175** Daily update check cron job (dc1f52da) — checked OpenClaw and skills for available updates at 6:00 AM Asia/Seoul on February 24, 2026 (Feb 24, 6:29 AM)

**#S176** Investigating whether openclaw is installed in multiple locations on the system (Feb 24, 6:29 AM)

**General**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #484 | 7:00 AM | 🔵 | Daily Morning Briefing Cron Job for Sam (Seoul, 7 AM) | ~327 |  |

**SOUL.md**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #485 | " | 🔵 | Hugin Agent Identity Defined in SOUL.md | ~433 |  |

**General**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #486 | 8:10 AM | 🔵 | openclaw Installed in Two Locations | ~305 |  |
| #487 | 8:11 AM | 🔵 | Both openclaw Installations Are the Same Version | ~167 |  |

**#S177** Understanding whether openclaw's workspace and config are shared across both installations (Feb 24, 8:11 AM)

**../../home/lfant/.openclaw/workspace/AGENTS.md**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #488 | 8:11 AM | 🔵 | openclaw Workspace Directory Contents | ~339 |  |

**General**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #489 | " | 🔵 | openclaw Config Explicitly Sets Workspace Path | ~166 |  |

**../../home/lfant/.openclaw/openclaw.json**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #490 | " | 🔵 | openclaw Main Config File Structure (openclaw.json) | ~321 |  |

**#S178** Diagnosing why openclaw is installed in two places and deciding which installation to keep (Feb 24, 8:11 AM)

**General**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #491 | 8:12 AM | 🔵 | Precise Timestamps for Both openclaw Installation Symlinks | ~221 |  |
| #492 | " | 🔵 | openclaw Installations Differ: NVM Has Skills Directory, npm-global Is 1.3GB | ~300 |  |
| #493 | " | 🔵 | npm-global openclaw Disk Usage Breakdown | ~301 |  |
| #494 | 8:21 PM | 🔵 | Research: OpenClaw OAuth + AntiGravity Ban Cases | ~228 |  |

**~/.openclaw/**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #495 | " | 🔵 | Local Environment Has .openclaw and .clawhub Directories | ~319 |  |

**General**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #496 | 8:22 PM | 🔵 | Anthropic Banned OpenClaw OAuth Tokens; Google AI Also Restricting Accounts | ~449 |  |
| #497 | " | 🔵 | Anthropic Banned OAuth Token Use in Third-Party Tools (Feb 19, 2026) | ~562 |  |
| #498 | " | 🔵 | OpenClaw Founder Joined OpenAI; Anthropic Ban Has Corporate Conflict-of-Interest Dimension | ~482 |  |
| #499 | 8:23 PM | 🔵 | Real User Ban Case: Google AI One Pro + OpenCode OAuth → ToS Ban via AntiGravity | ~535 |  |
| #500 | " | 🔵 | Google Antigravity Mass Ban: Zero-Tolerance Policy for OpenClaw OAuth Use | ~821 |  |

**~/.openclaw/agents/&lt;agentId&gt;/agent/auth-profiles.json**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #501 | 8:24 PM | 🔵 | OpenClaw OAuth Docs: Anthropic Uses setup-token Flow; Google/AntiGravity Not Listed | ~586 |  |

**General**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #502 | " | 🔵 | Global Media Coverage: OpenClaw Antigravity Ban Is Worldwide News; Creator May End Project | ~698 |  |
| #503 | 8:25 PM | 🔵 | GitHub Issue #14203: Exact Error Messages and Recommended Fix for Antigravity Ban | ~534 |  |

**../../home/lfant/.openclaw/workspace**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #504 | 8:52 PM | 🔵 | OpenClaw Version Check Before Update | ~329 |  |

**../../home/lfant/.nvm/versions/node/v22.22.0/lib/node_modules/openclaw**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #505 | " | 🔵 | OpenClaw Auto-Update Skipped: npm Global Install Requires Manual Update | ~321 |  |

**General**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #506 | " | 🔴 | OpenClaw Update Fails: System npm Used Instead of NVM npm | ~357 |  |
| #507 | " | 🔵 | PATH Conflict: System Node/npm Active While OpenClaw Lives Under NVM | ~312 |  |

**../../home/lfant/.nvm/current/bin**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #508 | 8:53 PM | 🔵 | NVM Global Bin Directory Contents Mapped | ~329 |  |

**General**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #509 | " | 🔵 | Research: OpenClaw OAuth Usage Leading to Anti-Gravity Ban | ~243 |  |

**package-lock.json**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #510 | " | ✅ | openclaw npm 패키지 업데이트 | ~145 |  |

**~/.openclaw/agents/main/sessions/sessions.json**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #511 | " | 🔵 | openclaw doctor 실행 결과 - 시스템 상태 점검 | ~219 |  |

**#S179** OpenClaw + Google Antigravity(Gemini) OAuth 사용으로 인한 계정 밴 케이스 조사 (Feb 24, 8:54 PM)

**General**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|
| #512 | 9:23 PM | 🔵 | Google DeepMind/Antigravity OpenClaw Ban — Background Intelligence | ~493 |  |

**#513** 9:24 PM 🔵 **Google DeepMind Engineer Announced Appeal Path for Banned OpenClaw/Antigravity Users**

The primary session's subagent was asked whether Google DeepMind engineers announced an appeal/소명 procedure for users banned in the OpenClaw/Antigravity incident. The VentureBeat article (2026-02-23) provides the definitive answer: YES. Varun Mohan, a Google DeepMind engineer, explicitly stated in an X post that users unaware of the ToS violation "will get a path for them to come back on." This constitutes a public announcement of an appeal/reinstatement pathway, though the specific mechanics of that process had not yet been defined at time of publication. The ban itself was motivated by massive Gemini token overconsumption routed through OpenClaw's OAuth plugin to Antigravity, degrading service for paying users. The incident also has a competitive dimension: OpenClaw's creator joined OpenAI one week prior, making Google's action a simultaneous ToS enforcement and competitive barrier. Both Google and Anthropic are moving toward "walled garden" agent ecosystems that exclude third-party wrappers.

Read: ~649

**General**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|

**#514** " 🔵 **The Register Confirms Mohan's Reinstatement Promise + Google Developer Forum Threads**

The Register article (2026-02-23) corroborates the VentureBeat findings and adds a second Mohan quote explicitly promising reinstatement. The article also surfaces Google developer forum threads where affected users organized and documented their bans. The core finding for the original research question remains: Mohan publicly committed to a path for users to return, framing it as urgency-driven rather than punitive. No formal appeal mechanism with specific steps has been announced — just a commitment that one will exist. Anthropic's parallel ban (documented 2026-02-20) suggests this is an industry-wide pattern of clamping down on subscription token arbitrage via third-party wrappers.

Read: ~539

**General**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|

**#515** 9:25 PM 🔵 **Google's Official Appeal Channel: Antigravity In-App Feedback Tool (Practically Inaccessible to Banned Users)**

The Google AI developer forum thread (discuss.ai.google.dev/t/account-restricted-without-warning-google-ai-ultra-oauth-via-openclaw/122778) reveals that the ban wave predates news coverage by ~10 days, starting around 2026-02-12. A Google staff member did respond and pointed users toward the official appeal mechanism: the Antigravity in-app feedback "Report Issue" tool. However, this was a Catch-22 — banned users were fully logged out of their accounts and unable to access the app to submit feedback. Support escalation through Google Cloud and Google One created a circular redirect with no resolution. This directly answers the original research question: yes, Google provided an official appeal channel (in-app feedback), but it was operationally inaccessible to the affected users, compounding the perception that the ban was "draconian."

Read: ~569

**General**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|

**#516** " 🔵 **Second Google Forum Thread Confirms Global Scope: Korean Users Affected, Subscriptions Charged During Ban**

The second Google AI developer forum thread (discuss.ai.google.dev/t/.../123015) corroborates and extends the picture: the ban was global (Korean-language user confirmed affected), Google continued billing banned subscribers with no service, and no formal appeal/소명 process existed as of mid-February. The absence of any Google staff response in this higher-profile thread (vs. the token response in thread 122778) reinforces that the "path to come back" promised by Varun Mohan on 2026-02-23 was a response to escalating public pressure, not a pre-existing process. The OpenClaw ban predated Mohan's public commitment by ~10 days with no official reinstatement mechanism in place during that window.

Read: ~495

**General**
| ID | Time | T | Title | Read | Work |
|----|------|---|-------|------|------|

**#517** " 🔵 **Critical New Details: Permanent Bans Reported, "WAF Bug" Cited, Fake Student Accounts as Root Cause**

The processed summary of both forum threads reveals significant new details. First, some bans are permanent — at least one user was explicitly told after 3 weeks that their account cannot be restored. Second, Google's own Tier 1 support described the issue as a "known WAF bug," raising the possibility that some bans were triggered by automated web application firewall rules misidentifying legitimate OpenClaw OAuth traffic as malicious. Third, a community member identified "millions of fake student accounts" as the underlying capacity problem, meaning innocent developers were caught in a broad sweep targeting account abuse. Fourth, a second Google staff post acknowledged the issue and promised prioritized resolution. The appeal/소명 process that Varun Mohan promised on 2026-02-23 had not materialized for users who had been waiting since 2026-02-12, with at least some being told their accounts cannot be restored.

Read: ~656


Access 121k tokens of past research & decisions for just 18,928t. Use the claude-mem skill to access memories by ID.