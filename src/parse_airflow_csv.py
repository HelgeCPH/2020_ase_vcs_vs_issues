import os
import pandas as pd
import semver

bugs_to_versions = {}

df = pd.read_csv('./output/airflow_jira.csv')
df_bugs = df[df['issue_type'] == 'Bug']

for index, row in df_bugs.head(300).iterrows():
    for version in str(row['versions']).split():
        try:
            v = semver.VersionInfo.parse(version)            
        except ValueError as error:
            # Some bug reports has no versions defined, so we skip them.
            continue

        key = f'{v.major}.{v.minor}.{v.patch}'

        if key in bugs_to_versions:
            bugs_to_versions[key] = bugs_to_versions[key] + 1
        else:
            bugs_to_versions[key] = 1

for key, value in bugs_to_versions.items():
    print(f'Version: {key} = {value}')

output = 'version,count\n'

for version, count in bugs_to_versions.items():
    output += f'{version},{count}\n'

with open('./output/airflow_jira_bugs.csv', 'w') as file:
    file.write(output)