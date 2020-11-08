"""
Run me with:
$ python git_to_png.py > history.dot; dot -Tpng -o x.png history.dot; open x.png
"""
import os
import subprocess
from pydriller import RepositoryMining


REPO_NAME = "ignite"


if not os.path.exists(REPO_NAME):
    cmd = f"git clone git@github.com:apache/{REPO_NAME}.git"
    subprocess.run(cmd.split())


# Since from_commit is exclusive the given commit hash, we use the parent of
# tag 1.6.0 commit:
# https://github.com/apache/ignite/commit/0b22c45bb9b97692208fd0705ddf8045ff34a031
# FROM = "0b22c45bb9b97692208fd0705ddf8045ff34a031"
FROM = "2a35fb6f02d6031e7f7b6a61e01579c48c081a67"
TO = "383273e3f66f702de2482466dce954d570a8ccf2"
rm = RepositoryMining(REPO_NAME, from_commit=FROM, to_commit=TO)

print(
    """digraph D {
    rankdir=BT;"""
)
for commit in rm.traverse_commits():
    if commit.parents:
        for parent in commit.parents:
            print(f'"{parent[:10]}" -> "{commit.hash[:10]}";')
    else:
        print(f"{commit.hash[:10]}")
print("}")
