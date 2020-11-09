import pandas as pd
import os
import sys
import io
from contextlib import redirect_stdout

""" This script takes two arguments: Arg1 csv path Arg2 version_file_paths """
""" Run like this python jira_bug_count.py "code_snippets/output/camel_jira.csv" "output/versions.txt" """

def CreateOutputDirectories(path):
    """ Creates directory if it doesnt exist"""
    if not os.path.exists(path):
        os.makedirs(path)

def WriteOutputAsFile(function, input_csv_path, versions_txt_path, output_path, outputfilename):
    """ Calls function and writes return value to file """
    path = os.path.join(output_path, outputfilename)
    out = function(input_csv_path, versions_txt_path).strip()
    output = open(path, "w")
    output.write(out)
    output.flush()
    output.close()

def prepare_dataframe(input_csv_path):
    """ Reads input file as Dataframe, converts to new df with only one version per row """
    df = pd.read_csv (input_csv_path)
    df = df.sort_values(by=['versions']) # Sort on version ascending
    df = df[(df.issue_type == "Bug")]
    df = df.dropna(how='any')

    new_df = pd.DataFrame(df.versions.str.split(' ').tolist(), index=df.id).stack() # Step 2
    new_df = new_df.reset_index([0, 'id'])
    new_df.columns = ['id', 'versions'] # Result
    return new_df


def data_to_csv(input_csv_path, versions_txt_path):
    """ Prepares input data, counts rows/version, prepares csv and writes csv to file """
    df = prepare_dataframe(input_csv_path)
   
   # Create (version, count) csv file
   # Count number of rows for each version
    csv_body = ""
    with open(versions_txt_path, "r") as version_file_object:
        for version in version_file_object:
            count = int(df[(df.versions == version.strip())].shape[0])
            csv_body = csv_body + f"{version.strip()}, {count}\n"
    csv_with_header = f"""version, csv\n{csv_body.strip()}"""
    return csv_with_header


"""
We decided in class to output to outputs folder.

Takes the two lists as arguments to be called as subprocess from other python script.
Otherwise, change to environment variables os.getenv("var_name") for Docker support
Can also be made into std module 
"""

BASE_PATH = "outputs/"
INPUT_CSV = sys.argv[1]
VERSIONS_TXT = sys.argv[2]

def main(input_csv_path, versions_txt_path, base_path):
    CreateOutputDirectories(base_path)
    split_arr = input_csv_path.split("/")
    outputfilename = split_arr[split_arr.__len__()-1].split(".")[0] + "_bugs_per_version.csv"
    WriteOutputAsFile(data_to_csv, input_csv_path, versions_txt_path, base_path, outputfilename)

if __name__ == "__main__":
    main(INPUT_CSV, VERSIONS_TXT, BASE_PATH)
