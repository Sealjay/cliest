"""Top level CLI for completing general employment tasks, in the area of:
    - Twitter
    - Calendar
    - Tasks
    - Curating tweets"""
import click
from PyInquirer import prompt
import o365
import music


@click.group()
def main():
    """ A CLI for getting employment tasks done. """


@main.command("p")
def run_interactive_prompt():
    """An interactive prompt to run through all available options."""
    questions = [
        {
            "type": "list",
            "message": "What do you want to do?",
            "name": "function",
            "choices": [
                {"name": "View Calendar", "value": o365.print_tabulated_calendar},
                {
                    "name": "Open Calendar (open-cal)",
                    "value": o365.prompt_to_open_calendar_event,
                },
                {"name": "View Tasks", "value": o365.get_tasks},
                {"name": "Open Music", "value": music.prompt_to_select_station},
            ],
        }
    ]
    prompt_output = prompt(questions)
    if "function" in prompt_output:
        prompt_output["function"]()


def structure():
    """Reserved for sorting out day planning functions."""
    raise NotImplementedError


def twitter():
    """Reserved for creating tweets."""
    raise NotImplementedError


@main.command()
def calendar():
    """Prints out calendar - used for Click decorator."""
    o365.print_tabulated_calendar()


@main.command()
def open_cal():
    """Opens a calendar event - used for Click decorator."""
    o365.prompt_to_open_calendar_event()


@main.command()
def play_music():
    """Opens a station in Apple Music."""
    music.prompt_to_select_station()


if __name__ == "__main__":
    main()
