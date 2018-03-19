{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{{ cookiecutter.project_short_description }}

Install
--------
# apt install virtualenv python3 python3-pip cookiecutter
# cookiecutter https://github.com/orseni/cookiecutter-bottle-psycopg2.git
# cd <project_name>
# virtualenv -p /usr/bin/python3 venv
# source venv/bin/activate
# ./install_dependences.sh

Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `orseni/cookiecutter-bottle-psycopg2`_ project template.

.. _Cookiecutter: https://github.com/orseni/cookiecutter-bottle-psycopg2
