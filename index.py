from flask import Flask, render_template
from urllib2 import urlopen
import simplejson

app = Flask("CobraTeam Website")

@app.route("/")
def index():
    members = get_members()
    projects = get_projects()
    return render_template("index.html", members=members, projects=projects)

def get_members():
    users = simplejson.load(urlopen('https://github.com/api/v2/json/organizations/cobrateam/public_members'))
    members = []
    for user in users['users']:
        members.append((user['name'], user['login']))

    return members

def get_projects():
    repositories = simplejson.load(urlopen('https://github.com/api/v2/json/organizations/cobrateam/public_repositories'))
    projects = []
    for project in repositories['repositories']:
        projects.append((project['name'], project['url']))

    return projects

if __name__ == "__main__":
    app.run(debug=True)
