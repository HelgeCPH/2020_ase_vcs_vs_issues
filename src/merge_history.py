from pydriller import RepositoryMining
from datetime import datetime
import json

REPO_NAME_IGNITE = "apache/ignite"
REPO_NAME_AIRFLOW = "apache/airflow"
REPO_NAME_CAMEL = "apache/camel"


def get_relevant_merge_commits(repo):
    merge_commits = []
    for commit in RepositoryMining(f"https://github.com/{repo}.git").traverse_commits():
        if commit.merge:
            merge_commits.append(commit)
    return merge_commits


