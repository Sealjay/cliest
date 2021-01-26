# Cliest

## Installation

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

## Contributions

Use [semantic commits](https://nitayneeman.com/posts/understanding-semantic-commit-messages-using-git-and-angular/#common-types).

Create a new branch in the [Gitflow style](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow).

Merge your branch [via pull request](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/creating-an-issue-or-pull-request) for review when ready, relating to [the issue](https://guides.github.com/features/issues/).
