#!/usr/bin/python3
"""Fetch data from an API and export to a JSON file."""
import json
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <USER_ID>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]
    url_to_user = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    
    user_response = requests.get(url_to_user)
    if user_response.status_code != 200:
        print("Error fetching user data.")
        sys.exit(1)

    username = user_response.json().get('username')
    
    url_to_tasks = f'{url_to_user}/todos'
    tasks_response = requests.get(url_to_tasks)
    if tasks_response.status_code != 200:
        print("Error fetching tasks data.")
        sys.exit(1)

    tasks = tasks_response.json()

    user_tasks = {user_id: []}
    for task in tasks:
        task_completed_status = task.get('completed')
        task_title = task.get('title')
        user_tasks[user_id].append({
            "task": task_title,
            "completed": task_completed_status,
            "username": username
        })

    with open(f'{user_id}.json', 'w') as json_file:
        json.dump(user_tasks, json_file)
