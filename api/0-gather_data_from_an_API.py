#!/usr/bin/python3
"""Script that fetches a user's TODO list progress from an API"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 0-gather_data_from_an_API.py <user_id>")

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        sys.exit("Error: User ID must be an integer")

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)

    # Fetch user details
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        sys.exit("Error: User not found")

    user_name = user_response.json().get("name")

    # Fetch TODO list
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        sys.exit("Error: Could not fetch TODO list")

    todos = todos_response.json()
    completed_tasks = [todo["title"] for todo in todos if todo["completed"]]
    total_tasks = len(todos)

    # Print output in required format
    print("Employee {} is done with tasks({}/{}):".format(user_name, len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task))

