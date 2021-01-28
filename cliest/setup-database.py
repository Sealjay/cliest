import click
from PyInquirer import prompt
from schema import connect_to_database, Base


def check_for_go_ahead():
    questions = [
        {
            "type": "confirm",
            "message": "Do you want to go ahead and create the database using the configured connection settings?",
            "name": "outcome",
            "default": True,
        }
    ]
    prompt_output = prompt(questions)
    assert "outcome" in prompt_output
    return prompt_output["outcome"]


@click.command()
def main(run=True):
    """Creates and sets up the databse tables for Cliest."""
    if not check_for_go_ahead():
        click.secho("Creation aborted.", fg="bright_red")
        exit()

    engine = connect_to_database()
    # Create all tables that do not already exist
    Base.metadata.create_all(engine)
    click.secho("Database creation complete!", fg="bright_green")


if __name__ == "__main__":
    main()