#!/usr/bin/env bash
# Fails the run if any committed JSONL history line was modified or removed (insert-only DB).
set -euo pipefail
status=0
for f in $(git ls-files 'data/*.jsonl' 'data/**/*.jsonl'); do
  old=$(git show "HEAD:$f" | wc -c)
  if ! cmp -s <(git show "HEAD:$f") <(head -c "$old" "$f"); then
    echo "APPEND-ONLY VIOLATION: $f"; status=1
  fi
done
exit $status
