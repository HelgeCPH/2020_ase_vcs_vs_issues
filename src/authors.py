import os
import subprocess
import csv

from pydriller import RepositoryMining

REPO_NAME = "ignite"
FROM = "2a35fb6f02d6031e7f7b6a61e01579c48c081a67"
TO = "383273e3f66f702de2482466dce954d570a8ccf2"

if not os.path.isdir(REPO_NAME):
    print(f"Directory '{REPO_NAME}' does not exist..")
    cmd = f"git clone git@github.com:apache/{REPO_NAME}.git"
    subprocess.run(cmd.split())

rm = RepositoryMining(REPO_NAME, from_commit=FROM, to_commit=TO)

commits = []
authors = set()

for commit in rm.traverse_commits():
    authors.add(commit.author.name)

with open('unique_authors.csv', mode='w') as unique_authors:
    writer = csv.writer(unique_authors, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for author in sorted(authors, key=str.lower):
        writer.writerow([author])
