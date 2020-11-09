import json
import requests

total_zulu_open = 0
total_zulu_closed = 0
total_bacon_open = 0
total_bacon_closed = 0

# TODO: refactor the whole shit with an ampersand chained filter per project, fucking mantis api docs not explaining it
# TODO: remove this scraping code that cost me more than two days to figure out and finally use the filter
# TODO: fucking lazy idiots https://www.mantisbt.org/bugs/view.php?id=27489 not documenting anything
# TODO: oh and try to make everything more readable and neat
for page in (1, 2, 3):
    url = f"http://mantis..com/api/rest/issues?page_size=70&page={page}"
    header = {"Authorization": ""}

    response = requests.get(url, headers=header)  # .json()

    issues = json.loads(response.text)["issues"]  # JSON object to a dict

    # print(issues[0]["id"], issues[0]["project"]["name"])

    pid = [issue["project"]["id"] for issue in issues]
    status = [issue["status"]["name"] for issue in issues]
    pid_status = list(zip(pid, status))
    bool_check = [(issue["project"]["id"] == 36 or issue["project"]["id"] == 38 or issue["project"]["id"] == 40)
                  for issue in issues
                  if (issue["resolution"]["name"] == "open" or issue["resolution"]["name"] == "reopened")]

    # if zulu in project and zulu in date

    # filter per project, including subprojects
    zulu_open = [(issue["project"]["id"] == 36 or issue["project"]["id"] == 38 or issue["project"]["id"] == 40)
                 and issue["resolution"]["name"] == "open" or issue["resolution"]["name"] == "reopened"
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

    total_zulu_open += zulu_open
    total_zulu_closed += zulu_closed
    total_bacon_open += bacon_open
    total_bacon_closed += bacon_closed

# with open("project_stats.txt", "a") as stats_file:
#     stats_file.write(f"zulu open/closed: {total_zulu_open}/{total_zulu_closed}"
#                      f" bacon open/closed: {total_bacon_open}/{total_bacon_closed}")


# debug helpers

# print(pid_status)
final_check = list(zip(pid_status, bool_check))
print(final_check)
print(zulu_open)


def prettify(x):
    formatted = json.dumps(x, indent=3)
    print(formatted)


# data = response.json()
# prettify(data)


# print(response.text)  # To print formatted JSON response


