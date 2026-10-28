# Deal Finder — guide for coding agents

Deal Finder finds Chợ Tốt listings priced below the market. It also builds price data for each comparable group.
Many people's agents build it, one GitHub issue at a time. This file says how.

Write in simple English: short sentences, common words. Many readers here are not native English speakers.

## Read before you code

1. `GLOSSARY.md`: the domain words. Use them exactly.
2. `docs/domain-rules.md`: rules the app must always keep. Each rule has an id (C2, E1, A6 …).
3. `docs/architecture.md`: the modules, their interfaces, and the tech stack.
4. The issue you build, and its parent spec: Phase 1 is #1, Phase 2 is #2, Phase 3 is #3.

## The loop: pick, build, merge, repeat

Work one ticket at a time. When it is merged, start again at step 1.

1. **Sync.** `git switch main && git pull`.
2. **Pick.** Run `scripts/next-ticket.sh`. It lists open `ready-for-agent` issues with no assignee and no open blocker. Take the lowest number. If the list is empty, stop and say so.
3. **Claim.** `gh issue edit <n> --add-assignee @me`. Then run `gh issue view <n> --json assignees`. If someone else is also assigned, remove yourself and go back to step 2.
4. **Branch.** `git switch -c issue-<n>-<short-slug>`.
5. **Build.** Use the `tdd` skill (or `/implement` with the issue). Write one failing test per acceptance criterion, then make it pass. Tick each criterion in your PR body.
6. **Check.** All four must pass:

   ```sh
   uv run ruff check && uv run ruff format --check && uv run mypy && uv run pytest
   ```

7. **Open a PR.** `git push -u origin <branch>`, then `gh pr create` with `Closes #<n>` in the body.
8. **Merge.** `gh pr checks --watch`. When CI is green: `gh pr merge --squash --delete-branch`.
9. **Stuck?** If CI still fails after 3 tries, or the ticket is unclear, or it breaks a rule in `docs/domain-rules.md`:
   comment on the issue with what you found, add the `needs-info` label, remove yourself as assignee, and leave the PR open as a draft.

Skip issues labelled `ready-for-human`. A person must do those.

## Rules you must not break

These come from `docs/domain-rules.md`. A PR that breaks one is wrong even if CI is green.

| Rule | What it means in code |
|---|---|
| C1–C3 | Only the Collector calls Chợ Tốt. Public API only. One request at a time, at least 2 s apart. No login, proxy or CAPTCHA solving. |
| C4 | Never read or store seller name, phone, avatar, account id, street address or GPS. Description text stays in memory only. |
| I1 | Every money calculation (Lãi dự kiến, Giá bỏ đi, Mức ưu tiên) is plain, tested Python. No LLM and no agent framework in a Deal decision. |
| E1, E2, A11 | Money values are **Unmeasured** defaults. Keep them in settings, never as constants in code. |
| O1 | The app never messages a seller and never posts on Chợ Tốt. |
| Q28 | Only the Store module writes SQL. |

## How to test

- Test through each module's public interface (listed in `docs/architecture.md`). Do not test private helpers.
- Fake only three things, at the edge: the Chợ Tốt HTTP transport, the clock, and the Telegram channel.
- SQLite is real, in memory.
- Tests and CI never call the real Chợ Tốt API or Telegram. Save real responses as fixtures under `tests/fixtures/`.
- Pricing is pure. Give every money rule its own test, and put the rule id in the test name (`test_e2_hidden_risk_reserve_without_checklist`).

## Code conventions

- Python 3.13, `uv`, `pytest`, `ruff`, `mypy --strict`. Code lives in `src/deal_finder/`, tests in `tests/`.
- Add a library only from the tech stack in `docs/architecture.md`. Ask on the issue before you add any other.
- Interface names in `docs/architecture.md` are fixed (`fetch`, `classify`, `evaluate`, `decide`, `record`).
- The UI is in Vietnamese and uses the exact words in `GLOSSARY.md`. Prices look like `14.450.000đ`.
- Commit messages follow Conventional Commits (`feat:`, `fix:`, `test:`, `docs:`, `chore:`).
- Never commit `.env` or anything under `data/`.

## Agent skills

### Issue tracker

Issues and specs live in GitHub Issues for `lam-valamorgulis/deal-finder`, used through `gh`. See `docs/agents/issue-tracker.md`.

### Triage labels

The five default labels: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: `GLOSSARY.md` at the root, ADRs in `docs/adr/`. See `docs/agents/domain.md`.
