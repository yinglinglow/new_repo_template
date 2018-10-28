# New Repository Template

This is a starter template for creating new repositories/projects.
Project structure is designed for pytest and pipenv.

Setup:
1) `mkdir myproject; cd myproject`
2) `pipenv install`
3) `pipenv install pytest`
4) Write your tests and stuff
5) To run your tests without all the problems of importing and stuff, run pytest as a module on its own with `pipenv shell python -m pytest tests`. Check Stefano's answer out for more details: https://stackoverflow.com/questions/10253826/path-issue-with-pytest-importerror-no-module-named-yadayadayada
6) To exit pipenv shell, type `exit`

*If you are on pip 18.1 and are hitting an error message, check this out (saved my life!): https://stackoverflow.com/questions/52706769/pipenv-trouble-on-macos-typeerror-module-object-is-not-callable