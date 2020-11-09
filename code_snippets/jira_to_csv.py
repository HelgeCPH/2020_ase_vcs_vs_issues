#!/usr/bin/env python

import os
import re
import argparse
import requests
import pandas as pd
from time import sleep
from io import StringIO
from dateutil.parser import parse


JIRA_API_BASE_URL = "https://issues.apache.org/jira/"
PAGE_LENGTH = 500

JIRA_COLUMNS = (
    "issue_type",
    "issue_component",
    "creator_name",
    "creator_display_name",
    "reporter_name",
    "reporter_display_name",
    "priority",
    "description",
    "labels",
    "created",
    "resolution",
    "updated",
    "status",
    "versions",
    "id",
    "key",
)

PROJECTS = {"ignite": "IGNITE", "airflow": "AIRFLOW", "camel": "CAMEL"}


def collect_from_jira(force_recollections=False):
    for proj_gh_name, proj_jira_id in PROJECTS.items():
        if not proj_jira_id:
            continue

        fname = f"output/{proj_gh_name}_jira.csv"
        if not force_recollections:
            if os.path.isfile(fname):
                print(f"Found {fname}, will not recreate it...")
                continue

        print(f"Collecting data from {proj_gh_name}...")
        sleep(5)

        rows = []
        start_idx = 0
        url = (
            JIRA_API_BASE_URL
            + f"rest/api/2/search?jql=project={proj_jira_id}+order+by+created"
            + f"&issuetypeNames=Bug&maxResults={PAGE_LENGTH}&"
            + f"startAt={start_idx}&fields=id,key,priority,labels,versions,"
            + "status,components,creator,reporter,issuetype,description,"
            + "summary,resolutiondate,created,updated"
        )

        print(f"Getting data from {url}...")
        r = requests.get(url)
        r_dict = r.json()

        while start_idx < r_dict["total"]:
            sleep(2)

            # The above `issuetypeNames=Bug` should limit the response to bugs
            # only but the response for `WW` contains more issue types. So I
            # have to filter later ...
            for idx in range(len(r_dict["issues"])):
                fields = r_dict["issues"][idx]["fields"]

                # fields["issuetype"]["description"]
                issue_type = fields["issuetype"]["name"]

                issue_component = [
                    c["name"] for c in fields["issuetype"].get("components", [])
                ]
                creator = fields["creator"]
                if creator:
                    creator_name = creator.get("name", None)
                    creator_display_name = creator.get("displayName", None)
                else:
                    creator_name = None
                    creator_display_name = None

                reporter = fields["reporter"]
                if reporter:
                    reporter_name = reporter.get("name", None)
                    reporter_display_name = reporter.get("displayName", None)
                else:
                    reporter_name = None
                    reporter_display_name = None

                priority = fields["priority"]
                if priority:
                    priority = priority.get("name", None)

                description = fields["description"]
                labels = fields["labels"]

                created = fields["created"]
                if created:
                    created = parse(created)
                resolution = fields["resolutiondate"]
                if resolution:
                    resolution = parse(resolution)
                updated = fields["updated"]
                if updated:
                    updated = parse(updated)
                status = fields["status"]["name"]

                version_fields = fields["versions"]
                versions_str = " ".join([v["name"] for v in version_fields])

                id_val = r_dict["issues"][idx]["id"]
                key_val = r_dict["issues"][idx]["key"]

                rows.append(
                    (
                        issue_type,
                        issue_component,
                        creator_name,
                        creator_display_name,
                        reporter_name,
                        reporter_display_name,
                        priority,
                        description,
                        labels,
                        created,
                        resolution,
                        updated,
                        status,
                        versions_str,
                        id_val,
                        key_val,
                    )
                )

            start_idx += PAGE_LENGTH
            url = re.sub(r"startAt=\d+&", f"startAt={start_idx}&", url)
            inner_idx = start_idx + PAGE_LENGTH
            print(f"Getting data for index {start_idx} to {inner_idx}...")
            r = requests.get(url)
            r_dict = r.json()

        print(f"Writing {fname} for {proj_gh_name}...")
        df = pd.DataFrame(rows, columns=JIRA_COLUMNS)
        df.to_csv(fname, index=False)


if __name__ == "__main__":

    msg = "Collect issues from JIRA and from Bugzilla."
    parser = argparse.ArgumentParser(description=msg)
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite previously collected issue dumps.",
    )

    args = parser.parse_args()
    collect_from_jira(force_recollections=args.force)
