#!/usr/bin/env bash
# Wrapper for install.cmem.ai/openclaw.sh to run non-interactively
# Usage: ./install_claude_mem.sh

# Force non-interactive mode and use Gemini provider
export NON_INTERACTIVE=true
export CLI_PROVIDER=gemini
# We'll set the API key later in the config if needed, or rely on existing auth profiles.
# The script supports --api-key but we can skip it if we configure manually.
# However, to pass the script's validation without prompt, we might need a dummy key or just rely on defaults.
# Let's try passing the provider flag directly.

curl -fsSL https://install.cmem.ai/openclaw.sh | bash -s -- --non-interactive --provider=gemini --api-key=placeholder_will_configure_manually
