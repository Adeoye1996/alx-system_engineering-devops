#!/usr/bin/python3
'''
Let gather the employee data from API
'''

import json
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"


def get_employee_data(employee_id):
    user_response = requests.get(
        '{}/users/{}'.format(REST_API, employee_id)
    )
    todos_response = requests.get(
        '{}/todos'.format(REST_API)
    )

    if user_response.status_code == 200 and todos_response.status_code == 200:
        user_data = user_response.json()
        todos_data = todos_response.json()
        return user_data, todos_data
    return None, None


def export_to_json(employee_id, employee_name, tasks):
    filename = '{}.json'.format(employee_id)
    task_list = [
        {
            'task': task['title'],
            'completed': task['completed'],
            'username': employee_name
        }
        for task in tasks
    ]
    employee_tasks = {str(employee_id): task_list}
    with open(filename, 'w') as jsonfile:
        json.dump(employee_tasks, jsonfile)
    print('Data exported to {}'.format(filename))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1].isdigit():
            employee_id = int(sys.argv[1])
            user_data, todos_data = get_employee_data(employee_id)

            if user_data and todos_data:
                employee_name = user_data.get('name')
                tasks = [
                    task for task in todos_data
                    if task.get('userId') == employee_id
                ]
                export_to_json(employee_id, employee_name, tasks)
            else:
                print('Error fetching data from API.')
        else:
            print('Please provide a valid integer employee ID.')
    else:
        print('Usage: {} <employee_id>'.format(sys.argv[0]))
