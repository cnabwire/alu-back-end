#!/usr/bin/python3
"""Script to export user TODO list data to a JSON file."""

import json
import requests
import sys


def fetch_user_data(user_id):
    """Fetches user information from the API."""
    user_url = "https://jsonplaceholder.typicode.com/users/" + str(user_id)
    response = requests.get(user_url)
    if response.status_code != 200:
        print("Error: Unable to fetch user data")
        sys.exit(1)
    return response.json()


def fetch_todo_data(user_id):
    """Fetches TODO list data from the API."""
    todo_url = "https://jsonplaceholder.typicode.com/todos?userId=" + str(user_id)
    response = requests.get(todo_url)
    if response.status_code != 200:
        print("Error: Unable to fetch TODO data")
        sys.exit(1)
    return response.json()


def export_to_json(user_id, username, tasks):
    """Exports tasks to a JSON file in the required format."""
    file_name = str(user_id) + ".json"
    task_list = []
    for task in tasks:
        task_list.append({
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        })
    data = {str(user_id): task_list}
    with open(file_name, mode="w", encoding="utf-8") as file:
        json.dump(data, file)


def main():
    """Main function."""
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <USER_ID>")
        sys.exit(1)
    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("Error: USER_ID must be an integer")
        sys.exit(1)
    user_data = fetch_user_data(user_id)
    todo_data = fetch_todo_data(user_id)
    export_to_json(user_id, user_data["username"], todo_data)
    print("Data successfully exported to", str(user_id) + ".json")


if __name__ == "__main__":
    main()

