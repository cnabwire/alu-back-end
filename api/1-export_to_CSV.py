#!/usr/bin/python3
"""Script to export user TODO list data to a CSV file."""

import csv
import requests
import sys


def fetch_user_data(user_id):
    """Fetches user information from the API."""
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(user_url)
    if response.status_code != 200:
        print("Error: Unable to fetch user data")
        sys.exit(1)
    return response.json()

# Fetches TODO list data from the API#


def fetch_todo_data(user_id):
    todo_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
    )
    response = requests.get(todo_url)
    if response.status_code != 200:
        print("Error: Unable to fetch TODO data")
        sys.exit(1)
    return response.json()


def export_to_csv(user_id, username, tasks):
    """Exports tasks to a CSV file in the required format."""
    file_name = "{}.csv".format(user_id)
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow(
                [user_id, username, task['completed'], task['title']]
            )


def main():
    """Main function."""
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <USER_ID>")
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("Error: USER_ID must be an integer")
        sys.exit(1)

    user_data = fetch_user_data(user_id)
    todo_data = fetch_todo_data(user_id)
    export_to_csv(user_id, user_data['username'], todo_data)
    print("Data successfully exported to {}.csv".format(user_id))


if __name__ == "__main__":
    main()
