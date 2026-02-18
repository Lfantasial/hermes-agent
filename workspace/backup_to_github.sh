#!/bin/bash
cd /home/lfant/.openclaw
# Stage all changes
git add .
# Commit with timestamp
git commit -m "Daily backup: $(date '+%Y-%m-%d %H:%M:%S')"
# Push to master
git push origin master
