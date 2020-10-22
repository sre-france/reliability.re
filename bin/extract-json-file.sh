#!/bin/bash
#
# This script search for files added on $commit
# and checkout the file on the current workspace

set -xe

commit="$1"
branch="origin/gh-pages"
pattern="links/*/index.json"

json_post=$(git diff-tree --no-commit-id --name-only --diff-filter=A -r "$commit" -- "$pattern")
git checkout "$branch" -- "$json_post"
echo "$json_post"
