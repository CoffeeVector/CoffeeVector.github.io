#!venv/bin/python3
import json
import jinja2
from jinja2 import Template
from jinja2 import PackageLoader
from jinja2 import select_autoescape

env = jinja2.Environment(
    loader = jinja2.PackageLoader('main', 'templates'),
    autoescape=jinja2.select_autoescape(['html', 'xml'])
)

def ga(eventCategory, eventAction):
    return "ga('send', 'event', {{eventCategory: '{eventCategory}', eventAction: '{eventAction}'}})".format(eventCategory=eventCategory, eventAction=eventAction)

env.globals.update(ga=ga)


index_template = env.get_template('index.html')

with open('build/index.html', 'w+') as f:
    with open("projects.json", "r") as p:
        content = p.read()
        projects = json.loads(content)
        for project in projects:
            if project["description"]:
                project["description"] = "\n".join(project["description"])

        f.write(index_template.render(
            projects=projects
        ))
