import pandas as pd
import os
import sys
import io
from contextlib import redirect_stdout

""" This script takes two arguments: Arg1 csv path Arg2 version_file_paths """

""" Run like this python jira_bug_count.py "code_snippets/output/camel_jira.csv" "output/versions.txt" """

def csv():
    df = pd.read_csv (INPUT_CSV)
    df.sort_values(by=['versions'], inplace=True) # Sort on version
    df = df[(df.issue_type == "Bug")]
    df = df.dropna(how='any')

    new_df = pd.DataFrame(df.versions.str.split(' ').tolist(), index=df.id).stack() # Step 2
    new_df = new_df.reset_index([0, 'id'])# Step 3
    new_df.columns = ['id', 'versions'] # Result

    csv_body = ""
    with open(OUTPUT_CSV, "r") as version_file_object:
        for version in version_file_object:
            count = int(new_df[(new_df.versions == version.strip())].shape[0])
            csv_body = csv_body + f"{version.strip()}, {count}\n"

    csv_with_header = f"""version, csv\n{csv_body.strip()}""".strip()
    print(csv_with_header)

BASE_PATH = "output/"

def CreateOutputDirectories():
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH)

def CaptureOutputAsFile(function, outputfilename):
    path = f"{BASE_PATH}{outputfilename}"
    f = io.StringIO()
    with redirect_stdout(f):
        function()
    out = f.getvalue()
    output = open(path, "w")
    output.write(out)
    output.flush()
    output.close()

INPUT_CSV = sys.argv[1]
OUTPUT_CSV = sys.argv[2]

def main():
    CreateOutputDirectories()
    split = INPUT_CSV.split("/")
    outputfilename = split[split.__len__()-1].split(".")[0] + "_bugs_per_version.csv"

    CaptureOutputAsFile(csv, outputfilename)

main()
