#!/usr/bin/python3
"""Python script to get data from an API and convert to JSON."""
import json
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <USER_ID>".format(sys.argv[0]))
        sys.exit(1)

    USER_ID = sys.argv[1]
    url_to_user = f'https://jsonplaceholder.typicode.com/users/{USER_ID}'
    user_response = requests.get(url_to_user)

    if user_response.status_code != 200:
        print("Error fetching user data.")
        sys.exit(1)

    USERNAME = user_response.json().get('username')
    url_to_tasks = f'{url_to_user}/todos'
    tasks_response = requests.get(url_to_tasks)

    if tasks_response.status_code != 200:
        print("Error fetching tasks data.")
        sys.exit(1)

    tasks = tasks_response.json()
    dict_data = {USER_ID: []}

    for task in tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        dict_data[USER_ID].append({
            "task": TASK_TITLE,
            "completed": TASK_COMPLETED_STATUS,
            "username": USERNAME
        })

    with open(f'{USER_ID}.json', 'w') as json_file:
        json.dump(dict_data, json_file)
