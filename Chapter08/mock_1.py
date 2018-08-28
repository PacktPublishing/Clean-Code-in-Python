"""Clean Code in Python - Chapter 8: Unit Testing

> Mock Objects
"""

from typing import Dict, List


class GitBranch:
    def __init__(self, commits: List[Dict]):
        self._commits = {c["id"]: c for c in commits}

    def __getitem__(self, commit_id):
        return self._commits[commit_id]

    def __len__(self):
        return len(self._commits)


def author_by_id(commit_id, branch):
    return branch[commit_id]["author"]
