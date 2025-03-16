#!/usr/bin/python3
"""Script that gets user data (Todo list) from API
and then export the result to a CSV file."""

import csv
import requests
import sys

def main():
    """Main function"""
    user_id = int(sys.argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    # Get the employee data (username)
    response = requests.get(user_url)
    user_name = response.json().get('username')

    # Get the todos data
    response = requests.get(todo_url)
    tasks = response.json()

    # File name
    file_name = "{}.csv".format(user_id)

    # Open the CSV file and write the data
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write each task data for the specific user
        for task in tasks:
            if task.get('userId') == user_id:
                writer.writerow([user_id, user_name, task.get('completed'), task.get('title')])

if __name__ == "__main__":
    main()

