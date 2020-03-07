#!venv/bin/python3
import json
import jinja2

env = jinja2.Environment(
    loader = jinja2.PackageLoader('main', 'templates'),
    autoescape=jinja2.select_autoescape(['html', 'xml'])
)

def ga(eventCategory, eventAction):
    return "ga('send', 'event', {{eventCategory: '{eventCategory}', eventAction: '{eventAction}'}})".format(eventCategory=eventCategory, eventAction=eventAction)

env.globals.update(ga=ga)


index_template = env.get_template('index.html.jinja')
css_template = env.get_template('styles.css.jinja')

with open('build/index.html', 'w+') as f:
    from projects import projects
    for project in projects:
        if project["description"]:
            project["description"] = jinja2.Markup(project["description"])

    f.write(index_template.render(
        projects=projects
    ))

with open('build/styles.css', 'w+') as f:
    f.write(css_template.render())
