"""Library used for Office 365 command prompts"""
import time
from operator import itemgetter
import requests
import click
from tabulate import tabulate
from PyInquirer import prompt
import misc

API_URL = (
    "https://prod-119.westus.logic.azure.com:443/"
    "workflows/00335445955040c49128a6b2b0caf26c/"
    "triggers/manual/paths/invoke?api-version=2016-06-01"
    "&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=apm9AC5jDLD"
    "g5djylrY7Xz6OzcL34vb6he0sqRxfqfo"
)


def print_tabulated_calendar():
    """Returns calendar data in tabulated format."""
    calendar_data = get_calendar()
    filtered_list = filter_calendar_list(calendar_data)
    tabulated_output = tabulate(filtered_list, headers="keys")
    print(tabulated_output)


def prompt_to_open_calendar_event():
    """Shows a prompt then opens a particular calendar invite online."""
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
    if not "id" in prompt_output:
        click.secho("ID not found, cancelling.", fg="bright_red")
    else:
        selected_id = prompt_output["id"]
        related_dictionary = misc.find_item("id", selected_id, filtered_list)
        subject = related_dictionary["subject"]
        url = related_dictionary["webLink"]
        click.secho("Subject: ", fg="yellow", nl=False, bold=True)
        click.secho(subject, fg="bright_green")
        click.secho("URL: ", fg="yellow", nl=False, bold=True)
        click.secho(url, fg="bright_white", underline=True)
        click.launch(url)


def get_calendar():
    """Get calendar results from Office 365."""
    calendar_request = request_from_api("get-calendar")
    assert "value" in calendar_request
    return calendar_request["value"]


def request_from_api(action, item_id="default_id"):
    """Call the logic app/power automate posted online."""
    send_request = requests.post(API_URL, json={"action": action, "id": item_id})
    request_results = send_request.json()
    return request_results


def filter_calendar_list(list_to_filter, additional_keys=None):
    """Filter out unused calendar elements."""
    allowed_keys = ["subject", "start", "end", "isAllDay"]
    if not additional_keys is None:
        allowed_keys += additional_keys
    new_list = []
    for dictionary in list_to_filter:
        new_dictionary = {}
        for (key, value) in dictionary.items():
            if key == "end":
                time_obj = misc.get_time_struct_obj(value)
                if time_obj < time.gmtime():
                    new_dictionary = None
                    break
                value = misc.format_hour_minute_time(value)
            if key == "start":
                value = misc.format_hour_minute_time(value)
            if key == "subject":
                value = (value[:28] + "..") if len(value) > 30 else value
            if key in allowed_keys:
                new_dictionary[key] = value
        if not new_dictionary is None:
            new_list.append(new_dictionary)

    sorted_list = sorted(new_list, key=itemgetter("isAllDay", "start", "end"))
    return sorted_list


def get_tasks():
    """Get the office 365 tasks."""
    tasks_request = request_from_api("get-tasks")
    return tasks_request


def filter_task_list(list_to_filter, additional_keys=None):
    """Filter task to used task elements."""
    allowed_keys = ["subject", "start", "end", "isAllDay"]
    if not additional_keys is None:
        allowed_keys += additional_keys
    new_list = []
    for dictionary in list_to_filter:
        new_dictionary = {}
        for (key, value) in dictionary.items():
            if key == "end":
                time_obj = misc.get_time_struct_obj(value)
                if time_obj < time.gmtime():
                    new_dictionary = None
                    break
                value = misc.format_time(value)
            if key == "start":
                value = misc.format_time(value)
            if key == "subject":
                value = (value[:28] + "..") if len(value) > 30 else value
            if key in allowed_keys:
                new_dictionary[key] = value
        if not new_dictionary is None:
            new_list.append(new_dictionary)

    sorted_list = sorted(new_list, key=itemgetter("isAllDay", "start", "end"))
    return sorted_list
