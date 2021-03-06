from decorators import minified_response
from flask import Flask, render_template
from urllib2 import urlopen
import simplejson

app = Flask("CobraTeam Website")

@app.route("/")
@minified_response
def index():
    members = get_members()
    projects = get_projects()
    return render_template("index.html", members=members, projects=projects)

def get_members():
    users = simplejson.load(urlopen('https://github.com/api/v2/json/organizations/cobrateam/public_members'))
    members = []
    for user in sorted(users['users'], key=lambda x: x['name']):
        members.append((user['name'], user['login'], user['gravatar_id']))

    return members

def get_projects():
    repositories = simplejson.load(urlopen('https://github.com/api/v2/json/organizations/cobrateam/public_repositories'))
    projects = []
    for project in reversed(sorted(repositories['repositories'], key=lambda x: x['watchers'])):
        projects.append((project['name'], project['url'], project['description']))

    return projects

if __name__ == "__main__":
    app.run(debug=True)
