#! /usr/env bash

GITLAB_TOKEN=XXX GITLAB_PID=XXX python git_match.py  \
    --commit_regex "((feat|fix|docs|style|refactor|perf|test|build|ci|chore)(\(.*\))?:.*)|(Revert \".*\")|(Merge branch '.*' into '.*')|([Ii]nit.*commit)" \
    --merge_regex "((feat|fix|docs|style|refactor|perf|test|build|ci|chore)(\(.*\))?:.*)|(Revert \".*\")|(Merge branch '.*' into '.*')|([Ii]nit.*commit)" \
    --branch_regex "(([Ff]eat|[Ff]eature|[Bb]ugfix|[Ff]ix|[Dd]ev|[Dd]ocs|[Ss]tyle|[Rr]efactor|[Pp]erf|[Tt]est|[Bb]uild|[Cc][Ii]|[Cc]hore)(-|\s).*)|master|main|(dev.*)"

