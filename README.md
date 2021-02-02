# Cliest

This CLI aspires to automate common employment tasks for developers in knowledge worker roles, including:
- Calendar management
- Twitter posts (including searching for articles via news api)
- Music control (haha!)
- Task management
- Note taking

Right now, an MVP is implmented for calendar management, and music control - and you can see the start of the twitter development.
## Software Installation

1. Create a Python virtualenv, activate it, and install dependencies:

   - on windows, you may need to use `python` command where there are references to the `python3` command,
   - on macos/linux, you may need to run sudo apt-get install python3-venv first.)

   ```bash
   $ python3 -m venv env
   $ source env/bin/activate
   $ pip3 install -r requirements-dev.txt
   ```

   - if you are using a distribution of conda, you may want to create a new conda environment, rather than use venv `conda create --name cliest python=3.8 -y`

2. For usage instead, create a virtual environment or a conda environment, then `pip install --editable .` and use the prompt with `cx`.
3. Install the Cliest API logic app, located in `integration/logic-app.json` and add the URL to your .env file.
4. Complete other settings from the .env template.

## Dependencies
This depends on Python 3, and focusses on mac developers in an Office 365 ecosystem.

Twitter posting will rely on a SQL Server database (which is not yet documented in Pulumi), and an Azure function for integration.
## Contributions

Use [semantic commits](https://nitayneeman.com/posts/understanding-semantic-commit-messages-using-git-and-angular/#common-types).

Create a new branch in the [Gitflow style](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow).

Merge your branch [via pull request](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/creating-an-issue-or-pull-request) for review when ready, relating to [the issue](https://guides.github.com/features/issues/).
