"""Library used for controlling Apple Music"""
import click
from PyInquirer import prompt


def prompt_to_select_station():
    """Shows a prompt then opens a music station."""
    questions = [
        {
            "type": "list",
            "message": "Which calendar event do you want to open?",
            "name": "url",
            "choices": [
                {
                    "name": "Favourites",
                    "value": "itmss://music.apple.com/gb/playlist/"
                    + "favourites-mix/pl.pm-20e9f373919da0803b5df847f4690cca",
                },
                {
                    "name": "Get Up! Mix",
                    "value": "itmss://music.apple.com/gb/playlist/"
                    + "get-up-mix/pl.pm-20e9f373919da0809934e84dac910279",
                },
                {
                    "name": "New Music Mix",
                    "value": "itmss://music.apple.com/gb/playlist/"
                    + "new-music-mix/pl.pm-20e9f373919da080ebe5728cc1b6f437",
                },
            ],
        }
    ]
    prompt_output = prompt(questions)
    if not "url" in prompt_output:
        click.secho("Url not found, cancelling.", fg="bright_red")
    else:
        selected_url = prompt_output["url"]
        click.secho("URL: ", fg="yellow", nl=False, bold=True)
        click.secho(selected_url, fg="bright_white", underline=True)
        click.launch(selected_url)
