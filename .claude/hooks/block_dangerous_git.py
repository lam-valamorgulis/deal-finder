"""PreToolUse hook: stop git commands that can lose work or skip review.

Agents may push their own branch. They may not push to main, force push,
or throw away local work. Merging happens through `gh pr merge`.
"""

import json
import re
import sys

BLOCKED = [
    (r"git\s+push\b.*(--force|--force-with-lease|\s-f\b|\s\+)", "force push"),
    (r"git\s+push\b.*\bmain\b", "push to main"),
    (r"git\s+push\s*($|;|&&|\|)", "bare `git push` (name the branch: git push -u origin <branch>)"),
    (r"git\s+reset\s+--hard", "git reset --hard"),
    (r"git\s+clean\s+-[a-zA-Z]*f", "git clean -f"),
    (r"git\s+branch\s+-D\b", "git branch -D"),
    (r"git\s+(checkout|restore)\s+\.", "discarding all local changes"),
]


def main() -> int:
    command = json.load(sys.stdin).get("tool_input", {}).get("command", "")
    for pattern, name in BLOCKED:
        if re.search(pattern, command):
            print(
                f"BLOCKED: {name}. This repo does not allow it. "
                "Push your own branch and merge with `gh pr merge` after CI is green.",
                file=sys.stderr,
            )
            return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
