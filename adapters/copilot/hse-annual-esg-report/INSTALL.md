# Install `hse-annual-esg-report` as a Microsoft Copilot declarative agent

1. Register a new declarative agent (Copilot Studio / agent manifest).
2. Use `manifest.json` (declarative-agent schema 1.7) as the agent manifest.
3. Paste `instructions.md` into the agent's instruction field.
4. Attach every file under `knowledge/` as a knowledge source.
5. The agent emits a structured markdown report (no Python execution on this host).
