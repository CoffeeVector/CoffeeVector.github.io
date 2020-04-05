#!venv/bin/python3
import json
import jinja2
import colorsys

env = jinja2.Environment(
    loader = jinja2.PackageLoader('app', 'templates'),
    autoescape=jinja2.select_autoescape(['html', 'xml'])
)

def ga(eventCategory, eventAction):
    return "ga('send', 'event', {{eventCategory: '{eventCategory}', eventAction: '{eventAction}'}})".format(eventCategory=eventCategory, eventAction=eventAction)

def hex_to_rgb(hex): # input is in the format #rrggbb
    return tuple( int(hex[i:i+2], 16) for i in (1, 3, 5) )

def rgb_to_hex(r, g, b): # input is r, g, and b integers
    r = int(r)
    g = int(g)
    b = int(b)
    return f"#{r:0{2}x}{g:0{2}x}{b:0{2}x}"

def complementary(r, g, b):
    hsv = colorsys.rgb_to_hsv(r, g, b)
    return colorsys.hsv_to_rgb((hsv[0] - 137.507764/360) % 1, hsv[1], hsv[2])

def link_color(r, g, b):
    hsv = colorsys.rgb_to_hsv(r, g, b)
    return colorsys.hsv_to_rgb(hsv[0], 0.95, hsv[2])


env.globals.update(
    ga=ga,
    hex_to_rgb=hex_to_rgb,
    rgb_to_hex=rgb_to_hex,
    complementary=complementary,
    link_color=link_color
)

index_template = env.get_template('index.html.jinja')
css_template = env.get_template('styles.css.jinja')



def main(build_directory='build', theme='allure'):
    from app.projects import projects
    for project in projects:
        if project["description"]:
            project["description"] = jinja2.Markup(project["description"])

    print(index_template.render(
        projects=projects,
        theme=theme
    ), file=open(f'{build_directory}/index.html', 'w+'))
    print(css_template.render(
        theme=theme
    ), file=open(f'{build_directory}/styles.css', 'w+'))
