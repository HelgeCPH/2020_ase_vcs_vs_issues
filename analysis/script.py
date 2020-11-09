from pydriller import RepositoryMining
from datetime import datetime
import pyfiglet
import operator
import math
import emoji
import io
from contextlib import redirect_stdout
import json
import requests
import os
import subprocess


from pydriller import RepositoryMining


REPO_NAME = "ignite"
FROM = "2a35fb6f02d6031e7f7b6a61e01579c48c081a67"
TO = "383273e3f66f702de2482466dce954d570a8ccf2"

    
cmd = f"git clone git@github.com:apache/{REPO_NAME}.git"
subprocess.run(cmd.split())
rm = RepositoryMining(REPO_NAME, from_commit=FROM, to_commit=TO)
for commit in rm.traverse_commits():
    print(f"{commit.hash[:10]}")