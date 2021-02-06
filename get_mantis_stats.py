from datetime import datetime, date, timedelta
import requests

project_url = "http://mantis.com/api/rest/issues?project_id="
filter_open, filter_closed = "&filter_id=100&page_size=900", "&filter_id=1115&page_size=170"
project_id = ["36", "37"]

projects = [project_url + _ + filter_open for _ in project_id] + [project_url + _ + filter_closed for _ in project_id]

header = {"Authorization": "token_goes_here"}


def get_project_data(url):
    """a REST API client"""
    response = requests.get(url, headers=header)
    return response.json()["issues"]   # JSON object to a dict inside a list


open_today = 0
resolved_today = 0
today = date.today() - timedelta(days=0)

with open("project_stats.txt", "a") as stats_file:
    stats_file.write(f"{today:%d %b %Y}, ")
for index, project in enumerate(sorted(projects), start=1):
    issues = get_project_data(project)
    if filter_open in project:
        open_today += len([issue["id"] for issue in issues])
    elif filter_closed in project:
        get_datetime = [issue["updated_at"] for issue in issues]    # %Y-%m-%dT%H:%M:%S%z ISO 8601 format
        resolved_today = [datetime.fromisoformat(issue).date() for issue in get_datetime].count(today)
        with open("project_stats.txt", "a") as stats_file:
            stats_file.write(f"{'SimsWorld' if 'project_id=37' in project else 'JA'}: "
                             f"{{Open: {open_today}, Resolved: {resolved_today}}}"
                             f"{', ' if len(projects) > index else chr(10)}")
        open_today = 0
        resolved_today = 0


# debug helpers #

# pid = [issue["project"]["id"] for issue in issues]
# status = [issue["status"]["name"] for issue in issues]
# pid_status = list(zip(pid, status))
# issue_filter = [(issue["project"]["id"] == 37 or issue["project"]["id"] == 39)
#                 for issue in issues
#                 if (issue["resolution"]["name"] == "open" or issue["resolution"]["name"] == "reopened")]
# check = list(zip(pid_status, issue_filter))
# print(issues[0]["id"], issues[0]["project"]["name"])


# def prettify(json_to_format):
#     import json
#     return print(json.dumps(json_to_format, indent=3))


# prettify(response.json())
