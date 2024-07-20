"""
from jinja2 import Environment, FileSystemLoader

he Environment and FileSystemLoader classes from the jinja2 module are used to
create and manage templates in Python. Jinja2 is a powerful and flexible templating engine for Python,
often used for generating HTML, XML, or other markup formats.

Here's a breakdown of what these classes do and how you can use them:

Environment
The Environment class is the central object in Jinja2. It contains configuration data and global objects
that will be used during the template rendering process.
It provides methods for loading templates, rendering templates, and configuring the template environment.

FileSystemLoader
The FileSystemLoader class is a loader for loading templates from the file system.
It takes a path to a directory (or list of directories) where templates are stored and loads templates
from these directories.
"""
from jinja2 import Environment, FileSystemLoader
file_loader = FileSystemLoader('/Users/sakshamsaxena/PycharmProjects/python_tut/tut_python/templates')
env = Environment(loader=file_loader)
template = env.get_template('example_template.html')
context = {
    'title': 'Jinja2 Template Example',
    'heading': 'Hello, World!',
    'content': 'This is an example of rendering a template with Jinja2.'
}
rendered_template = template.render(context)
print(rendered_template)
