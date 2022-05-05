import requests
import json
from datetime import datetime, timedelta
from prettytable import PrettyTable
import smtplib
from smtplib import SMTPException

github_url = "https://github.com/microsoft/vstest"
url_parts = github_url.split("/")
owner = url_parts[-2]
repo = url_parts[-1]
github_api_url = "https://api.github.com/repos/"+owner+"/"+repo+"/pulls"
to_email = ""
from_email = ""
days = 7
page = 1

olddate = datetime.now().date() - timedelta(days=days)
data = []
############# Get All data from API except older than days = 7
def get_all_pulls(page,data):
    keep_looping = True
    while keep_looping:
        param = {
            "state" : "all",
            "per_page" : 100,
            "page": page
        }
        res = requests.get(github_api_url, params=param)

        pulls = json.loads(res.text)
        data.extend(pulls)
        first_created_date = datetime.strptime(pulls[0]["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        last_created_date = datetime.strptime(pulls[-1]["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        page += 1
        if first_created_date.date() >= olddate and last_created_date.date() >= olddate:
            continue
        else:
            keep_looping = False
    return data
def sending_mail_content(body):
    message = """From: Github Reports <githubpr@gmail.com>
To: Amrit Sharma <sharmaamrit@gmail.com>
Subject:  Last One Week Pull Request Status

Hi, 
<h1> Below is the Last Week Pull Request Status Data</h1>
"""
    message = message + str(body)
    print(message)


if __name__ == "__main__":
    data  = get_all_pulls(page=page, data=data)
    t = PrettyTable(['S.No', 'Pull ID', 'Title', 'User Name', 'State', 'Created At'])
    count = 1
    for pull in data:
        created_date = datetime.strptime(pull["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        if created_date.date() >= olddate:
            t.add_row([count, pull["number"], pull["title"],  pull["user"]["login"], pull["state"], created_date])
        count += 1
    t.align = "l"
    sending_mail_content(body=t)
