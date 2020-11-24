from datetime import datetime, date, timedelta
import json
import requests

bacon_open_url = "http://mantis.com/api/rest/issues?project_id=37&filter_id=100&page_size=900"
bacon_closed_url = "http://mantis.com/api/rest/issues?project_id=37&filter_id=1115&page_size=170"
zulu_open_url = "http://mantis.com/api/rest/issues?project_id=36&filter_id=100&page_size=900"
zulu_closed_url = "http://mantis.com/api/rest/issues?project_id=36&filter_id=1115&page_size=170"

projects = [bacon_open_url, bacon_closed_url, zulu_open_url, zulu_closed_url]

header = {"Authorization": "token_goes_here"}

open_today = 0
resolved_today = 0
today = date.today() - timedelta(days=0)

with open("project_stats.txt", "a") as stats_file:
    stats_file.write(f"{today:%d %b %Y}, ")
for index, project in enumerate(projects, start=1):
    response = requests.get(project, headers=header)
    issues = response.json()["issues"]    # JSON object to a dict inside a list
    if "filter_id=100" in project:
        open_today += len([issue["id"] for issue in issues])
    elif "filter_id=1115" in project:
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


# def prettify(x):
#     formatted = json.dumps(x, indent=3)
#     print(formatted)


# data = response.json()
# prettify(data)
