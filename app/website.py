#!venv/bin/python3
import json
import jinja2

env = jinja2.Environment(
    loader = jinja2.PackageLoader('app', 'templates'),
    autoescape=jinja2.select_autoescape(['html', 'xml'])
)

def ga(eventCategory, eventAction):
    return "ga('send', 'event', {{eventCategory: '{eventCategory}', eventAction: '{eventAction}'}})".format(eventCategory=eventCategory, eventAction=eventAction)

env.globals.update(ga=ga)

index_template = env.get_template('index.html.jinja')
css_template = env.get_template('styles.css.jinja')

def main(build_directory='build'):
    from app.projects import projects
    for project in projects:
        if project["description"]:
            project["description"] = jinja2.Markup(project["description"])

    print(index_template.render(projects=projects), file=open(f'{build_directory}/index.html', 'w+'))
    print(css_template.render(), file=open(f'{build_directory}/styles.css', 'w+'))
