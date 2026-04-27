#!/bin/bash
cd /home/lfant/.openclaw
# Stage all changes except memory files
git add .
git reset HEAD workspace/memory/
git reset HEAD workspace/MEMORY.md
git reset HEAD workspace/SESSION-STATE.md
# Commit with timestamp
git commit -m "Daily backup: $(date '+%Y-%m-%d %H:%M:%S')"
# Push to master
git push origin master
