# Deal Finder

Finds Chợ Tốt listings priced below the market. Builds price data for each comparable group.

- What the words mean: `GLOSSARY.md`
- Rules the app must keep: `docs/domain-rules.md`
- How it is built: `docs/architecture.md`
- Work to do: [GitHub issues](https://github.com/lam-valamorgulis/deal-finder/issues), starting from #4

## Set up

1. Install [uv](https://docs.astral.sh/uv/) and the GitHub CLI (`gh`), then run `gh auth login`.
2. Run `uv sync`.
3. Copy `.env.example` to `.env`. Fill it in only if your ticket needs Telegram.
4. Check that everything passes:

   ```sh
   uv run ruff check && uv run ruff format --check && uv run mypy && uv run pytest
   ```

## Build with a coding agent

Open the repo in Claude Code. On first open, accept the prompt to install the `mattpocock-skills` plugin, and trust the project settings.

Then ask the agent to pick up the next ticket. `CLAUDE.md` tells it how to choose a ticket, build it and merge it.
