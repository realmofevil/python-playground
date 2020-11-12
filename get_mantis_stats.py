from datetime import datetime, date     # , timedelta
import json
import requests

# TODO: oh and try to make everything more readable and neat

bacon_open_url = "http://mantis.com/api/rest/issues?project_id=37&filter_id=100&page_size=900"
bacon_closed_url = "http://mantis.com/api/rest/issues?project_id=37&filter_id=1115&page_size=170"
zulu_open_url = "http://mantis.com/api/rest/issues?project_id=36&filter_id=100&page_size=900"
zulu_closed_url = "http://mantis.com/api/rest/issues?project_id=36&filter_id=1115&page_size=170"

projects = [bacon_open_url, bacon_closed_url, zulu_open_url, zulu_closed_url]

header = {"Authorization": "token_goes_here"}


open_today = 0
resolved_today = 0

for project in projects:
    response = requests.get(project, headers=header)
    issues = json.loads(response.text)["issues"]    # JSON object to a dict inside a list
    issue_id = [issue["id"] for issue in issues]    # print(issues[0]["id"], issues[0]["project"]["name"])
    if "filter_id=100" in project:
        open_today += len(issue_id)
    if "filter_id=1115" in project:
        get_datetime = [issue["updated_at"] for issue in issues]    # %Y-%m-%dT%H:%M:%S%z ISO 8601 format
        for issue in get_datetime:
            resolved_date = datetime.fromisoformat(issue).date()    # make this a list comprehension and .count() it
            today = date.today()    # - timedelta(days=1)
            if resolved_date == today:
                resolved_today += 1
        with open("project_stats.txt", "a") as stats_file:
            stats_file.write(f"{date.today().strftime('%d %b %Y')}, Open: {open_today} / Resolved: {resolved_today} -"
                             f" {'SimsWorld' if 'project_id=37' in project else 'JA'}\n")
        open_today = 0
        resolved_today = 0


# debug helpers

pid = [issue["project"]["id"] for issue in issues]
status = [issue["status"]["name"] for issue in issues]
pid_status = list(zip(pid, status))
issue_filter = [(issue["project"]["id"] == 37 or issue["project"]["id"] == 39)
                for issue in issues
                if (issue["resolution"]["name"] == "open" or issue["resolution"]["name"] == "reopened")]
check = list(zip(pid_status, issue_filter))


def prettify(x):
    formatted = json.dumps(x, indent=3)
    print(formatted)


# data = response.json()
# prettify(data)

# filter per project, including subprojects (something is off with the results by -/+5 )
zulu_open = [(issue["project"]["id"] == 36 or issue["project"]["id"] == 38 or issue["project"]["id"] == 40)
             and (issue["resolution"]["name"] == "open" or issue["resolution"]["name"] == "reopened")
             for issue in issues].count(True)
bacon_open = [(issue["project"]["id"] == 37 or issue["project"]["id"] == 39)
              and issue["resolution"]["name"] == "open" or issue["resolution"]["name"] == "reopened"
              for issue in issues].count(True)
zulu_closed = [(issue["project"]["id"] == 36 or issue["project"]["id"] == 38 or issue["project"]["id"] == 40)
               and issue["status"]["name"] == "resolved" or issue["status"]["name"] == "closed"
               for issue in issues].count(True)
bacon_closed = [(issue["project"]["id"] == 37 or issue["project"]["id"] == 39)
                and issue["status"]["name"] == "resolved" or issue["status"]["name"] == "closed"
                for issue in issues].count(True)
