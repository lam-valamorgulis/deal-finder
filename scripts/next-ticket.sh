#!/usr/bin/env bash
# List the tickets an agent can take now: open, ready-for-agent,
# no assignee, no open blocker, and not a spec (a spec has sub-issues).
# Lowest number first.
set -euo pipefail

repo=$(gh repo view --json nameWithOwner --jq .nameWithOwner)

gh issue list --state open --label ready-for-agent --search "no:assignee" --limit 200 \
  --json number,title --jq 'sort_by(.number) | .[] | "\(.number)\t\(.title)"' |
  while IFS=$'\t' read -r number title; do
    skip=$(gh api "repos/$repo/issues/$number" \
      --jq '((.issue_dependencies_summary.blocked_by // 0) + (.sub_issues_summary.total // 0))')
    if [ "$skip" = "0" ]; then
      printf '#%s\t%s\n' "$number" "$title"
    fi
  done
