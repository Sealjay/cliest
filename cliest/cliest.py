import click
import requests
from tabulate import tabulate
import json
import time
from operator import itemgetter
from PyInquirer import prompt
from dotenv import dotenv_values

config = dotenv_values(".env")
calendar_url = config["CALENDAR_URL"]


@click.group(invoke_without_command=True)
def main():
    """ A CLI for getting employment tasks done. """
    questions = [
        {
            "type": "list",
            "message": "What do you want to do?",
            "name": "function",
            "choices": [
                {"name": "Open Calendar (open-cal)", "value": open_cal},
                {"name": "View Calendar", "value": calendar},
            ],
        }
    ]
    prompt_output = prompt(questions)
    if not "function" in prompt_output:
        return None
    selected_function = prompt_output["function"]()


def structure():
    pass


def twitter():
    pass


@main.command()
def calendar():
    calendar_data = get_calendar()
    filtered_list = filter_calendar_list(calendar_data)
    tabulated_output = tabulate(filtered_list, headers="keys")
    print(tabulated_output)


def get_calendar():
    calendar_request = requests.get(calendar_url)
    calendar_results = json.loads(calendar_request.text)["value"]
    return calendar_results


def filter_calendar_list(list_to_filter, additional_keys=None):
    allowed_keys = ["subject", "start", "end", "isAllDay"]
    if not additional_keys is None:
        allowed_keys += additional_keys
    new_list = []
    for dictionary in list_to_filter:
        new_dictionary = {}
        for (key, value) in dictionary.items():
            if key == "end":
                time_obj = get_time_struct_obj(value)
                if time_obj < time.gmtime():
                    new_dictionary = None
                    break
                value = format_time(value)
            if key == "start":
                value = format_time(value)
            if key == "subject":
                value = (value[:28] + "..") if len(value) > 30 else value
            if key in allowed_keys:
                new_dictionary[key] = value
        if not new_dictionary is None:
            new_list.append(new_dictionary)

    sorted_list = sorted(new_list, key=itemgetter("isAllDay", "start", "end"))
    return sorted_list


@main.command()
def open_cal():
    calendar_data = get_calendar()
    filtered_list = filter_calendar_list(calendar_data, ["id", "webLink"])
    questions = [
        {
            "type": "list",
            "message": "Which calendar event do you want to open?",
            "name": "id",
            "choices": list(
                map(
                    lambda option: {
                        "name": f"{option['subject']} ({option['start']}-{option['end']})",
                        "value": option["id"],
                    },
                    filtered_list,
                )
            ),
        }
    ]
    prompt_output = prompt(questions)
    if not id in prompt_output:
        click.secho("ID not found, cancelling.", fg="bright_red")
        return None
    selected_id = prompt_output["id"]
    related_dictionary = find_item("id", selected_id, filtered_list)
    subject = related_dictionary["subject"]
    url = related_dictionary["webLink"]
    click.secho("Subject: ", fg="yellow", nl=False, bold=True)
    click.secho(subject, fg="bright_green")
    click.secho("URL: ", fg="yellow", nl=False, bold=True)
    click.secho(url, fg="bright_white", underline=True)
    click.launch(url)


def find_item(find_key, find_value, search_dictionary):
    for dictionary in search_dictionary:
        if find_key in dictionary:
            if dictionary[find_key] == find_value:
                return dictionary
    return None


def get_time_struct_obj(time_string):
    time_struct_obj = time.strptime(time_string, "%Y-%m-%dT%H:%M:%S.0000000")
    return time_struct_obj


def format_time(time_string):
    time_struct = get_time_struct_obj(time_string)
    formatted_time_string = time.strftime("%H:%M", time_struct)
    return formatted_time_string


def tasks():
    pass


def settings():
    pass


if __name__ == "__main__":
    main()