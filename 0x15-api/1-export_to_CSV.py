#!/usr/bin/python3
"""Python script to get data from an API and convert to JSON."""
import json
import requests
import sys


def fetch_user_data(user_id):
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def fetch_tasks(user_id):
    url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def export_to_json(user_id, username, tasks):
    dict_data = {str(user_id): []}
    for task in tasks:
        dict_data[str(user_id)].append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })
    with open(f'{user_id}.json', 'w') as json_file:
        json.dump(dict_data, json_file)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: {} <USER_ID>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]

    try:
        user_data = fetch_user_data(user_id)
        tasks = fetch_tasks(user_id)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

    username = user_data.get("username")
    export_to_json(user_id, username, tasks)
