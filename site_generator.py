
import markdown
from jinja2 import Environment, FileSystemLoader, Template, select_autoescape
from os import path, listdir
import sys
print(sys.version)
templates_dir = path.join('./templates')
word_list = ['mama', 'papa']

env = Environment(
    loader=FileSystemLoader(searchpath='./templates/'),
    autoescape=True,
    trim_blocks=False
)

for file in listdir(templates_dir):
    print(file)


template = env.get_template('index.html.j2')


with open('./articles/0_tutorial/14_google.md', 'r', encoding='utf-8') as md_file:
    md_html = markdown.markdown(md_file.read(), extension='codehilite')

# with open('./templates/layout.html.j2', 'r') as fh_layout_tamplate:
#     layout_tamplate = env.parse(fh_layout_tamplate.read())

with open('static/index.html', 'w', encoding='utf-8') as index_fh:
    index_fh.write(template.render(
        title='Энциклопедия!'
    ))


def markdown_to_html(mdfile):
    with open(mdfile, 'r', encoding='utf-8') as md_file:
        html = markdown.markdown(md_file.read(), extension='codehilite')
        return html


article_html = markdown_to_html('./articles/0_tutorial/14_google.md')

with open('static/article.html', 'w', encoding='utf-8') as article_fh:
    article_fh.write(
        env.get_template('article.html.j2').render(
            title='Гугол!',
            content=article_html
        ))
