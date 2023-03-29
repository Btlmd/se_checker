import gitlab
import re
import os
import argparse

def diff_modified_lines(commit):
    total_addition, total_deletion = 0, 0
    for d in commit.diff(all=True):
        addition = d['diff'].count('\n+')
        deletion = d['diff'].count('\n-')
        total_addition += addition
        total_deletion += deletion
    return total_addition + total_deletion



def check_and_pick(repo, commit_regex, merge_regex, branch_regex):
    token, pid = repo
    gl = gitlab.Gitlab("https://gitlab.secoder.net", token)
    proj = gl.projects.get(pid)
    print("Check", proj.name)
    commits = proj.commits.list(all=True)
    mrs = proj.mergerequests.list(all=True)
    branches = proj.branches.list(all=True)

    print("TOTAL commit, merge, branches:", len(commits), len(mrs), len(branches))

    for i in commits:
        if not re.fullmatch(commit_regex, i.title):
            print("Commit Regex Unmatch:", i.id, i.title, i.author_name, i.author_email, i.created_at, sep=" | ")
        
        diff_count = diff_modified_lines(i)
        if diff_count > 500:
            print("Commit Line limit exceed:", i.id, f"{diff_count} lines", i.title, i.author_name, i.author_email, i.created_at, sep=" | ")
            print(" > ", i.web_url)

    for i in mrs:
        if not re.fullmatch(merge_regex, i.title):
            print("MR Regex Unmatch:", i.iid, i.title, i.author['name'], i.author['username'], i.created_at, sep=" | ")

    for i in branches:
        if not re.fullmatch(branch_regex, i.name):
            print("Branch Regex Unmatch:", i.name, i.commit['author_name'], i.commit['author_email'], i.commit['created_at'], sep=" | ")
    print("")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit_regex", help="commit regex")
    parser.add_argument("--merge_regex", help="merge regex")
    parser.add_argument("--branch_regex", help="issue regex")
    args = parser.parse_args()

    ident = os.environ.get("GITLAB_TOKEN"), os.environ.get("GITLAB_PID")

    check_and_pick(ident, args.commit_regex, args.merge_regex, args.branch_regex)