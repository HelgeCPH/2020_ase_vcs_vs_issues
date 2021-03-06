# Run with: authors.py [tag/commit] <apache_repo_name> <from> <to>

# Prints number of unique authors AND outputs list of unique author names as CSV.

import os
import subprocess
import csv
import sys

from pydriller import RepositoryMining

RANGE_MARKER = sys.argv[1]  # tag or commit
REPO_NAME = sys.argv[2]  # ignite
FROM = sys.argv[3]  # v.1.2.3 or 2a35fb6f02d6031e7f7b6a61e01579c48c081a67
TO = sys.argv[4]  # v.4.5.6 or 383273e3f66f702de2482466dce954d570a8ccf2

if not os.path.isdir(REPO_NAME):
    print(f"Directory '{REPO_NAME}' does not exist..")
    cmd = f"git clone git@github.com:apache/{REPO_NAME}.git"
    subprocess.run(cmd.split())

rm = None

if RANGE_MARKER == "tag":
    rm = RepositoryMining(REPO_NAME, from_tag=FROM, to_tag=TO)
elif RANGE_MARKER == "commit":
    rm = RepositoryMining(REPO_NAME, from_commit=FROM, to_commit=TO)
else:
    print("It seems you failed to provide 'tag' or 'commit' as your first parameter. ")

authors = set()

for commit in rm.traverse_commits():
    authors.add(commit.author.name)

with open('output/unique_authors.csv', mode='w') as unique_authors:
    writer = csv.writer(unique_authors, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for author in sorted(authors, key=str.lower):
        writer.writerow([author])

print(len(authors))
