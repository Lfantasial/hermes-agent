# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ local specifics — the non-sensitive details that are unique to your setup.

## What Goes Here

Store only non-sensitive local notes such as:

- Camera names and locations
- SSH host aliases and friendly names
- Preferred voices for TTS
- Speaker or room names
- Device nicknames
- Environment-specific hints that do not contain credentials

## Never Store Here

Do **not** store secrets or raw credentials in this file, including:

- Access tokens
- Passwords or passphrases
- API keys
- Session cookies
- Private keys
- Recovery codes
- Raw credential files or copied secrets

Use environment variables, a password manager, or a dedicated secret store for sensitive values.

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → Home lab jump host

### Notion

- Workspace: Personal Ops
- Integration alias: notion-main
- Secret location: stored outside this file (env / password manager / vault)
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking local operational context.

---

Keep this file as a non-sensitive local reference only.
